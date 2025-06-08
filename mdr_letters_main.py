# ─── Python Standard Library ────────────────────────────────────────────────

import logging

# ─── Local Application Imports ──────────────────────────────────────────────

from mdr_letters.config import LOG_FORMAT, LOG_DATE_FORMAT
from mdr_letters.document_processor import DocumentProcessor

# ─── Configure Logging Format and Level ─────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    datefmt=LOG_DATE_FORMAT
)

# ─── Script Entry Point ─────────────────────────────────────────────────────

def main() -> None:
    logging.info("Initializing MDR Letters Processing System")
    
    try:
        document_processor = DocumentProcessor()
        document_processor.execute_workflow()
        
    except Exception as application_error:
        logging.error("Application execution failed", exc_info=True)
        raise application_error

# ─── Execute Script ────────────────────────────────────────────────────────────

if __name__ == '__main__':
    main()