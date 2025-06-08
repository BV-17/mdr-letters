# ─── Python Standard Library ────────────────────────────────────────────────

import re
import logging
from datetime import datetime
from typing import Tuple, List

# ─── Local Application Imports ──────────────────────────────────────────────

from .config import (
    KAMBIZ_DIRECTORY,
    BHUPEN_DIRECTORY,
    DATE_PATTERN,
    POSTAL_CODES
)

# ─── Recipient Detection and Date Extraction ────────────────────────────────

class RecipientDetector:

    # ─── Initialize Recipient Detector ────────────────────────────────────────

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    # ─── Determine Recipients & Destinations ─────────────────────────────────

    def determine_recipients_and_destinations(self, document_text: str) -> Tuple[str, List[str]]:

        # ─── Check for Multiple Postal Code Combinations ─────────────────────

        contains_w6_0xe = POSTAL_CODES["W6_0XE"] in document_text
        contains_ha0_2nj = POSTAL_CODES["HA0_2NJ"] in document_text
        contains_m20_6re = POSTAL_CODES["M20_6RE"] in document_text
        contains_ec4a_1nl = POSTAL_CODES["EC4A_1NL"] in document_text
        contains_ec2v_7hn = POSTAL_CODES["EC2V_7HN"] in document_text

        # ─── Evaluate Postal Code Combinations ───────────────────────────────

        if contains_w6_0xe and contains_ha0_2nj and contains_m20_6re:
            return 'All Defendants', [BHUPEN_DIRECTORY, KAMBIZ_DIRECTORY]
        
        if contains_w6_0xe and contains_ha0_2nj:
            return 'Kambiz Babaee & Bhupen Varsani', [BHUPEN_DIRECTORY, KAMBIZ_DIRECTORY]
        
        if contains_w6_0xe:
            return 'Kambiz Babaee', [KAMBIZ_DIRECTORY]
        
        if contains_ha0_2nj:
            return 'Bhupen Varsani', [BHUPEN_DIRECTORY]
        
        if contains_m20_6re:
            return 'Fortis Insolvency', [KAMBIZ_DIRECTORY]
        
        if contains_ec4a_1nl:
            return 'London Circuit Commercial Court', [KAMBIZ_DIRECTORY]
        
        if contains_ec2v_7hn:
            return 'Lloyds Banking Group', [KAMBIZ_DIRECTORY]
        
        # ─── Default Case ─────────────────────────────────────────────────────

        return 'Kambiz Babaee', [KAMBIZ_DIRECTORY]

    # ─── Extract & Format Date from Text ─────────────────────────────────────

    def extract_and_format_date(self, document_text: str) -> Tuple[str, str]:
        date_match = DATE_PATTERN.search(document_text)
        if date_match:
            try:
                parsed_date = datetime.strptime(date_match.group(1), "%d %B %Y")
                return parsed_date.strftime('%d %B %Y'), parsed_date.strftime('%Y')
            except ValueError:
                self.logger.warning("Invalid date format in text: %s", date_match.group(1))
        return "Unknown Date", "Unknown"

    # ─── Analyze Document Content ─────────────────────────────────────────────

    def analyze_document(self, document_text: str) -> Tuple[str, List[str], str, str]:
        recipient_name, destination_directories = self.determine_recipients_and_destinations(document_text)
        formatted_date, year = self.extract_and_format_date(document_text)
        
        self.logger.info("Document analysis complete - Recipient: %s, Date: %s", recipient_name, formatted_date)
        
        return recipient_name, destination_directories, formatted_date, year