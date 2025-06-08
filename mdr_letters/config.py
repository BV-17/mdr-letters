# ─── Python Standard Library ────────────────────────────────────────────────

import re
from pathlib import Path

# ─── Configuration & Constants ───────────────────────────────────────────────

INPUT_DIRECTORY = r"C:\Users\Bhupen Varsani\Downloads\PDF"
KAMBIZ_DIRECTORY = r"G:\Shared drives\Legal\One Unique LLC -v- Kambiz Babaee\Kambiz Babaee\Civil\Mishcon de Reya"
BHUPEN_DIRECTORY = r"G:\Shared drives\Legal\One Unique LLC -v- Kambiz Babaee\Bhupen Varsani\Civil\Mishcon de Reya"
OUTPUT_DIRECTORIES = [BHUPEN_DIRECTORY, KAMBIZ_DIRECTORY]

# ─── Regular Expression Patterns ─────────────────────────────────────────────

DATE_PATTERN = re.compile(r'\b(\d{1,2} [A-Za-z]+ \d{4})\b')

# ─── PDF Metadata Configuration ──────────────────────────────────────────────

METADATA_UPDATES = {
    "title": "",
    "author": "",
    "subject": "",
    "keywords": "",
    "producer": "",
    "creator": ""
}

# ─── File Processing Constants ───────────────────────────────────────────────

SUPPORTED_FILE_EXTENSIONS = ['.pdf', '.docx', '.xlsx', '.gdoc']
TEMP_FILE_PREFIX = "temp_"

# ─── Postal Code Mapping ─────────────────────────────────────────────────────

POSTAL_CODES = {
    "W6_0XE": "W6 0XE",
    "HA0_2NJ": "HA0 2NJ", 
    "M20_6RE": "M20 6RE",
    "EC4A_1NL": "EC4A 1NL",
    "EC2V_7HN": "EC2V 7HN"
}

# ─── Application Logging Configuration ───────────────────────────────────────

LOG_FORMAT = '%(asctime)s:%(msecs)03d | %(levelname)s: %(message)s'
LOG_DATE_FORMAT = '%d %B %Y | %H:%M:%S'