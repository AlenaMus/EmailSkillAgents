# Changelog

All notable changes to the Email Skill Agents project.

---

## [2.1.0] - 2025-12-02

### ✨ Added
- **Date Filtering Support** - Flexible date filtering options:
  - `--after DATE` - Filter emails after specific date (YYYY-MM-DD)
  - `--before DATE` - Filter emails before specific date (YYYY-MM-DD)
  - `--newer-than PERIOD` - Filter recent emails (e.g., 7d, 2m, 1y)
  - `--older-than PERIOD` - Filter old emails (e.g., 30d, 6m)
- **Flexible Filter Combinations** - Use any combination of label, subject, and date filters
- **Enhanced Orchestrator Prompts** - Interactive prompts now include date filter options
- **Comprehensive Documentation** - New `DATE_FILTERING_GUIDE.md` with examples and use cases

### 📝 Changed
- Updated `gmailagent/cli.py` to accept date filter parameters
- Updated `gmailagent/gmail_client.py` to build queries with date filters
- Updated `orchestrator.py` to prompt for and pass date filters
- Enhanced Option 1 and Option 5 with date filtering inputs

### 📖 Documentation
- Added `docs/DATE_FILTERING_GUIDE.md`
- Updated `FINAL_STATUS.md` to version 2.1.0
- Updated `QUICK_STATUS.md` with date filtering info

---

## [2.0.1] - 2025-12-02

### 🐛 Fixed
- **Unicode Encoding Error** - Removed Unicode arrow (→) from orchestrator docstring
- **No Emails Detection** - Added proper detection when gmailagent finds no matching emails
- **Python Cache** - Cleaned all bytecode cache files to prevent stale code execution

### ✅ Verified
- All 7/7 tests passing
- Menu displays correctly without encoding errors
- Proper error messages when no emails match filters

### 📖 Documentation
- Added `docs/LATEST_FIXES.md`
- Added `QUICK_STATUS.md`
- Updated `FINAL_STATUS.md` to version 2.0.1
- Created `tests/test_no_emails_fix.py`

---

## [2.0.0] - 2024-12-02

### ✨ Added
- **Status Column Coordination** - All agents use Status = "ready" for sequencing
- **Interactive Menu System** - Orchestrator with 7 menu options
- **Folder Organization** - Professional folder structure with instructions/ directories
- **Comprehensive Testing** - Test suite with 5/5 tests passing

### 🐛 Fixed
- **Option 5 Issues** - Created `gmailagent/__main__.py` for module execution
- **Unicode Symbols** - Replaced with ASCII equivalents in gmailagent
- **Command Format** - Fixed orchestrator to use `python -m gmailagent`

### 📁 Organized
- Moved 40+ documentation files to organized folders
- Created `instructions/` folders for each agent
- Created `tests/` folder for test scripts
- Created `docs/` folder for general documentation

### 📖 Documentation
- `README.md` - Complete project overview
- `FINAL_STATUS.md` - Comprehensive status report
- `OPTION_5_FIX.md` - Detailed fix information
- `RUN_ORCHESTRATOR.md` - How to run guide
- `FOLDER_STRUCTURE.md` - Complete folder tree

---

## [1.0.0] - Initial Release

### Features
- **Agent 1: GmailAgent** - Export emails from Gmail to Excel
- **Agent 2: Repository Analyzer** - Analyze Git repositories and grade assignments
- **Agent 3: Greetings Agent** - Add personalized greetings based on grades
- **Agent 4: Evaluation Sender** - Create HTML email drafts and send

### Capabilities
- Gmail API integration with OAuth 2.0
- URL extraction from email bodies
- Repository cloning and analysis
- Persona-based greeting generation
- HTML email template generation
- Excel file processing with openpyxl

---

## Legend

- ✨ Added - New features
- 📝 Changed - Changes to existing functionality
- 🐛 Fixed - Bug fixes
- ✅ Verified - Tested and verified
- 📖 Documentation - Documentation updates
- 📁 Organized - File organization changes
- ⚠️ Deprecated - Features marked for removal
- 🗑️ Removed - Removed features

---

**Current Version:** 2.1.0
**Status:** Production Ready ✅
**Last Updated:** December 2, 2025
