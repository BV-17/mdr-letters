# MDR Letters Processing System

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/licence-MIT-green.svg)
![Status](https://img.shields.io/badge/status-production-brightgreen.svg)

> Automated legal document processing and distribution system for Mishcon de Reya correspondence

## Overview

The MDR Letters Processing System is a sophisticated Python application designed to automate the processing, categorisation, and distribution of legal correspondence from Mishcon de Reya solicitors. The system intelligently analyses PDF documents, extracts relevant information, and distributes files to appropriate directories based on recipient postal codes and case requirements.

## Features

- **Intelligent Recipient Detection** - Automatically identifies recipients based on postal code analysis
- **Multi-Destination Distribution** - Distributes documents to appropriate case directories
- **Date Extraction & Formatting** - Extracts and standardises dates from document content
- **Metadata Management** - Updates PDF metadata for enhanced organisation
- **File Organisation** - Chronological ordering and systematic file naming conventions
- **Comprehensive Logging** - Detailed logging for audit trails and troubleshooting
- **Modular Architecture** - Clean, maintainable codebase with separation of concerns

## Prerequisites

- **Python 3.11** or higher
- **pip** package manager
- Access to shared legal drives (G:\ mapped network drive)
- PyMuPDF library for PDF processing

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd mdr_letters
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Quick Start

1. **Ensure network drives are accessible:**
   - Verify G:\ drive mapping to shared legal directories
   - Check read/write permissions on target directories

2. **Place PDF files in input directory:**
   - Default location: `C:\Users\Bhupen Varsani\Downloads\PDF`

3. **Execute the application:**
   ```bash
   python mdr_letters_main.py
   ```

## Configuration

### Directory Structure

The application expects the following directory structure:

```
G:\Shared drives\Legal\One Unique LLC -v- Kambiz Babaee\
├── Kambiz Babaee\Civil\Mishcon de Reya\
│   └── [Year folders with processed documents]
└── Bhupen Varsani\Civil\Mishcon de Reya\
    └── [Year folders with processed documents]
```

### Postal Code Mapping

The system uses the following postal code logic for recipient determination:

| Postal Code Combination | Recipient | Destination |
|-------------------------|-----------|-------------|
| W6 0XE + HA0 2NJ + M20 6RE | All Defendants | Both directories |
| W6 0XE + HA0 2NJ | Kambiz Babaee & Bhupen Varsani | Both directories |
| W6 0XE only | Kambiz Babaee | Kambiz directory |
| HA0 2NJ only | Bhupen Varsani | Bhupen directory |
| M20 6RE only | Fortis Insolvency | Kambiz directory |
| EC4A 1NL only | London Circuit Commercial Court | Kambiz directory |
| EC2V 7HN only | Lloyds Banking Group | Kambiz directory |

## Project Structure

```
mdr_letters/
│
├── 📁 mdr_letters/           # Main package directory
│   ├── __init__.py           # Package initialisation
│   ├── config.py             # Configuration constants
│   ├── document_processor.py # Main processing engine
│   ├── file_manager.py       # File operations utilities
│   ├── pdf_utils.py          # PDF processing utilities
│   └── recipient_detector.py # Recipient detection logic
│
├── 📁 data/                  # Application data
├── 📁 logs/                  # Application logs  
├── 📁 tests/                 # Unit tests
│
├── 📄 README.md              # Project documentation
├── 📄 LICENSE                # MIT licence
├── 📄 CHANGELOG.md           # Version history
├── 📄 requirements.txt       # Python dependencies
├── 📄 .gitignore             # Git ignore rules
└── 📄 mdr_letters_main.py    # Main application entry point
```

## Usage

### Basic Operation

The application operates in three main phases:

1. **Document Processing**: Analyses PDF files in the input directory
2. **File Organisation**: Organises existing files chronologically
3. **Metadata Updates**: Updates PDF metadata for consistency

### Command Line Execution

```bash
# Basic execution
python mdr_letters_main.py

# With virtual environment activated
./venv/Scripts/python mdr_letters_main.py  # Windows
./venv/bin/python mdr_letters_main.py      # macOS/Linux
```

### Logging

The application provides comprehensive logging with timestamps:

```
DD Month YYYY | HH:MM:SS:mmm | INFO: Processing input PDF: filename.pdf
DD Month YYYY | HH:MM:SS:mmm | INFO: Document analysis complete - Recipient: Name, Date: DD Month YYYY
DD Month YYYY | HH:MM:SS:mmm | INFO: Moved PDF to: destination/path/filename.pdf
```

## Module Documentation

### DocumentProcessor

The main processing engine that orchestrates the entire workflow:
- Coordinates PDF processing and distribution
- Manages file organisation and metadata updates
- Handles error recovery and logging

### RecipientDetector

Intelligent analysis module for document categorisation:
- Postal code pattern recognition
- Date extraction from document content
- Recipient determination logic

### FileManager

Comprehensive file operations management:
- Temporary file handling and cleanup
- Sequential file organisation
- Duplicate filename resolution

### PDFUtils

Specialised PDF processing utilities:
- Text extraction from PDF documents
- Metadata manipulation and updates
- File integrity validation

## Development

### Code Standards

This project follows professional Python development standards:
- **PEP 8** compliance for code formatting
- **Type hints** for improved code documentation
- **Comprehensive logging** for debugging and audit trails
- **Modular architecture** for maintainability

### Testing

Future implementations will include:
- Unit tests for individual modules
- Integration tests for workflow validation
- Performance testing for large document batches

## Troubleshooting

### Common Issues

**File Access Errors:**
- Verify network drive mapping (G:\ drive)
- Check file permissions on shared directories
- Ensure no files are open in other applications

**PDF Processing Errors:**
- Verify PyMuPDF installation: `pip install PyMuPDF`
- Check PDF file integrity
- Ensure sufficient disk space for temporary files

**Date Extraction Issues:**
- Documents must contain dates in format: "DD Month YYYY"
- Verify date appears in square brackets in filenames

## Licence

This project is licenced under the MIT Licence - see the [LICENSE](LICENSE) file for details.

---

**© 2025 BV-17 | Professional Legal Document Processing System**