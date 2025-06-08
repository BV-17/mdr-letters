# Changelog

All notable changes to the MDR Letters Processing System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-08

### Added
- Initial release of modular MDR Letters Processing System
- Intelligent recipient detection based on postal code analysis
- Multi-destination document distribution system
- Automated PDF text extraction and analysis
- Comprehensive file organisation and chronological ordering
- PDF metadata management and updates
- Professional logging system with detailed audit trails
- Modular architecture with separation of concerns

### Features
- **DocumentProcessor**: Main workflow orchestration
- **RecipientDetector**: Postal code-based recipient identification
- **FileManager**: File operations and organisation utilities
- **PDFUtils**: PDF processing and metadata management
- **Configuration**: Centralised settings and constants

### Technical Improvements
- Full refactoring from monolithic script to modular architecture
- Enhanced error handling and logging throughout
- Type hints for improved code documentation
- Professional naming conventions and code structure
- Comprehensive documentation and README

### Postal Code Logic
- W6 0XE + HA0 2NJ + M20 6RE → All Defendants → Both directories
- W6 0XE + HA0 2NJ → Kambiz Babaee & Bhupen Varsani → Both directories
- W6 0XE only → Kambiz Babaee → Kambiz directory
- HA0 2NJ only → Bhupen Varsani → Bhupen directory
- M20 6RE only → Fortis Insolvency → Kambiz directory
- EC4A 1NL only → London Circuit Commercial Court → Kambiz directory
- EC2V 7HN → Lloyds Banking Group → Kambiz directory

## [Unreleased]

### Planned
- Unit test implementation
- Integration tests for workflow validation
- Performance optimisation for large document batches
- Configuration file support for flexible directory mapping
- Enhanced error recovery mechanisms
- Web interface for monitoring and control

---

**Repository**: BV-17/mdr_letters  
**Maintainer**: BV-17  
**Licence**: MIT