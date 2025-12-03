# Repository Analyzer Agent

**Version:** 1.0.0
**Status:** Phase 1 MVP - Sequential Processing

## Overview

Repository Analyzer Agent is an automated code grading tool for educational institutions that analyzes student GitHub repositories to assess code quality based on file structure and line count metrics.

### Key Features

- **Automated Repository Analysis**: Clone and analyze multiple GitHub repositories automatically
- **Code Metrics Calculation**: Count lines of code, number of files, and calculate grades
- **Excel Integration**: Read repository URLs from Excel (GmailAgent output) and generate graded results
- **Error Handling**: Gracefully handle repository errors (404, access denied, network issues)
- **Summary Statistics**: Generate detailed summary with grade distribution and statistics
- **Cross-platform**: Works on Windows, macOS, and Linux

### Grading Formula

```
Grade = (Files with <130 lines / Total files) × 100
```

This formula encourages students to break their code into small, focused files rather than monolithic files.

## Installation

### Prerequisites

- Python 3.8 or higher
- Git installed and accessible from command line
- Internet connection (to clone repositories)

### Install Dependencies

```bash
cd EmailSkillAgents
pip install -r requirements.txt
```

Required packages:
- `GitPython>=3.1.40` - Git repository cloning
- `openpyxl>=3.1.2` - Excel file operations
- `click>=8.1.7` - CLI framework
- `tqdm>=4.66.0` - Progress bars (future use)

## Usage

### Basic Usage

```bash
python -m repo_analyzer.cli analyze --input exports/homework_emails.xlsx
```

This will:
1. Read repository URLs from the Excel file
2. Clone each repository to a temporary directory
3. Calculate code metrics for each repository
4. Generate a graded Excel file in `output/` directory
5. Display summary statistics
6. Clean up temporary files

### Command Options

```bash
# Specify custom output path
python -m repo_analyzer.cli analyze --input hw.xlsx --output graded_hw.xlsx

# Enable verbose output
python -m repo_analyzer.cli analyze --input hw.xlsx --verbose

# Show help
python -m repo_analyzer.cli analyze --help
```

### Expected Input Format

The input Excel file should have these columns (from GmailAgent):
- **ID** - Unique identifier (optional)
- **Date** - Email date (optional)
- **Subject** - Email subject (optional)
- **URL** - GitHub repository URL (required)

Example:
```
| ID | Date              | Subject        | URL                                      |
|----|-------------------|----------------|------------------------------------------|
| 1  | 2025-11-20 10:30  | Homework 1     | https://github.com/student1/project      |
| 2  | 2025-11-20 11:15  | Assignment 2   | https://github.com/student2/assignment   |
```

### Output Format

The output Excel file contains two sheets:

#### Sheet 1: Graded Results

All original columns plus:
- **Grade** - Calculated grade (0-100%)
- **Total Files** - Number of code files found
- **Files <130** - Number of files with less than 130 lines
- **Total Lines** - Total lines of code
- **Status** - Success or error status
- **Error Message** - Error details if failed

#### Sheet 2: Summary

- Total repositories processed
- Successfully graded count
- Failed count
- Grade statistics (average, median, min, max, std dev)
- Grade distribution histogram
- Error report
- Processing time

## How It Works

### 1. Excel Input Processing

- Reads Excel file using openpyxl
- Validates required columns (at minimum: URL)
- Extracts repository URLs
- Filters out empty rows

### 2. Repository Cloning

- Creates temporary directory: `/tmp/repoanalyzer_YYYYMMDD_HHMMSS/`
- Clones repositories using shallow clone (depth=1) for speed
- Validates GitHub URL format
- Handles errors gracefully (404, access denied, network errors)

### 3. Metrics Calculation

**Code File Identification:**
- Includes: `.py`, `.java`, `.js`, `.ts`, `.jsx`, `.tsx`, `.cpp`, `.c`, `.h`, `.hpp`, `.go`, `.rs`, `.rb`, `.php`, `.swift`, `.kt`, `.cs`, `.scala`
- Excludes: Config files, documentation, binary files, dependencies

**Excluded Directories:**
- `node_modules`, `venv`, `.venv`, `env`, `.env`
- `__pycache__`, `.pytest_cache`, `.git`, `.svn`
- `build`, `dist`, `target`, `.idea`, `.vscode`
- `bower_components`, `vendor`, `bin`, `obj`

