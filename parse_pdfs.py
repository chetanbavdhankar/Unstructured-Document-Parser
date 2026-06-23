# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "docling",
#     "liteparse",
#     "marker-pdf",
#     "rapidocr-onnxruntime",
# ]
# ///

import os
import argparse
import urllib.request
import subprocess
import json

# Try importing the parser modules
try:
    from docling.document_converter import DocumentConverter
except ImportError:
    DocumentConverter = None

try:
    from liteparse import LiteParse
except ImportError:
    LiteParse = None


def parse_with_docling(pdf_path, output_dir, process_images=False):
    print("\n--- Running Docling ---")
    if DocumentConverter is None:
        print("[Error] docling is not installed in the current environment.")
        return False
        
    try:
        is_pdf = pdf_path.lower().endswith(".pdf")
        if is_pdf:
            from docling.datamodel.pipeline_options import PdfPipelineOptions
            from docling.document_converter import PdfFormatOption
            from docling.datamodel.base_models import InputFormat
            
            pipeline_options = PdfPipelineOptions()
            pipeline_options.generate_picture_images = process_images
            pipeline_options.generate_page_images = process_images
            pipeline_options.do_ocr = True
            
            converter = DocumentConverter(
                format_options={
                    InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
                }
            )
        else:
            converter = DocumentConverter()
            
        result = converter.convert(pdf_path)
        markdown_text = result.document.export_to_markdown()
        
        filename = os.path.splitext(os.path.basename(pdf_path))[0] + ".md"
        out_path = os.path.join(output_dir, "docling", filename)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(markdown_text)
            
        print(f"[Success] Docling complete. Saved output to {out_path}")
        return True
    except Exception as e:
        print(f"[Error] Docling failed: {e}")
        return False


# 3. LiteParse Parser
def parse_with_liteparse(pdf_path, output_dir):
    print("\n--- Running LiteParse ---")
    if LiteParse is None:
        print("[Error] liteparse is not installed in the current environment.")
        return False
        
    try:
        parser = LiteParse()
        result = parser.parse(pdf_path)
        
        filename = os.path.splitext(os.path.basename(pdf_path))[0] + ".md"
        out_path = os.path.join(output_dir, "liteparse", filename)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        
        with open(out_path, "w", encoding="utf-8") as f:
            if hasattr(result, "text"):
                f.write(result.text)
            elif hasattr(result, "pages"):
                text = "\n\n".join([page.text for page in result.pages if hasattr(page, "text")])
                f.write(text)
            else:
                f.write(str(result))
                
        print(f"[Success] LiteParse complete. Saved output to {out_path}")
        return True
    except Exception as e:
        print(f"[Error] LiteParse failed: {e}")
        return False


