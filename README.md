# Unstructured Document Parser (LLM-Ready Markdown Extractor)

This project provides an end-to-end local document parsing pipeline to convert unstructured files (PDF, DOCX, PPTX, XLSX, Images, EPUB, HTML) into clean, structured Markdown. The outputs are highly structured, layout-aware, and optimized for LLM training and RAG (Retrieval-Augmented Generation) pipelines, utilizing three robust engines: **Docling**, **LiteParse**, and **Marker**.

---

## 🛠️ Setup & Execution Instructions

There are two primary ways to run this tool: **without a virtual environment (recommended)** or **using a virtual environment**.

### Option A: Run without a Virtual Environment (Recommended via `uv`)
Since the script contains inline PEP 723 metadata, `uv` can execute it on-the-fly, downloading and managing all parser dependencies automatically in an isolated temporary cache, without altering your global Python environment or requiring you to create/activate a `.venv`:
```bash
uv run parse_pdfs.py --download_benchmark
```
*Note: Any argument you append to `uv run parse_pdfs.py` is passed directly to the script.*

### Option B: Run with standard global/user Pip
If you do not want to use `uv run`, you can install the dependencies globally or in your user space using the requirements.txt file:
```bash
pip install -r requirements.txt
python parse_pdfs.py --download_benchmark
```

### Option C: Run with local Virtual Environment
If you prefer a standard local virtual environment:
1. **Activate Virtual Environment**:
   ```bash
   source .venv/bin/activate
   ```
2. **Execute**:
   ```bash
   python parse_pdfs.py --download_benchmark
   ```

## 🌐 Web UI Dashboard

In addition to the CLI, you can launch a local web server to control the tool via a rich, dark-mode browser dashboard. This dashboard contains all CLI options, a real-time terminal log viewer, and a side-by-side markdown viewer to inspect and read results.

### Launch the Web UI
- **Using `uv` (without virtual environment)**:
  ```bash
  uv run app.py
  ```
- **Using standard Python (with active virtual environment)**:
  ```bash
  python app.py
  ```

Once started, open your browser and navigate to **`http://127.0.0.1:5000`**.

#### Running on a custom port
You can customize the host and port by passing CLI arguments. For example, to run the server on port `5001`:
- **Using `uv`**:
  ```bash
  uv run app.py --port 5001
  ```
- **Using standard Python**:
  ```bash
  python app.py --port 5001
  ```
Then navigate to **`http://127.0.0.1:5001`**.

### Dashboard Features
* **Folder and File Picker Explorer**: Select any custom directory or choose specific files on your host machine to process using the interactive modal file explorer.
* **Interactive File Scanner**: Specify an input folder or file path, configure format tags, and list target files instantly.
* **Granular Options**: Toggle parsing engines, target extensions, choose dynamic output directories, and toggle embedded image extraction flags.
* **Terminal Emulator Logs**: Streams standard stdout/stderr logs in real-time from the parsing execution thread using Server-Sent Events (SSE).
* **Parsed Documents Browser**: Access, open, and read any parsed output files from the sidebar outputs panel.
* **Formatted Reader View**: Render parsed documents in raw markdown, fully styled HTML, or a side-by-side split view with CDN-loaded `marked.js` markdown parser.

---

## 📄 Parsing Methods Overview

### 1. Docling (by IBM)
- **Description**: A local, open-source document parsing engine. It natively parses multiple document formats and builds structured representation trees.
- **Under the Hood**: Employs neural layout analysis and ONNX-based RapidOCR engines.
- **Best For**: Native, layout-aware structure extraction (headers, lists, tables) from PDFs and Microsoft Office files (`.docx`, `.xlsx`, `.pptx`).

### 2. LiteParse (by LlamaIndex)
- **Description**: A local, lightweight document parser. It focuses on spatial layout text parsing (preserves reading orders and bounding box coordinates).
- **Under the Hood**: Uses local text extraction and OCR (RapidOCR/Tesseract).
- **Best For**: Fast, real-time, privacy-first local extraction where spatial positioning of text on the page is needed.

### 3. Marker (by Vik Paruchuri)
- **Description**: A local, deep-learning based pipeline designed to convert PDFs into highly clean Markdown.
- **Under the Hood**: Orchestrates Surya layout/detector and Texify math models using PyTorch.
- **Best For**: High-fidelity formatting, tables, and excellent translation of mathematical equations/formulas.
- **System Requirements**: Requires ~3GB RAM/VRAM; runs slower on CPU but performs very well on GPU/Apple Silicon.

### 📋 Supported Formats Matrix

