# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "flask",
#     "docling",
#     "liteparse",
#     "marker-pdf",
#     "rapidocr-onnxruntime",
# ]
# ///

import os
import sys
import queue
import threading
import argparse
import webbrowser
from flask import Flask, render_template, jsonify, request, Response

# Ensure we can import from parse_pdfs.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from parse_pdfs import find_matching_files, run_parsing_pipeline, download_benchmark_pdf

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
print(f"[Debug] template_dir absolute path: {template_dir}")
print(f"[Debug] templates folder exists: {os.path.exists(template_dir)}")
if os.path.exists(template_dir):
    print(f"[Debug] contents of template_dir: {os.listdir(template_dir)}")
app = Flask(__name__, template_folder=template_dir)
print(f"[Debug] Flask root_path: {app.root_path}")
print(f"[Debug] Flask template_folder: {app.template_folder}")

# Global state to track active parsing job
active_job = {
    "status": "idle",  # "idle", "running", "completed"
    "logs": queue.Queue(),
    "thread": None
}

class QueueWriter:
    def __init__(self, q):
        self.q = q
        
    def write(self, message):
        if message:
            self.q.put(message)
            
    def flush(self):
        pass


def execute_parsing_task(files, methods, output_dir, process_images):
    global active_job
    
    # Redirect stdout and stderr to the log queue
    orig_stdout = sys.stdout
    orig_stderr = sys.stderr
    sys.stdout = QueueWriter(active_job["logs"])
    sys.stderr = QueueWriter(active_job["logs"])
    
    try:
        run_parsing_pipeline(files, methods, output_dir, process_images=process_images)
        print("\nAll tasks completed successfully!")
        active_job["status"] = "completed"
    except Exception as e:
        print(f"\n[Error] Parsing thread crashed: {e}")
        active_job["status"] = "failed"
    finally:
        # Restore stdout and stderr
        sys.stdout = orig_stdout
        sys.stderr = orig_stderr
        # Put EOF marker in queue
        active_job["logs"].put(None)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/scan", methods=["GET"])
def scan_directory():
    pdf_dir = request.args.get("pdf_dir", "RAG_data")
    extensions_raw = request.args.get("extensions", "pdf")
    
    file_types = [ext.lower().strip().lstrip(".") for ext in extensions_raw.split(",")]
    
    if not os.path.exists(pdf_dir):
        return jsonify({"error": f"Directory not found: {pdf_dir}", "files": []}), 404
        
    try:
        matching_files = find_matching_files(pdf_dir, file_types, download_benchmark=False)
    except Exception as e:
        return jsonify({"error": f"Failed to read directory: {e}", "files": []}), 500
        
    return jsonify({
        "pdf_dir": pdf_dir,
        "file_types": file_types,
        "files": matching_files
    })


@app.route("/api/parse", methods=["POST"])
def start_parse():
    global active_job
    
    if active_job["status"] == "running":
        return jsonify({"error": "A parsing job is already running."}), 400
        
    data = request.json or {}
    pdf_dir = data.get("pdf_dir", "RAG_data")
    methods = data.get("methods", ["docling", "liteparse", "marker"])
    extensions = data.get("file_types", ["pdf"])
    process_images = bool(data.get("process_images", False))
    output_dir = data.get("output_dir", "RAG_data/parsed_outputs")
    
    # Check if specific files list is provided
    files = data.get("files", [])
    if files:
        # Ensure files exist
        files = [f for f in files if os.path.exists(f)]
    else:
        if not os.path.exists(pdf_dir):
            return jsonify({"error": f"Input directory/file not found: {pdf_dir}"}), 404
            
        try:
            files = find_matching_files(pdf_dir, extensions, download_benchmark=False)
        except Exception as e:
            return jsonify({"error": f"Failed to resolve files: {e}"}), 500
            
    if not files:
        return jsonify({"error": "No files found to process."}), 400
        
    # Reset job logs queue
    active_job["logs"] = queue.Queue()
    active_job["status"] = "running"
    
    # Start thread
    active_job["thread"] = threading.Thread(
        target=execute_parsing_task,
        args=(files, methods, output_dir, process_images),
        daemon=True
    )
    active_job["thread"].start()
    
    return jsonify({"status": "running", "file_count": len(files)})


