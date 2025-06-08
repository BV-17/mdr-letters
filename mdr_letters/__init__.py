# ─── MDR Letters Package ─────────────────────────────────────────────────────

__version__ = "1.0.0"
__author__ = "BV-17"
__description__ = "Automated legal document processing and distribution system for Mishcon de Reya letters"

# ─── Package Exports ─────────────────────────────────────────────────────────

from .config import (
    INPUT_DIRECTORY,
    KAMBIZ_DIRECTORY, 
    BHUPEN_DIRECTORY,
    OUTPUT_DIRECTORIES
)

from .document_processor import DocumentProcessor
from .file_manager import FileManager
from .pdf_utils import PDFUtils
from .recipient_detector import RecipientDetector

__all__ = [
    "DocumentProcessor",
    "FileManager", 
    "PDFUtils",
    "RecipientDetector",
    "INPUT_DIRECTORY",
    "KAMBIZ_DIRECTORY",
    "BHUPEN_DIRECTORY", 
    "OUTPUT_DIRECTORIES"
]