def parse_with_marker(pdf_path, output_dir, process_images=False):
    print("\n--- Running Marker ---")
    try:
        # Run marker_single via command line first as it handles memory and models cleanly.
        out_subdir = os.path.join(output_dir, "marker")
        os.makedirs(out_subdir, exist_ok=True)
        
        # Check if local venv bin exists
        venv_bin = os.path.join(os.getcwd(), ".venv", "bin")
        marker_single_bin = os.path.join(venv_bin, "marker_single")
        if not os.path.exists(marker_single_bin):
            marker_single_bin = "marker_single"
            
        cmd = [marker_single_bin, pdf_path, "--output_dir", out_subdir]
        if not process_images:
            cmd.append("--disable_image_extraction")
            
        print(f"Running command: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
        
        # marker_single creates a subfolder matching the pdf name, let's locate the output
        pdf_name_clean = os.path.splitext(os.path.basename(pdf_path))[0]
        generated_md_path = None
        target_subfolder = os.path.join(out_subdir, pdf_name_clean)
        if os.path.exists(target_subfolder):
            for file in os.listdir(target_subfolder):
                if file.endswith(".md"):
                    generated_md_path = os.path.join(target_subfolder, file)
                    break
        
        if generated_md_path:
            standard_out_path = os.path.join(out_subdir, pdf_name_clean + ".md")
            os.rename(generated_md_path, standard_out_path)
            print(f"[Success] Marker complete. Saved output to {standard_out_path}")
            return True
        else:
            print("[Warning] Marker ran successfully but output markdown file was not found inside standard subfolder. Checking marker output directory...")
            for root, dirs, files in os.walk(out_subdir):
                for file in files:
                    if file.endswith(".md") and not file.startswith("marker"):
                        found_path = os.path.join(root, file)
                        standard_out_path = os.path.join(out_subdir, pdf_name_clean + ".md")
                        os.rename(found_path, standard_out_path)
                        print(f"[Success] Marker complete. Moved output to {standard_out_path}")
                        return True
            return False
            
    except Exception as e:
        print(f"[Error] Marker CLI execution failed: {e}")
        print("Attempting Marker Python API fallback...")
        try:
            from marker.converters.pdf import PdfConverter
            from marker.models import create_model_dict
            
            model_dict = create_model_dict()
            config = {}
            if not process_images:
                config["disable_image_extraction"] = True
                
            converter = PdfConverter(artifact_dict=model_dict, config=config)
            full_text = converter(pdf_path)
            
            filename = os.path.splitext(os.path.basename(pdf_path))[0] + ".md"
            out_path = os.path.join(output_dir, "marker", filename)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(full_text)
                
            print(f"[Success] Marker Python API complete. Saved output to {out_path}")
            return True
        except Exception as py_e:
            print(f"[Error] Marker Python API also failed: {py_e}")
            return False


# Benchmark downloader
def download_benchmark_pdf(target_path):
    print(f"Downloading benchmark PDF to {target_path}...")
    url = "https://arxiv.org/pdf/1706.03762"
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    try:
        urllib.request.urlretrieve(url, target_path)
        print("[Success] Benchmark PDF downloaded successfully.")
        return True
    except Exception as e:
        print(f"[Error] Failed to download benchmark PDF: {e}")
        return False


def find_matching_files(pdf_dir_or_file, file_types, download_benchmark=False):
    target_files = []
    file_types = [ext.lower().lstrip(".") for ext in file_types]
    
    if download_benchmark:
        benchmark_path = "RAG_data/attention_is_all_you_need.pdf"
        if not os.path.exists(benchmark_path):
            download_benchmark_pdf(benchmark_path)
        if os.path.exists(benchmark_path):
            target_files.append(benchmark_path)
    elif pdf_dir_or_file:
        if os.path.exists(pdf_dir_or_file):
            if os.path.isdir(pdf_dir_or_file):
                # Search for all specified extensions (non-recursive)
                for f in os.listdir(pdf_dir_or_file):
                    ext = os.path.splitext(f)[1].lower().lstrip(".")
                    if ext in file_types:
                        target_files.append(os.path.join(pdf_dir_or_file, f))
            elif os.path.isfile(pdf_dir_or_file):
                ext = os.path.splitext(pdf_dir_or_file)[1].lower().lstrip(".")
                if ext in file_types:
                    target_files.append(pdf_dir_or_file)
        else:
            print(f"[Error] Directory/file not found: {pdf_dir_or_file}")
    else:
        # Look for files in RAG_data
        rag_data_dir = "RAG_data"
        if os.path.exists(rag_data_dir):
            for f in os.listdir(rag_data_dir):
                ext = os.path.splitext(f)[1].lower().lstrip(".")
                if ext in file_types:
                    target_files.append(os.path.join(rag_data_dir, f))
            
        if not target_files:
            print(f"[Info] No matching files found in RAG_data. Downloading 'Attention Is All You Need' benchmark PDF by default...")
            benchmark_path = "RAG_data/attention_is_all_you_need.pdf"
            if not os.path.exists(benchmark_path):
                download_benchmark_pdf(benchmark_path)
            if os.path.exists(benchmark_path):
                target_files.append(benchmark_path)
                
    return target_files


def run_parsing_pipeline(files, methods, output_dir, process_images=False):
    selected_methods = [m.lower() for m in methods]
    
    # Process each file
    for file_path in files:
        print(f"\n========================================\nProcessing: {file_path}\n========================================")
        
        # 1. Docling
        if "docling" in selected_methods:
            parse_with_docling(file_path, output_dir, process_images=process_images)
        
        # 2. LiteParse
        if "liteparse" in selected_methods:
            parse_with_liteparse(file_path, output_dir)
        
        # 3. Marker
        if "marker" in selected_methods:
            parse_with_marker(file_path, output_dir, process_images=process_images)


def main():
    parser = argparse.ArgumentParser(description="Parse documents using Docling, LiteParse, and Marker.")
    parser.add_argument("--pdf_dir", type=str, default=None, help="Path to directory containing input files.")
    parser.add_argument("--output_dir", type=str, default="RAG_data/parsed_outputs", help="Output directory path.")
    parser.add_argument("--download_benchmark", action="store_true", help="Download the 'Attention Is All You Need' benchmark PDF.")
    parser.add_argument(
        "--methods",
        nargs="+",
        choices=["docling", "liteparse", "marker"],
        default=["docling", "liteparse", "marker"],
        help="List of parsing methods to run. Options: docling, liteparse, marker"
    )
    parser.add_argument(
        "--file_types",
        nargs="+",
        default=["pdf"],
        help="List of file extensions to search for and parse. Options: pdf, docx, doc, pptx, ppt, xlsx, xls, png, jpg, jpeg, epub, html"
    )
    parser.add_argument(
        "--process_images",
        action="store_true",
        help="Extract and process images embedded in documents (e.g. run OCR, save extracted images)."
    )
    
    args = parser.parse_args()
    
    target_files = find_matching_files(args.pdf_dir, args.file_types, download_benchmark=args.download_benchmark)
    
    if not target_files:
        print("[Error] No files available to process.")
        return
        
    print(f"Found {len(target_files)} file(s) to process: {target_files}")
    print(f"Selected parsing methods: {args.methods}")
    print(f"Process/Extract embedded images: {args.process_images}")
    
    run_parsing_pipeline(target_files, args.methods, args.output_dir, process_images=args.process_images)
    print("\nAll tasks completed!")


if __name__ == "__main__":
    main()