Different parsers support different native or converted formats. Below is a breakdown of what formats can be parsed by each engine:

| Format / Extension | Docling (IBM) | LiteParse (LlamaIndex) | Marker (Vik Paruchuri) |
|---|:---:|:---:|:---:|
| **PDF** (`.pdf`) | ✅ Native (OCR) | ✅ Native (OCR) | ✅ Native (Deep Learning OCR) |
| **Word** (`.docx`, `.doc`) | ✅ Native (`.docx`) | ✅ Auto-converted | ✅ Native (`.docx`) |
| **PowerPoint** (`.pptx`, `.ppt`) | ✅ Native (`.pptx`) | ✅ Auto-converted | ✅ Native (`.pptx`) |
| **Excel** (`.xlsx`, `.xls`) | ✅ Native (`.xlsx`) | ✅ Auto-converted | ✅ Native (`.xlsx`) |
| **E-books** (`.epub`) | ✅ Native | ❌ Not Supported | ✅ Native |
| **Images** (`.png`, `.jpg`, `.jpeg`, `.webp`, `.tiff`, `.bmp`) | ✅ Native | ✅ Native (via Tesseract/RapidOCR) | ✅ Native |
| **Web / Markup** (`.html`, `.xml`, `.latex`, `.md`, `.asciidoc`) | ✅ Native | ❌ Not Supported | ✅ Native (`.html`) |
| **Plain Text** (`.txt`) | ✅ Native | ❌ Not Supported | ❌ Not Supported |
| **Data / CSV** (`.csv`, `.tsv`) | ✅ Native | ✅ Auto-converted | ❌ Not Supported |

*Note: LiteParse auto-conversion for Office and spreadsheets requires LibreOffice/ImageMagick to be installed on the system (which converts files to temporary PDFs prior to parsing).*

---

## 🚀 Commands and Usage

Execute the parser script `parse_pdfs.py` using your terminal. 

> [!TIP]
> If running **without a virtual environment**, prefix the commands with `uv run` (e.g. `uv run parse_pdfs.py --methods docling`). If running **inside an activated virtual environment**, run with `python` (e.g. `python parse_pdfs.py --methods docling`).

### 1. Run all parsers on default files
If no custom input directory is specified, the script checks `RAG_data/` for PDF files.
```bash
uv run parse_pdfs.py
# OR
python parse_pdfs.py
```

### 2. Choose specific parser methods
You can use the `--methods` flag to select one or multiple parsers to run (space-separated list). Options: `docling`, `liteparse`, `marker`.
- **Run only Docling**:
  ```bash
  uv run parse_pdfs.py --methods docling
  ```
- **Run Docling and Marker**:
  ```bash
  uv run parse_pdfs.py --methods docling marker
  ```

### 3. Choose custom file types (e.g. docx, pptx)
By default, the script processes `.pdf` files. You can choose to parse other document types (such as `docx`, `pptx`, `xlsx`, `png`, `jpg`, `epub`, `html`, etc.) using the `--file_types` argument:
- **Parse only docx files**:
  ```bash
  uv run parse_pdfs.py --file_types docx --methods docling
  ```
- **Parse docx and pptx files together**:
  ```bash
  uv run parse_pdfs.py --file_types docx pptx --methods docling
  ```

### 4. Enable or disable embedded image extraction/processing
If you want to extract and process pictures/images embedded within the documents (e.g. saving embedded images as files, running OCR on page screenshots), pass the `--process_images` flag:
```bash
uv run parse_pdfs.py --process_images
```
*If not passed, image extraction is disabled to save computation time and space (Marker will pass `--disable_image_extraction` and Docling will set picture extraction flags to `False`).*

### 5. Parse files from a custom directory
To scan a specific folder containing your files, pass it via `--pdf_dir`:
```bash
uv run parse_pdfs.py --pdf_dir /path/to/your/files/ --file_types pdf docx
```

### 6. Parse custom folder with selected methods
Combine arguments to process custom folders with specific tools:
```bash
uv run parse_pdfs.py --pdf_dir /Users/username/documents/ --methods docling liteparse --file_types docx
```

### 7. Download the benchmark PDF and run
Explicitly force downloading the *Attention Is All You Need* paper and parse it:
```bash
uv run parse_pdfs.py --download_benchmark
```

### 8. Change output directory
By default, outputs are saved in `RAG_data/parsed_outputs/<method_name>/`. Use `--output_dir` to change this location:
```bash
uv run parse_pdfs.py --pdf_dir RAG_data/ --output_dir custom_outputs/ --file_types pdf docx
```
