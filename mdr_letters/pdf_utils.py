# ─── Python Standard Library ────────────────────────────────────────────────

import os
import logging
from typing import Optional

# ─── Third-Party Libraries ──────────────────────────────────────────────────

import fitz

# ─── Local Application Imports ──────────────────────────────────────────────

from .config import METADATA_UPDATES, TEMP_FILE_PREFIX

# ─── PDF Processing and Metadata Management ─────────────────────────────────

class PDFUtils:

    # ─── Initialize PDF Utilities ─────────────────────────────────────────────

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    # ─── File Lock Check ──────────────────────────────────────────────────────

    def is_file_locked(self, file_path: str) -> bool:
        try:
            with open(file_path, 'r+'):
                return False
        except IOError:
            return True

    # ─── Load PDF Text Content ────────────────────────────────────────────────

    def load_pdf_text(self, pdf_file_path: str) -> str:
        try:
            pdf_document = fitz.open(pdf_file_path)
            extracted_text = "".join(page.get_text() for page in pdf_document)
            pdf_document.close()
            self.logger.info("Extracted text from PDF: %s", pdf_file_path)
            return extracted_text
        
        except Exception:
            self.logger.error("Failed to read PDF: %s", pdf_file_path, exc_info=True)
            return ""

    # ─── Update PDF Metadata ──────────────────────────────────────────────────

    def update_pdf_metadata(self, root_directory: str) -> None:
        for directory_path, _, filenames in os.walk(root_directory):
            for filename in filenames:
                if filename.lower().endswith(".pdf"):
                    pdf_file_path = os.path.join(directory_path, filename)

                    if self.is_file_locked(pdf_file_path):
                        self.logger.warning("Skipping locked PDF for metadata: %s", pdf_file_path)
                        continue

                    try:
                        pdf_document = fitz.open(pdf_file_path)
                        metadata = pdf_document.metadata
                        metadata.update(METADATA_UPDATES)
                        pdf_document.set_metadata(metadata)
                        temp_file_path = pdf_file_path + ".temp"
                        pdf_document.save(temp_file_path, garbage=4, deflate=True)
                        pdf_document.close()
                        os.replace(temp_file_path, pdf_file_path)
                        self.logger.info("Metadata updated: %s", pdf_file_path)

                    except Exception:
                        self.logger.error("Metadata update failed: %s", pdf_file_path, exc_info=True)

    # ─── Extract PDF Information for Processing ───────────────────────────────

    def extract_pdf_info(self, pdf_file_path: str) -> Optional[str]:
        if not os.path.exists(pdf_file_path):
            self.logger.error("PDF file not found: %s", pdf_file_path)
            return None

        if not pdf_file_path.lower().endswith('.pdf'):
            self.logger.error("File is not a PDF: %s", pdf_file_path)
            return None

        return self.load_pdf_text(pdf_file_path)