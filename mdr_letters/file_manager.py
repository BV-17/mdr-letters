# ─── Python Standard Library ────────────────────────────────────────────────

import os
import re
import logging
from datetime import datetime
from typing import List, Tuple, Optional

# ─── Local Application Imports ──────────────────────────────────────────────

from .config import SUPPORTED_FILE_EXTENSIONS, TEMP_FILE_PREFIX

# ─── File Management and Organization Utilities ─────────────────────────────

class FileManager:

    # ─── Initialize File Manager ──────────────────────────────────────────────

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    # ─── Extract Date from Filename ───────────────────────────────────────────

    def extract_date_from_filename(self, filename: str) -> Optional[datetime]:
        try:
            date_string = filename[filename.find('[') + 1: filename.find(']')]
            return datetime.strptime(date_string, '%d %B %Y')
        except (ValueError, IndexError):
            return None

    # ─── Clean Filename Suffixes ─────────────────────────────────────────────

    def remove_google_suffix(self, filename: str) -> str:
        return re.sub(r' - Google (Docs|Sheets)(?=\.[^.]+$)', '', filename)

    def remove_leading_sequence(self, filename: str) -> str:
        return re.sub(r'^\d{2}\s+', '', filename)

    # ─── File Lock & Availability Checks ─────────────────────────────────────

    def is_file_locked(self, file_path: str) -> bool:
        try:
            with open(file_path, 'r+'):
                return False
        except IOError:
            return True

    def ensure_all_files_closed(self, directory: str) -> bool:
        for directory_path, _, filenames in os.walk(directory):
            for filename in filenames:
                if filename.lower().endswith(tuple(SUPPORTED_FILE_EXTENSIONS)):
                    full_file_path = os.path.join(directory_path, filename)
                    if self.is_file_locked(full_file_path):
                        self.logger.error("Locked file detected: %s", full_file_path)
                        return False
        return True

    # ─── Temporary File Cleanup ───────────────────────────────────────────────

    def clean_temp_files(self, directory: str) -> None:
        for filename in os.listdir(directory):
            if filename.startswith(TEMP_FILE_PREFIX):
                temp_file_path = os.path.join(directory, filename)
                try:
                    os.remove(temp_file_path)
                    self.logger.info("Removed temp file: %s", temp_file_path)
                except Exception:
                    self.logger.error("Failed to remove temp file: %s", temp_file_path, exc_info=True)

    # ─── Unique Filename Generation ───────────────────────────────────────────

    def ensure_unique_filename(self, file_path: str) -> str:
        base_name, file_extension = os.path.splitext(file_path)
        counter = 1
        new_file_path = file_path
        while os.path.exists(new_file_path):
            new_file_path = f"{base_name} ({counter}){file_extension}"
            counter += 1
        return new_file_path

    # ─── Temporary Rename & Number Removal ────────────────────────────────────

    def temp_rename_for_ordering(self, directory: str) -> None:
        for filename in os.listdir(directory):
            if filename.lower().endswith(".pdf") and not filename.startswith(TEMP_FILE_PREFIX):
                original_file_path = os.path.join(directory, filename)

                if self.is_file_locked(original_file_path):
                    self.logger.error("File locked during temp rename: %s", original_file_path)
                    continue

                cleaned_filename = self.remove_leading_sequence(self.remove_google_suffix(filename))
                temp_file_path = os.path.join(directory, f"{TEMP_FILE_PREFIX}{cleaned_filename}")
                unique_temp_path = self.ensure_unique_filename(temp_file_path)

                try:
                    os.rename(original_file_path, unique_temp_path)
                    self.logger.info("Temp renamed: %s -> %s", original_file_path, unique_temp_path)
                except Exception:
                    self.logger.error("Failed temp rename: %s", original_file_path, exc_info=True)

    # ─── Sequential Rename Based on Date ──────────────────────────────────────

    def rename_in_sequence(self, directory: str) -> None:
        filename_date_pairs: List[Tuple[str, datetime]] = []

        for filename in os.listdir(directory):
            if filename.startswith(TEMP_FILE_PREFIX):
                date_object = self.extract_date_from_filename(filename)
                if date_object:
                    filename_date_pairs.append((filename, date_object))

        filename_date_pairs.sort(key=lambda x: (x[1], x[0][5:]))

        for index, (temp_filename, _) in enumerate(filename_date_pairs, start=1):
            cleaned_name = temp_filename[5:]
            new_filename = f"{index:02d} {cleaned_name}"
            old_file_path = os.path.join(directory, temp_filename)
            new_file_path = os.path.join(directory, new_filename)
            try:
                os.rename(old_file_path, new_file_path)
                self.logger.info("Renamed for sequence: %s -> %s", old_file_path, new_file_path)
            except Exception:
                self.logger.error("Sequence rename failed: %s", old_file_path, exc_info=True)

    # ─── Process Single Folder ───────────────────────────────────────────────

    def process_folder(self, directory: str) -> None:
        self.clean_temp_files(directory)
        self.temp_rename_for_ordering(directory)
        self.rename_in_sequence(directory)
        self.logger.info("Folder processed: %s", directory)

    # ─── Recursive Directory Processing ──────────────────────────────────────

    def process_directory_with_subfolders(self, root_directory: str) -> None:
        for directory_path, _, filenames in os.walk(root_directory):
            if filenames:
                self.process_folder(directory_path)

    # ─── Validate Filename Dates ──────────────────────────────────────────────

    def validate_dates_in_filenames(self, root_directory: str) -> bool:
        is_valid = True
        for directory_path, _, filenames in os.walk(root_directory):
            for filename in filenames:
                if filename.lower().endswith(".pdf") and not filename.startswith(TEMP_FILE_PREFIX):
                    if self.extract_date_from_filename(filename) is None:
                        self.logger.error("Missing date in filename: %s in %s", filename, directory_path)
                        is_valid = False
        return is_valid