**Line Counting Rules:**
- Count non-empty lines (strip whitespace, skip if empty)
- Include comment lines (they're still code maintenance)
- Use UTF-8 encoding with fallback to latin-1
- Skip files that can't be read

**Grade Calculation:**
```python
if total_files == 0:
    grade = 0.00
else:
    grade = (files_under_130 / total_files) * 100
```

### 4. Output Generation

- Merges original data with analysis results
- Creates formatted Excel with color-coded status cells
- Generates summary statistics sheet
- Saves to `output/` directory

### 5. Cleanup

- Removes temporary directory
- Cleans up all cloned repositories
- Handles cleanup errors gracefully

## Example Output

```
Repository Analyzer v1.0.0
==================================================

Reading input: exports/homework_emails.xlsx
Found 4 repository URLs

Processing repositories...
Temporary directory: /tmp/repoanalyzer_20251123_172055

[1/4] Analyzing https://github.com/student1/project...
  Grade: 100.00%

[2/4] Analyzing https://github.com/student2/assignment...
  Grade: 75.00%

[3/4] Analyzing https://github.com/student3/homework...
  Error: Repository not found or deleted

[4/4] Analyzing https://github.com/student4/code...
  Grade: 85.00%

Writing output...

Summary
==================================================
Successfully Analyzed: 3/4
Failed: 1/4
Average Grade: 86.67%
Processing Time: 0m 45s

Output: output/homework_emails_graded.xlsx

Analysis complete!
```

## Error Handling

The tool handles various error scenarios gracefully:

| Error Type | Status | Behavior |
|-----------|--------|----------|
| Repository not found (404) | "Not Found" | Continue processing other repos |
| Private repository (403) | "Access Denied" | Continue processing other repos |
| Invalid URL format | "Invalid URL" | Continue processing other repos |
| Network connection failed | "Network Error" | Continue processing other repos |
| No code files found | "No Code Files" | Grade = 0.00, continue processing |
| Timeout (>5 min) | "Timeout" | Continue processing other repos |

## Limitations (Phase 1 MVP)

- **Sequential processing only**: Processes one repository at a time
- **Public repositories only**: No support for private repositories (requires authentication)
- **HTTPS URLs only**: SSH URLs not supported
- **Fixed line limit**: 130 lines threshold is hardcoded (not configurable)
- **No timeout enforcement**: Git clone timeout not enforced on Windows

## Future Enhancements (Planned)

### Phase 2: Performance (Multithreading)
- Parallel processing with 5-10 worker threads
- Thread-safe result collection
- 4-8x speedup for large batches
- Target: 30 repos in <25 minutes

### Phase 3: Features
- Support for private repositories (SSH keys, tokens)
- Configurable line limit threshold
- Custom grading formulas
- CSV input/output support
- Retry failed repositories

### Phase 4: Advanced Features
- Code quality metrics (cyclomatic complexity)
- Plagiarism detection (code similarity)
- Unit test coverage analysis
- GUI interface
- LMS integration (Canvas, Blackboard, Moodle)

## Troubleshooting

### Git not found
```
Error: GitPython requires Git to be installed
```
**Solution**: Install Git from https://git-scm.com/ and ensure it's in your PATH

### Excel file not found
```
Error: Excel file not found: exports/homework_emails.xlsx
```
**Solution**: Check the file path and ensure the file exists

### Invalid Excel format
```
Error: Missing required columns: URL
```
**Solution**: Ensure the Excel file has at least a "URL" column

### Clone fails
```
Error: Repository not found or deleted
```
**Solution**: Verify the repository URL is correct and the repository is public

### Cleanup warning
```
Warning: Could not clean up temporary directory: Access is denied
```
**Solution**: This is a Windows file locking issue. The directory will be cleaned up automatically later. You can manually delete it if needed.

## Development

### Project Structure

```
repo_analyzer/
├── __init__.py           # Package initialization
├── __main__.py          # Module entry point
├── cli.py               # Click-based CLI
├── analyzer.py          # Main orchestrator
├── excel_manager.py     # Excel I/O operations
├── repo_manager.py      # Git clone/cleanup
├── metrics_calculator.py # Code metrics calculation
├── config.py            # Configuration constants
├── errors.py            # Custom exceptions
└── README.md            # This file
```

### Testing

Run with verbose mode to see detailed output:
```bash
python -m repo_analyzer.cli analyze --input test_data.xlsx --verbose
```

### Configuration

Edit `config.py` to change:
- Code file extensions
- Excluded directories
- Line limit threshold
- Retry attempts
- Timeout values

## Credits

**Developer**: AI Development Course - Lesson 19
**Project**: Email Skill Agents
**PRD**: See `PRD-RepositoryAnalyzer.md` for comprehensive product requirements

## License

Internal educational tool - Not for commercial use

## Support

For issues or questions, refer to the PRD or contact the development team.

---

**Version History**

- **1.0.0** (2025-11-23): Phase 1 MVP - Sequential processing
  - Basic Excel input/output
  - Repository cloning and metrics calculation
  - Grade calculation and summary statistics
  - Error handling
  - Cross-platform support
