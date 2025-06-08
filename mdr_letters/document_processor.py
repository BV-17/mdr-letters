# ─── Python Standard Library ────────────────────────────────────────────────

import os
import sys
import shutil
import logging
from typing import List

# ─── Local Application Imports ──────────────────────────────────────────────

from .config import INPUT_DIRECTORY, OUTPUT_DIRECTORIES
from .pdf_utils import PDFUtils
from .recipient_detector import RecipientDetector
from .file_manager import FileManager

# ─── Main Document Processing Engine ─────────────────────────────────────────

class DocumentProcessor:

    # ─── Initialize Document Processor ────────────────────────────────────────

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.pdf_utils = PDFUtils()
        self.recipient_detector = RecipientDetector()
        self.file_manager = FileManager()

    # ─── Rename & Distribute PDF ─────────────────────────────────────────────

    def rename_and_distribute(
        self,
        original_pdf_path: str,
        recipient_name: str,
        formatted_date: str,
        year: str,
        destination_directories: List[str]
    ) -> None:
        
        _, file_extension = os.path.splitext(original_pdf_path)
        new_filename = f"Mishcon de Reya — Letter to {recipient_name} [{formatted_date}]{file_extension}"
        source_file_path = None

        for directory_index, destination_root_directory in enumerate(destination_directories):
            target_year_folder = os.path.join(destination_root_directory, year)
            os.makedirs(target_year_folder, exist_ok=True)
            target_file_path = os.path.join(target_year_folder, new_filename)

            try:
                if directory_index == 0:
                    shutil.move(original_pdf_path, target_file_path)
                    source_file_path = target_file_path
                    self.logger.info("Moved PDF to: %s", target_file_path)

                else:
                    shutil.copy2(source_file_path, target_file_path)
                    self.logger.info("Copied PDF to: %s", target_file_path)

            except Exception:
                self.logger.error("Failed to distribute PDF to %s", destination_root_directory, exc_info=True)

    # ─── Process Input PDFs ──────────────────────────────────────────────────

    def process_input_pdfs(self) -> None:
        for filename in os.listdir(INPUT_DIRECTORY):

            if not filename.lower().endswith(".pdf"):
                continue
            
            pdf_file_path = os.path.join(INPUT_DIRECTORY, filename)
            self.logger.info("Processing input PDF: %s", pdf_file_path)

            document_text = self.pdf_utils.load_pdf_text(pdf_file_path)
            if not document_text:
                continue

            recipient_name, destination_directories, formatted_date, year = self.recipient_detector.analyze_document(document_text)
            self.rename_and_distribute(pdf_file_path, recipient_name, formatted_date, year, destination_directories)

    # ─── Process Existing File Organization ───────────────────────────────────

    def process_existing_files(self) -> bool:
        for output_directory in OUTPUT_DIRECTORIES:
            if (self.file_manager.validate_dates_in_filenames(output_directory) and 
                self.file_manager.ensure_all_files_closed(output_directory)):
                self.file_manager.process_directory_with_subfolders(output_directory)
            else:
                self.logger.error("Validation failed for directory: %s", output_directory)
                return False
        return True

    # ─── Update PDF Metadata for All Files ───────────────────────────────────

    def update_all_pdf_metadata(self) -> None:
        for output_directory in OUTPUT_DIRECTORIES:
            self.pdf_utils.update_pdf_metadata(output_directory)

    # ─── Execute Complete Processing Workflow ────────────────────────────────

    def execute_workflow(self) -> None:
        self.logger.info("Starting PDF processing workflow")

        # ─── Process Input PDFs ───────────────────────────────────────────────

        self.process_input_pdfs()

        # ─── Validate & Organize Existing PDFs ────────────────────────────────

        if not self.process_existing_files():
            self.logger.error("Existing file processing failed")
            sys.exit(1)

        # ─── Update PDF Metadata ──────────────────────────────────────────────

        self.update_all_pdf_metadata()
        
        self.logger.info("PDF processing workflow completed successfully")