@app.route("/api/browse", methods=["GET"])
def browse_directory():
    path = request.args.get("path", "")
    if not path or path.strip() == "":
        path = os.getcwd()
    else:
        path = os.path.abspath(path)
        
    if not os.path.exists(path) or not os.path.isdir(path):
        # If it's a file path, get parent dir
        if os.path.exists(path) and os.path.isfile(path):
            path = os.path.dirname(path)
        else:
            path = os.getcwd()
            
    try:
        items = os.listdir(path)
        folders = []
        files = []
        for item in sorted(items):
            if item.startswith("."):
                continue
            item_path = os.path.join(path, item)
            try:
                if os.path.isdir(item_path):
                    folders.append(item)
                else:
                    files.append(item)
            except Exception:
                pass
                
        parent_path = os.path.dirname(path)
        if parent_path == path:
            parent_path = ""
            
        return jsonify({
            "current_path": path,
            "parent_path": parent_path,
            "folders": folders,
            "files": files
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/stream", methods=["GET"])
def stream_logs():
    def generate():
        q = active_job["logs"]
        while True:
            try:
                # Wait up to 10 seconds for a message
                message = q.get(timeout=10)
                if message is None:
                    # Job complete EOF
                    yield "data: __EOF__\n\n"
                    break
                # Send log line
                yield f"data: {message}\n\n"
            except queue.Empty:
                # Keep-alive comment
                yield "data: \n\n"
                
    return Response(generate(), mimetype="text/event-stream")


@app.route("/api/status", methods=["GET"])
def get_status():
    return jsonify({
        "status": active_job["status"],
        "is_running": active_job["status"] == "running"
    })


@app.route("/api/download-benchmark", methods=["POST"])
def trigger_benchmark_download():
    benchmark_path = "RAG_data/attention_is_all_you_need.pdf"
    success = download_benchmark_pdf(benchmark_path)
    if success:
        return jsonify({"status": "success", "file": benchmark_path})
    else:
        return jsonify({"status": "error", "message": "Download failed"}), 500


@app.route("/api/outputs", methods=["GET"])
def list_outputs():
    output_dir = request.args.get("output_dir", "RAG_data/parsed_outputs")
    if not os.path.exists(output_dir):
        return jsonify({"outputs": {}})
        
    outputs = {}
    try:
        # Loop through method subdirectories (docling, liteparse, marker)
        for method in os.listdir(output_dir):
            method_path = os.path.join(output_dir, method)
            if os.path.isdir(method_path) and not method.startswith("."):
                outputs[method] = []
                for f in os.listdir(method_path):
                    if f.endswith(".md") and not f.startswith("."):
                        outputs[method].append({
                            "name": f,
                            "path": os.path.join(method_path, f),
                            "size": os.path.getsize(os.path.join(method_path, f))
                        })
    except Exception as e:
        return jsonify({"error": str(e), "outputs": {}}), 500
        
    return jsonify({"outputs": outputs})


@app.route("/api/output-content", methods=["GET"])
def get_output_content():
    file_path = request.args.get("path")
    if not file_path or not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404
        
    # Basic path safety check
    workspace_dir = os.getcwd()
    abs_path = os.path.abspath(file_path)
    if not abs_path.startswith(os.path.abspath(workspace_dir)):
        return jsonify({"error": "Access denied"}), 403
        
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return jsonify({
            "path": file_path,
            "filename": os.path.basename(file_path),
            "content": content
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start Document Parser Dashboard Server")
    parser.add_argument("--port", type=int, default=5000, help="Port to run Flask server on.")
    parser.add_argument("--host", type=str, default="127.0.0.1", help="Host address.")
    args = parser.parse_args()
    
    # Auto-open browser when the server starts
    # Since debug=True runs a reloader, check WERKZEUG_RUN_MAIN to only open once in the active child process
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        def open_browser():
            webbrowser.open(f"http://{args.host}:{args.port}")
        threading.Timer(1.0, open_browser).start()
        
    print(f"Starting Document Parser Dashboard at http://{args.host}:{args.port}")
    app.run(host=args.host, port=args.port, debug=True)
