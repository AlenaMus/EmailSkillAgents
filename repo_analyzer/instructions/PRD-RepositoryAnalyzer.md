# REPOSITORY ANALYZER AGENT - PRD

**Version:** 2.0 (Product Strategy Review)
**Date:** 2025-11-23
**Status:** Ready for Development
**Product Owner:** Product Strategy Team

---

## Executive Summary

Repository Analyzer Agent is an automated code grading tool for educational institutions that analyzes student GitHub repositories to assess code quality based on file structure and line count metrics. It integrates with the existing GmailAgent workflow to process homework submissions at scale, reducing instructor grading time from 2.5-5 hours to under 30 minutes for a class of 30 students.

**Core Value**: Automate the tedious, repetitive task of checking basic code metrics (file count, line distribution) so instructors can focus on actual code review and student feedback.

---

## Problem Statement

### User Problem

**Who**: Course instructors teaching programming courses with 20-50 students per class

**What**: "I receive 30+ GitHub repository URLs via email for each homework assignment. I need to quickly assess whether students are following good code practices (breaking code into small, focused files vs. monolithic files). Currently, I must manually:
1. Clone each repository
2. Count total files
3. Count lines in each file
4. Calculate a basic grade based on file size distribution
5. Record results in a spreadsheet

This takes 5-10 minutes per repo = 2.5-5 hours per assignment."

**Why it matters**: Instructors spend hours on mechanical grading tasks instead of providing meaningful code feedback to students. This creates bottlenecks in feedback loops and reduces teaching effectiveness.

### Business Problem

- **Inefficiency**: 2.5-5 hours of manual work per homework assignment
- **Error-prone**: Manual counting leads to inconsistencies
- **Scalability**: Impossible to grade more than 50 students without TA support
- **Poor student experience**: Delayed feedback (often 1-2 weeks) reduces learning effectiveness

---

## Goals & Success Metrics

### Objectives

1. **Primary**: Reduce basic grading time by 90% (from 2.5-5 hours to <30 minutes for 30 repos)
2. **Secondary**: Achieve 98%+ accuracy in code metric calculation
3. **Tertiary**: Enable instructors to grade 50+ students without additional TA resources

### North Star Metric

**Time from homework submission to initial grade**: Reduce from 1-2 weeks to same day

### Success Metrics

| Metric | Baseline | Target | Timeline | Measurement |
|--------|----------|--------|----------|-------------|
| **Grading Time** (30 repos) | 2.5-5 hours | <30 min | Launch | Stopwatch timing |
| **Metric Accuracy** | N/A | 98%+ | Launch | Manual verification sample (10 repos) |
| **Instructor Satisfaction** | N/A | 4.5/5 | Week 4 | Post-use survey |
| **Adoption Rate** | 0 | 80% of instructors | Month 3 | Usage logs |
| **Error Rate** | N/A | <2% repos fail | Launch | Error logs |

### Key Performance Indicators (KPIs)

**Leading Indicators:**
- Setup completion rate (instructors who complete first grading session)
- Average repositories graded per session
- Time to first successful grading run

**Lagging Indicators:**
- Weekly active instructors
- Total repos graded
- Instructor retention (using tool for 3+ assignments)
- Net Promoter Score (NPS)

---

## Target Users

### Primary User Persona

**Professor Sarah Chen - Computer Science Instructor**

**Demographics:**
- Age: 35
- Role: Assistant Professor, Computer Science
- Institution: Mid-size university
- Class size: 30 students per section, 2 sections per semester
- Teaching: Introduction to Programming, Data Structures

**Goals:**
- Provide timely feedback to students (within 48 hours)
- Ensure students follow code organization best practices
- Scale grading without sacrificing quality
- Spend more time on meaningful code reviews vs. mechanical counting

**Pain Points:**
- Spends 5 hours every week grading homework structure
- Inconsistent grading (counts vary when manually checking)
- Delayed feedback frustrates students
- Can't grade more than 30 students per section without TA
- Existing automated tools are too complex or require code changes

**Technical Proficiency:**
- Comfortable with command line
- Uses Git/GitHub regularly
- Can run Python scripts
- Not a DevOps expert (needs simple setup)

**Current Workflow:**
1. Receives emails with GitHub URLs from students
2. Exports to Excel (using GmailAgent)
3. Manually clones each repository
4. Counts files and lines per file
5. Calculates grade based on rubric
6. Records grade in Excel
7. Uploads to LMS

**Quote:** "I just need to know if students are breaking their code into small files or writing everything in one massive file. The manual counting is killing me."

### Secondary Users

- Teaching Assistants (TAs) supporting large courses
- Bootcamp instructors with rapid turnaround needs
- Online course creators with hundreds of students

---

## Scope

### In Scope (v1.0 - MVP)

**Core Functionality:**
- Read Excel file from GmailAgent (ID, Date, Subject, URL columns)
- Clone GitHub repositories to temporary directory
- Calculate code metrics per repository:
  - Total lines of code (all code files)
  - Total files (code files only, exclude config/docs)
  - Files with <130 lines
- Calculate grade: `(files <130 lines / total files) * 100`
- Output enhanced Excel with original data + Grade column
- Summary statistics sheet (avg grade, min/max, distribution)
- Basic error handling (404, timeout, access denied)

**Technical:**
- Multithreaded processing (5-10 parallel workers)
- Thread-safe Excel updates
- CLI interface with progress bars
- Temporary directory cleanup
- Windows/macOS/Linux support

**File Type Support:**
- Python: `.py`
- JavaScript: `.js`, `.jsx`, `.ts`, `.tsx`
- Java: `.java`
- C/C++: `.c`, `.cpp`, `.h`, `.hpp`
- C#: `.cs`
- Go: `.go`
- Ruby: `.rb`
- Rust: `.rs`

**Exclusions** (don't count):
- Configuration files: `package.json`, `requirements.txt`, etc.
- Documentation: `.md`, `.txt`, `.rst`
- Build artifacts: `dist/`, `build/`, `node_modules/`
- Version control: `.git/`, `.gitignore`
- Binary files: images, PDFs, executables

### Out of Scope (Future Versions)

**v1.1** (Next 3 months):
- Custom grading formulas (configurable)
- Support for private repositories (SSH keys, tokens)
- CSV input/output support
- Date range filtering
- Retry failed repositories
- Detailed error reporting per repository

**v2.0** (Next 6 months):
- Code quality metrics (cyclomatic complexity, maintainability index)
- Plagiarism detection (code similarity)
- Unit test coverage analysis
- GUI interface for non-technical users
- LMS integration (Canvas, Blackboard, Moodle)
- Scheduled/automated grading runs

**v3.0** (Future):
- AI-powered code review suggestions
- Style guide compliance checking
- Performance analysis
- Security vulnerability scanning
- Distributed processing for large-scale deployments

### MVP Definition

**Minimum Viable Version** includes:
- Sequential processing (no multithreading) - must work first
- Process 10 repositories successfully
- Calculate metrics and grade accurately
- Output Excel with Grade column
- Handle one error type (repository not found)

**Success Criteria:**
- Processes 10 repos in <10 minutes (sequential)
- 100% metric accuracy (verified manually)
- Excel output opens correctly
- Zero crashes

---

## User Stories

### Epic 1: Excel Input Processing

**User Story 1.1: Read Excel from GmailAgent**
```
As an instructor
I want to load an Excel file exported from GmailAgent
So that I can automatically grade all repositories without manual data entry

Acceptance Criteria:
- Given an Excel file with columns [ID, Date, Subject, URL]
- When I run the analyzer with that file
- Then all repository URLs are extracted correctly
- And invalid/missing URLs are flagged with warnings
- And the row count matches the Excel file

Priority: CRITICAL
Effort: 3 points
```

**User Story 1.2: Validate Input Data**
```
As an instructor
I want the tool to validate the Excel structure before processing
So that I catch errors early and don't waste time on bad data

Acceptance Criteria:
- Given an Excel file
- When the tool validates it
- Then it checks for required columns (ID, URL at minimum)
- And warns if URL column is missing or empty
- And shows count of valid URLs found
- And prompts for confirmation before proceeding

Priority: HIGH
Effort: 2 points
```

### Epic 2: Repository Cloning

**User Story 2.1: Clone Public Repositories**
```
As an instructor
I want to automatically clone student repositories
So that I can analyze their code without manual Git operations

Acceptance Criteria:
- Given a GitHub repository URL
- When the tool clones it
- Then it creates a temporary directory with timestamp
- And clones to: /tmp/repoanalyzer_YYYYMMDD_HHMMSS/repo_name/
- And handles repository names with special characters
- And cleans up the temporary directory after analysis

Priority: CRITICAL
Effort: 5 points

Technical Notes:
- Use GitPython library
- Timeout: 5 minutes per clone
- Shallow clone (--depth=1) for speed
- Handle large repositories (>500MB) with warning
```

**User Story 2.2: Handle Repository Errors**
```
As an instructor
I want clear error messages for failed repository clones
So that I can understand what went wrong and take corrective action

Acceptance Criteria:
- Given a repository that doesn't exist (404)
- When the tool tries to clone it
- Then it logs the error: "Repository not found: [URL]"
- And continues processing other repositories
- And marks the row with error status in output Excel

Error Scenarios:
- 404 Not Found: "Repository not found or deleted"
- 403 Forbidden: "Private repository - access denied"
- Timeout: "Repository clone timed out (>5 min)"
- Network error: "Network connection failed - check internet"
- Invalid URL: "Invalid GitHub URL format"

Priority: HIGH
Effort: 3 points

Expected Behavior:
- Retry 3 times with exponential backoff (1s, 2s, 4s)
- After 3 failures, mark as error and continue
- Don't crash the entire grading run for one bad repo
```

### Epic 3: Code Metrics Calculation

**User Story 3.1: Count Lines of Code**
```
As an instructor
I want accurate line counts for all code files
So that I can assess code volume and complexity

Acceptance Criteria:
- Given a cloned repository
- When the tool counts lines
- Then it counts all non-empty, non-comment lines in code files
- And excludes blank lines and comment-only lines
- And supports multiple programming languages
- And excludes documentation and configuration files

Line Counting Rules:
- Exclude blank lines (whitespace only)
- Exclude pure comment lines (# comment, // comment, /* comment */)
- Include lines with code + inline comments
- Count each physical line (not logical statements)

Priority: CRITICAL
Effort: 5 points

Edge Cases:
- Multi-line strings: COUNT (they're code)
- Multi-line comments: EXCLUDE
- Files with no code (all comments): 0 lines
- Mixed tabs/spaces: Normalize to 1 count per line
```

**User Story 3.2: Identify File Types**
```
As an instructor
I want only code files counted (not config, docs, etc.)
So that metrics reflect actual student code

Acceptance Criteria:
- Given a repository with mixed file types
- When the tool analyzes it
- Then it identifies code files by extension
- And excludes configuration files (package.json, .gitignore, etc.)
- And excludes documentation (.md, .txt, README)
- And excludes build artifacts (dist/, node_modules/, __pycache__)
- And logs which files were counted vs. excluded

Included Extensions:
.py, .js, .jsx, .ts, .tsx, .java, .c, .cpp, .h, .hpp, .cs, .go, .rb, .rs, .php, .swift, .kt

Excluded Patterns:
- Directories: node_modules/, dist/, build/, .git/, __pycache__/, venv/
- Config: package.json, requirements.txt, .gitignore, .env, *.config.js
- Docs: *.md, *.txt, *.rst, README*, LICENSE*, CHANGELOG*
- Binary: *.pyc, *.class, *.exe, *.dll, *.so, *.jpg, *.png, *.pdf

Priority: CRITICAL
Effort: 3 points
```

**User Story 3.3: Calculate Grade**
```
As an instructor
I want an automated grade based on file size distribution
So that I can quickly identify students following best practices

Acceptance Criteria:
- Given code metrics (total files, files <130 lines)
- When the tool calculates grade
- Then it uses formula: (files <130 lines / total files) * 100
- And rounds to 2 decimal places
- And handles edge cases (0 files, all files >130 lines)

Formula: Grade = (files_under_130 / total_files) * 100

Examples:
- 4 files <130, 5 total files → 80.00%
- 10 files <130, 10 total files → 100.00%
- 0 files <130, 5 total files → 0.00%
- 0 files total → Grade = 0.00 (edge case)

Priority: CRITICAL
Effort: 2 points

Edge Cases:
- 0 total files: Grade = 0.00, Warning: "No code files found"
- All files > 130 lines: Grade = 0.00 (student wrote monolithic code)
- 1 file total <130 lines: Grade = 100.00 (perfect small project)
```

### Epic 4: Multithreaded Processing

**User Story 4.1: Parallel Repository Processing**
```
As an instructor
I want repositories processed in parallel
So that I can grade 30 students in <30 minutes instead of hours

Acceptance Criteria:
- Given 30 repository URLs
- When the tool processes them
- Then it uses 5-10 worker threads (configurable)
- And shows progress for all threads
- And completes in <25 minutes (vs. 2+ hours sequential)
- And produces identical results to sequential processing

Performance Targets:
- Sequential: ~2-3 min per repo = 60-90 min for 30 repos
- Parallel (5 workers): ~15-20 min for 30 repos (4-5x speedup)
- Parallel (10 workers): ~10-15 min for 30 repos (6-8x speedup)

Priority: HIGH
Effort: 8 points

Technical Requirements:
- Use concurrent.futures.ThreadPoolExecutor
- Thread-safe Excel updates (use lock or queue)
- Graceful handling of thread exceptions
- Progress bar showing: [15/30 repos processed] 50%
```

**User Story 4.2: Thread-Safe Excel Updates**
```
As an instructor
I want the output Excel to be consistent and correct
So that I can trust the grades even with multithreading

Acceptance Criteria:
- Given multiple threads writing results
- When they update the Excel file
- Then updates are serialized (no race conditions)
- And no data loss or corruption occurs
- And final Excel has exactly N rows for N input repos
- And row order matches input order

Priority: HIGH
Effort: 5 points

Technical Approach:
- Option A: Collect results in thread-safe queue, write at end
- Option B: Use threading.Lock for Excel writes
- Recommended: Option A (safer, simpler)
```

### Epic 5: Excel Output

**User Story 5.1: Generate Graded Excel**
```
As an instructor
I want an Excel file with original data plus grades
So that I can upload results to my LMS or share with students

Acceptance Criteria:
- Given processed repositories and original Excel
- When the tool generates output
- Then it creates new Excel with columns:
  - Original: ID, Date, Subject, URL
  - New: Grade (%), Total Files, Files <130, Total Lines, Status, Error Message
- And preserves original row order
- And saves to: output/[original_name]_graded.xlsx
- And displays file location to user

Example Output:
| ID | Date | Subject | URL | Grade | Total Files | Files <130 | Total Lines | Status | Error |
|----|------|---------|-----|-------|-------------|-----------|-------------|--------|-------|
| 1  | 2025-11-20 | HW1 | github.com/student1/hw1 | 80.00 | 5 | 4 | 469 | Success | - |
| 2  | 2025-11-20 | HW1 | github.com/student2/hw1 | 0.00 | 0 | 0 | 0 | Error | Repository not found |

Priority: CRITICAL
Effort: 5 points
```

**User Story 5.2: Generate Summary Sheet**
```
As an instructor
I want a summary of grading results
So that I can understand class performance at a glance

Acceptance Criteria:
- Given all graded repositories
- When the tool generates output
- Then it creates a second sheet "Summary" with:
  - Total repositories: 30
  - Successfully graded: 28
  - Errors: 2
  - Average grade: 72.5%
  - Median grade: 75.0%
  - Min grade: 0.0%
  - Max grade: 100.0%
  - Grade distribution histogram (0-20%, 20-40%, 40-60%, 60-80%, 80-100%)

Priority: MEDIUM
Effort: 3 points
```

### Epic 6: Error Handling & Reliability

**User Story 6.1: Graceful Error Recovery**
```
As an instructor
I want the tool to handle errors without crashing
So that I can grade all repositories even if some fail

Acceptance Criteria:
- Given a mix of valid and invalid repositories
- When errors occur during processing
- Then the tool logs the error
- And continues processing remaining repositories
- And produces partial results for successful repos
- And lists all errors in summary report

Error Types:
1. Input errors: File not found, invalid Excel format
2. Repository errors: 404, timeout, access denied, empty repo
3. Processing errors: No code files, unsupported language
4. Output errors: Disk full, permission denied

Expected Behavior:
- Continue processing on repo-level errors
- Stop and report on critical errors (disk full, invalid input)
- Retry transient errors (network timeout) 3x

Priority: HIGH
Effort: 5 points
```

### Epic 7: User Experience

**User Story 7.1: Progress Tracking**
```
As an instructor
I want to see real-time progress while grading
So that I know the tool is working and how long to wait

Acceptance Criteria:
- Given a grading session in progress
- When I watch the console output
- Then I see:
  - "Processing 30 repositories with 5 workers..."
  - Progress bar: [████████------] 15/30 (50%) - ETA: 12 min
  - Per-repo status: "✓ student1/hw1 (Grade: 80.00%)"
  - Errors: "✗ student2/hw1 (Error: Repository not found)"
  - Final summary: "Completed: 28/30 in 18 minutes"

Priority: MEDIUM
Effort: 3 points
```

---

## Functional Requirements

### FR-1: Excel Input Processing

**Description:** Read and validate Excel file from GmailAgent

**Inputs:**
- Excel file path (required)
- Expected columns: ID, Date, Subject, URL (minimum: URL)

**Processing:**
1. Validate file exists and is readable
2. Check for .xlsx extension
3. Open with openpyxl
4. Validate required columns present
5. Extract URL column
6. Filter rows with non-empty URLs
7. Display validation summary

**Outputs:**
- List of repository URLs
- Validation warnings/errors
- Count of valid URLs found

**Error Handling:**
- File not found: Exit with error message
- Invalid format: "Not a valid Excel file"
- Missing URL column: "Excel missing required URL column"
- No valid URLs: "No repository URLs found in Excel"

**Acceptance Criteria:**
- Successfully reads Excel from GmailAgent
- Handles missing/malformed URLs gracefully
- Validates before expensive operations (cloning)

### FR-2: Repository Cloning

**Description:** Clone GitHub repositories to temporary directory

**Inputs:**
- Repository URL (GitHub HTTPS format)
- Temporary directory path

**Processing:**
1. Create temp directory: `/tmp/repoanalyzer_{timestamp}/`
2. Extract repo name from URL
3. Clone with GitPython (shallow clone, depth=1)
4. Set timeout: 5 minutes
5. Retry 3x on failure with backoff (1s, 2s, 4s)
6. Store clone path for analysis

**Outputs:**
- Local repository path
- Clone status (success/error)
- Error message (if failed)

**Performance:**
- Timeout: 5 minutes per clone
- Retry: 3 attempts
- Shallow clone for speed

**Error Handling:**
| Error | Retry? | Message |
|-------|--------|---------|
| 404 Not Found | No | "Repository not found or deleted" |
| 403 Forbidden | No | "Private repository - access denied" |
| Timeout | Yes (3x) | "Clone timeout (>5 min)" |
| Network error | Yes (3x) | "Network connection failed" |
| Invalid URL | No | "Invalid GitHub URL format" |

**Acceptance Criteria:**
- Clones public repositories successfully
- Handles errors without crashing
- Cleans up temp directory after processing
- Works on Windows/macOS/Linux

### FR-3: Code Metrics Calculation

**Description:** Calculate lines of code, file counts, and grade

**Inputs:**
- Repository local path
- Supported file extensions

**Processing:**
1. Traverse repository directory tree
2. Identify code files by extension
3. Exclude non-code files (config, docs, binary)
4. For each code file:
   - Count non-empty, non-comment lines
   - Track if <130 lines
5. Calculate totals:
   - `total_lines`: Sum of all line counts
   - `total_files`: Count of code files
   - `files_under_130`: Count of files with <130 lines
6. Calculate grade: `(files_under_130 / total_files) * 100`

**Outputs:**
- `total_lines`: Integer
- `total_files`: Integer
- `files_under_130`: Integer
- `grade`: Float (0.00-100.00, 2 decimal places)

**Business Logic:**

**Line Counting Rules:**
```python
def should_count_line(line: str) -> bool:
    """Determine if a line should be counted"""
    # Remove whitespace
    stripped = line.strip()

    # Exclude blank lines
    if not stripped:
        return False

    # Exclude pure comment lines
    comment_prefixes = ['#', '//', '/*', '*', '*/']
    if any(stripped.startswith(prefix) for prefix in comment_prefixes):
        return False

    # Count everything else (including code + inline comments)
    return True
```

**File Inclusion Rules:**
```python
# Code file extensions (case-insensitive)
CODE_EXTENSIONS = {
    '.py', '.js', '.jsx', '.ts', '.tsx',
    '.java', '.c', '.cpp', '.h', '.hpp',
    '.cs', '.go', '.rb', '.rs', '.php',
    '.swift', '.kt'
}

# Excluded directories (don't traverse)
EXCLUDED_DIRS = {
    'node_modules', 'dist', 'build', '.git',
    '__pycache__', 'venv', '.venv', 'env',
    'target', 'bin', 'obj'
}

# Excluded file patterns
EXCLUDED_FILES = {
    'package.json', 'package-lock.json',
    'requirements.txt', 'Gemfile', 'Gemfile.lock',
    '.gitignore', '.env', '.env.local',
    '*.config.js', '*.config.ts',
    'README*', 'LICENSE*', 'CHANGELOG*',
    '*.md', '*.txt', '*.rst',
    '*.pyc', '*.class', '*.exe', '*.dll'
}
```

**Grade Calculation:**
```python
def calculate_grade(files_under_130: int, total_files: int) -> float:
    """Calculate grade as percentage of files under 130 lines"""
    if total_files == 0:
        return 0.00  # Edge case: no code files

    percentage = (files_under_130 / total_files) * 100
    return round(percentage, 2)
```

**Examples:**
```
Repo 1: 5 files, 4 under 130 lines
  - Grade = (4 / 5) * 100 = 80.00%

Repo 2: 10 files, 10 under 130 lines
  - Grade = (10 / 10) * 100 = 100.00%

Repo 3: 5 files, 0 under 130 lines
  - Grade = (0 / 5) * 100 = 0.00%

Repo 4: 0 files (no code found)
  - Grade = 0.00% (edge case)
```

**Edge Cases:**
- Empty repository: `total_files = 0`, `grade = 0.00`
- No code files (only docs): `total_files = 0`, `grade = 0.00`
- All files > 130 lines: `files_under_130 = 0`, `grade = 0.00`
- Single small file: `files_under_130 = 1`, `total_files = 1`, `grade = 100.00`

**Acceptance Criteria:**
- Accurately counts lines (98%+ accuracy vs. manual)
- Correctly identifies code vs. non-code files
- Handles edge cases without errors
- Grade formula produces expected results

### FR-4: Multithreaded Processing

**Description:** Process multiple repositories in parallel

**Inputs:**
- List of repository URLs
- Number of worker threads (default: 5, max: 10)

**Processing:**
1. Create ThreadPoolExecutor with N workers
2. Submit repository processing tasks
3. Collect results in thread-safe queue
4. Update progress bar
5. Wait for all tasks to complete
6. Aggregate results

**Outputs:**
- Results for all repositories
- Processing statistics (time, success rate)

**Configuration:**
```python
# Default settings
DEFAULT_WORKERS = 5
MAX_WORKERS = 10
MIN_WORKERS = 1

# Adjust based on repo count
if num_repos < 5:
    workers = 1  # Sequential for small batches
elif num_repos < 20:
    workers = 5
else:
    workers = 10
```

**Thread Safety:**
- Use `concurrent.futures.ThreadPoolExecutor`
- Results collected in `queue.Queue` (thread-safe)
- Progress updates via `threading.Lock`
- No shared mutable state between threads

**Performance:**
- Expected speedup: 4-8x vs. sequential
- Target: 30 repos in <25 minutes

**Acceptance Criteria:**
- Produces identical results to sequential processing
- No race conditions or data corruption
- Handles thread exceptions gracefully
- Progress tracking works correctly

### FR-5: Excel Output Generation

**Description:** Generate Excel with original data plus grades

**Inputs:**
- Original Excel data (ID, Date, Subject, URL)
- Processing results (grades, metrics, errors)
- Output file path

**Processing:**
1. Create new Excel workbook
2. Create "Graded Results" sheet
3. Write headers: ID, Date, Subject, URL, Grade, Total Files, Files <130, Total Lines, Status, Error
4. Write data rows (preserve original order)
5. Create "Summary" sheet with statistics
6. Format cells (percentages, alignment, colors)
7. Auto-size columns
8. Save to output directory

**Output Format:**

**Sheet 1: Graded Results**
| Column | Type | Description | Example |
|--------|------|-------------|---------|
| ID | Text | Original ID from input | "1" |
| Date | DateTime | Email date from input | "2025-11-20 10:30:00" |
| Subject | Text | Email subject from input | "Homework 1 Submission" |
| URL | Text | Repository URL | "github.com/student1/hw1" |
| Grade | Percentage | Calculated grade | "80.00%" |
| Total Files | Integer | Count of code files | "5" |
| Files <130 | Integer | Files under 130 lines | "4" |
| Total Lines | Integer | Sum of all lines | "469" |
| Status | Text | "Success" or "Error" | "Success" |
| Error | Text | Error message if failed | "" or "Repository not found" |

**Sheet 2: Summary**
```
Grading Summary - Generated 2025-11-23 14:30:00

Total Repositories: 30
Successfully Graded: 28
Errors: 2

Grade Statistics:
  Average: 72.5%
  Median: 75.0%
  Min: 0.0%
  Max: 100.0%
  Std Dev: 18.3%

Grade Distribution:
  0-20%: 2 repos (7%)
  20-40%: 1 repo (3%)
  40-60%: 5 repos (17%)
  60-80%: 12 repos (40%)
  80-100%: 10 repos (33%)

Error Report:
  - student2/hw1: Repository not found
  - student15/hw1: Clone timeout
```

**File Naming:**
- Input: `homework_emails.xlsx`
- Output: `homework_emails_graded.xlsx`
- Location: `output/` directory (auto-created)

**Acceptance Criteria:**
- Excel opens correctly in Excel/Google Sheets
- All data preserved from input
- Grades and metrics accurate
- Summary statistics correct
- Professional formatting

---

## Non-Functional Requirements

### Performance

**Target Metrics:**
- **30 repositories**: <25 minutes (max acceptable: 45 min)
- **Sequential baseline**: ~2-3 min per repo
- **Parallel speedup**: 4-8x (with 5-10 workers)
- **Memory usage**: <3GB peak
- **Disk usage**: <5GB temporary (cleaned up after)

**Optimization Strategies:**
- Shallow clone (--depth=1) for speed
- Parallel processing for I/O-bound operations
- Efficient file traversal (skip excluded directories)
- Minimal string operations in hot paths

### Reliability

**Target Metrics:**
- **Excel output success**: 100% (never corrupt Excel)
- **Metric accuracy**: 98%+ (vs. manual verification)
- **Error recovery**: 100% (never crash entire run for one bad repo)
- **Data consistency**: 100% (thread-safe operations)

**Reliability Strategies:**
- Retry transient errors (3x with backoff)
- Validate input before processing
- Thread-safe result collection
- Graceful error handling (continue on failures)
- Comprehensive logging

### Security

**Considerations:**
- Clone to temporary directory (isolated)
- Clean up after processing (no residual data)
- Read-only operations (never modify repos)
- No credentials stored (public repos only in v1.0)
- Sandbox execution (no arbitrary code execution)

**Out of Scope for v1.0:**
- Private repository support
- Authentication/authorization
- Encrypted storage

### Usability

**CLI Design Principles:**
- Simple defaults (single required argument)
- Clear progress feedback
- Helpful error messages
- Non-technical language

**Example Usage:**
```bash
# Simplest usage (all defaults)
repoanalyzer analyze --input homework_emails.xlsx

# With options
repoanalyzer analyze --input hw.xlsx --output graded.xlsx --threads 10

# Help is clear and concise
repoanalyzer --help
```

**Progress Output:**
```
Repository Analyzer v1.0.0

Validating input...
✓ Found 30 repository URLs in homework_emails.xlsx

Processing with 5 worker threads...
[████████████░░░░░░░░] 15/30 (50%) - ETA: 12 min

✓ student1/hw1 - Grade: 80.00%
✓ student2/hw1 - Grade: 100.00%
✗ student3/hw1 - Error: Repository not found
✓ student4/hw1 - Grade: 65.00%

Completed: 28/30 in 18 minutes
Errors: 2 (see output for details)

Output saved to: output/homework_emails_graded.xlsx
```

### Compatibility

**Operating Systems:**
- Windows 10/11
- macOS 11+
- Linux (Ubuntu 20.04+, CentOS 8+)

**Python:**
- Python 3.8+
- Python 3.9, 3.10, 3.11 tested

**Dependencies:**
- openpyxl (Excel)
- GitPython (Git operations)
- click (CLI)
- tqdm (progress bars)

---

## Technical Design

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    CLI Interface (Click)                │
│                  repoanalyzer/cli.py                    │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────▼────────────┐
        │   Orchestrator          │
        │   (Main Controller)     │
        │   - Input validation    │
        │   - Thread management   │
        │   - Result aggregation  │
        └────┬────────────────┬───┘
             │                │
    ┌────────▼─────┐    ┌────▼────────────┐
    │ Excel Reader │    │ Thread Pool     │
    │ (openpyxl)   │    │ (5-10 workers)  │
    └──────────────┘    └────┬────────────┘
                             │
                    ┌────────▼──────────┐
                    │  Worker Thread    │
                    │  (per repository) │
                    └────┬──────────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
    ┌────▼─────┐   ┌────▼────┐   ┌─────▼──────┐
    │ Git      │   │ Metrics │   │ Result     │
    │ Cloner   │───│ Counter │───│ Collector  │
    │          │   │         │   │ (Queue)    │
    └──────────┘   └─────────┘   └─────┬──────┘
                                       │
                              ┌────────▼──────┐
                              │ Excel Writer  │
                              │ (openpyxl)    │
                              └───────────────┘
```

### Data Flow

```
1. INPUT
   homework_emails.xlsx
   ↓
2. VALIDATION
   Extract URLs (30 repos)
   ↓
3. PARALLEL PROCESSING (5 workers)
   ├─ Worker 1: Clone → Count → Grade → Queue result
   ├─ Worker 2: Clone → Count → Grade → Queue result
   ├─ Worker 3: Clone → Count → Grade → Queue result
   ├─ Worker 4: Clone → Count → Grade → Queue result
   └─ Worker 5: Clone → Count → Grade → Queue result
   ↓
4. RESULT AGGREGATION
   Collect 30 results from queue
   ↓
5. OUTPUT GENERATION
   homework_emails_graded.xlsx
   ├─ Sheet 1: Graded Results (30 rows)
   └─ Sheet 2: Summary (statistics)
```

### Core Modules

#### Module: excel_reader.py
**Purpose:** Read and validate Excel input

```python
class ExcelReader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.workbook = None
        self.data = []

    def read(self) -> List[Dict]:
        """Read Excel and extract repository URLs"""
        # Open workbook
        # Validate columns
        # Extract rows with non-empty URLs
        # Return list of dicts: {id, date, subject, url}

    def validate(self) -> Tuple[bool, str]:
        """Validate Excel structure and content"""
        # Check file exists
        # Check required columns
        # Check URL column has data
        # Return (is_valid, error_message)
```

#### Module: repo_cloner.py
**Purpose:** Clone GitHub repositories

```python
class RepoCloner:
    def __init__(self, temp_dir: str, timeout: int = 300):
        self.temp_dir = temp_dir
        self.timeout = timeout

    def clone(self, url: str) -> Tuple[str, bool, str]:
        """Clone repository to temporary directory"""
        # Validate URL format
        # Extract repo name
        # Create local path
        # Clone with GitPython (shallow, timeout)
        # Retry 3x on transient errors
        # Return (local_path, success, error_message)

    def cleanup(self):
        """Remove temporary directory"""
        # Delete temp_dir and all contents
```

#### Module: metrics_calculator.py
**Purpose:** Calculate code metrics and grade

```python
class MetricsCalculator:
    CODE_EXTENSIONS = {'.py', '.js', '.java', ...}
    EXCLUDED_DIRS = {'node_modules', '.git', ...}
    LINE_LIMIT = 130

    def calculate(self, repo_path: str) -> Dict:
        """Calculate metrics for repository"""
        # Traverse directory tree
        # Identify code files
        # Count lines per file
        # Calculate totals
        # Calculate grade
        # Return {total_lines, total_files, files_under_130, grade}

    def count_lines(self, file_path: str) -> int:
        """Count non-empty, non-comment lines in file"""
        # Read file
        # Filter blank/comment lines
        # Return count

    def is_code_file(self, file_path: str) -> bool:
        """Check if file is a code file (vs. config/docs)"""
        # Check extension
        # Check exclusion patterns
        # Return boolean
```

#### Module: parallel_processor.py
**Purpose:** Manage multithreaded processing

```python
class ParallelProcessor:
    def __init__(self, num_workers: int = 5):
        self.num_workers = num_workers
        self.results_queue = queue.Queue()
        self.progress_lock = threading.Lock()

    def process(self, repos: List[Dict]) -> List[Dict]:
        """Process repositories in parallel"""
        # Create ThreadPoolExecutor
        # Submit tasks for each repo
        # Collect results in queue
        # Update progress
        # Return list of results

    def process_single_repo(self, repo_data: Dict) -> Dict:
        """Process a single repository (worker function)"""
        # Clone repository
        # Calculate metrics
        # Calculate grade
        # Add to results queue
        # Return result dict
```

#### Module: excel_writer.py
**Purpose:** Generate graded Excel output

```python
class ExcelWriter:
    def __init__(self, output_path: str):
        self.output_path = output_path

    def write(self, original_data: List[Dict], results: List[Dict]):
        """Generate Excel with grades"""
        # Create workbook
        # Add "Graded Results" sheet
        # Add "Summary" sheet
        # Format cells
        # Save file

    def create_results_sheet(self, wb, original_data, results):
        """Create graded results sheet"""
        # Merge original data with results
        # Write headers
        # Write rows
        # Format columns

    def create_summary_sheet(self, wb, results):
        """Create summary statistics sheet"""
        # Calculate statistics
        # Generate distribution
        # List errors
        # Format as report
```

### Technology Stack

**Language:** Python 3.8+

**Core Libraries:**
- `openpyxl>=3.1.0` - Excel file I/O
- `GitPython>=3.1.40` - Git repository cloning
- `click>=8.1.0` - CLI framework
- `tqdm>=4.66.0` - Progress bars

**Standard Library:**
- `concurrent.futures` - Thread pool
- `threading` - Thread safety (Lock, Queue)
- `pathlib` - File path operations
- `tempfile` - Temporary directories
- `logging` - Error logging
- `statistics` - Summary calculations
- `re` - URL validation

### Project Structure

```
EmailSkillAgents/
├── repoanalyzer/              # Main package
│   ├── __init__.py           # Package initialization
│   ├── cli.py                # CLI interface (Click)
│   ├── excel_reader.py       # Read input Excel
│   ├── excel_writer.py       # Write output Excel
│   ├── repo_cloner.py        # Clone repositories
│   ├── metrics_calculator.py # Calculate code metrics
│   ├── parallel_processor.py # Multithreading orchestration
│   └── utils.py              # Shared utilities
├── tests/                     # Test suite
│   ├── test_excel_reader.py
│   ├── test_repo_cloner.py
│   ├── test_metrics.py
│   ├── test_parallel.py
│   └── fixtures/              # Test data
│       ├── sample_input.xlsx
│       └── sample_repos/
├── output/                    # Generated output files (auto-created)
├── exports/                   # Input files from GmailAgent
│   └── homework_emails.xlsx
├── setup.py                   # Package setup
├── requirements.txt           # Dependencies
├── README.md                  # User documentation
├── PRD-RepositoryAnalyzer.md # This document
└── .gitignore                # Git ignore rules
```

---

## Implementation Plan

### Development Approach: Incremental MVP

**Philosophy:** Build the simplest version that works, then add complexity

### Phase 1: Foundation (Week 1-2)

**Goal:** Sequential MVP - Process 10 repos successfully

**Tasks:**
- [ ] Project setup (structure, dependencies)
- [ ] Excel reader module (read GmailAgent Excel)
- [ ] Repository cloner (sequential, single repo)
- [ ] Basic metrics calculator (line counting, grade)
- [ ] Excel writer (basic output)
- [ ] Simple CLI (analyze command)

**Deliverable:**
```bash
repoanalyzer analyze --input sample.xlsx
# Processes 10 repos sequentially in ~20 minutes
# Outputs graded Excel with correct metrics
```

**Success Criteria:**
- Reads Excel correctly
- Clones 1 repo successfully
- Calculates metrics accurately (verified manually)
- Outputs Excel with grades
- Handles 1 error type (404)

### Phase 2: Robustness (Week 3)

**Goal:** Handle all error cases and edge cases

**Tasks:**
- [ ] Comprehensive error handling (404, timeout, network, empty repo)
- [ ] Retry logic with exponential backoff
- [ ] Edge case handling (0 files, all files >130 lines, binary files)
- [ ] File type filtering (exclude config, docs, binary)
- [ ] Input validation (check Excel structure)
- [ ] Logging (errors, warnings, info)

**Deliverable:**
- Handles all error scenarios gracefully
- Processes repos with edge cases correctly
- Comprehensive error messages

**Success Criteria:**
- Processes 30 mixed repos (some errors) without crashing
- Error messages are clear and actionable
- Logs all issues for debugging

### Phase 3: Multithreading (Week 4-5)

**Goal:** Parallel processing for performance

**Tasks:**
- [ ] Thread pool implementation (ThreadPoolExecutor)
- [ ] Thread-safe result collection (Queue)
- [ ] Parallel cloning and processing
- [ ] Progress tracking for multiple threads
- [ ] Worker count configuration (CLI flag)
- [ ] Performance testing (measure speedup)

**Deliverable:**
```bash
repoanalyzer analyze --input hw.xlsx --threads 5
# Processes 30 repos in <25 minutes (vs. 60+ min sequential)
# Shows real-time progress for all workers
```

**Success Criteria:**
- 4-8x speedup vs. sequential
- Identical results to sequential processing
- No race conditions or data corruption
- Progress bar works correctly

### Phase 4: Polish & UX (Week 6)

**Goal:** Professional user experience

**Tasks:**
- [ ] CLI improvements (help text, validation, confirmations)
- [ ] Progress indicators (spinner, ETA, per-repo status)
- [ ] Summary statistics sheet (average, median, distribution)
- [ ] Excel formatting (colors, alignment, auto-width)
- [ ] Output directory management (auto-create, custom path)
- [ ] User documentation (README, examples)

**Deliverable:**
- Professional CLI with clear feedback
- Polished Excel output
- Comprehensive README

### Phase 5: Testing & Documentation (Week 7-8)

**Goal:** Production-ready quality

**Tasks:**
- [ ] Unit tests (>80% coverage)
  - Excel reader/writer
  - Metrics calculator
  - Repo cloner
  - Parallel processor
- [ ] Integration tests (end-to-end)
- [ ] Manual testing (real repos, various languages)
- [ ] Performance testing (30, 50, 100 repos)
- [ ] Documentation (README, CLI help, examples)
- [ ] Bug fixes and refinements

**Deliverable:**
- Test suite with >80% coverage
- All tests passing
- Complete documentation
- v1.0.0 release ready

**Success Criteria:**
- All functional requirements met
- All acceptance criteria passing
- Performance targets achieved
- Documentation complete

### Timeline

| Week | Focus | Deliverable | Milestone |
|------|-------|-------------|-----------|
| 1-2 | Foundation | Sequential MVP | Processes 10 repos |
| 3 | Robustness | Error handling | Handles all errors |
| 4-5 | Performance | Multithreading | <25 min for 30 repos |
| 6 | Polish | UX improvements | Professional tool |
| 7-8 | Testing | Test suite + docs | Production ready |

**Total:** 8 weeks to v1.0.0

---

## Testing Plan

### Unit Tests

**test_excel_reader.py:**
- Read valid Excel with all columns
- Read Excel with missing columns (error)
- Read Excel with no URLs (error)
- Read Excel with mixed valid/invalid URLs
- Validate Excel structure

**test_repo_cloner.py:**
- Clone valid public repository
- Handle 404 (repository not found)
- Handle timeout (large repo)
- Handle network error
- Retry logic (3x with backoff)
- Cleanup temp directory

**test_metrics_calculator.py:**
- Count lines correctly (exclude blanks/comments)
- Identify code files (exclude config/docs)
- Calculate grade (various scenarios)
- Handle edge cases (0 files, all >130 lines)
- Support multiple languages

**test_excel_writer.py:**
- Write Excel with all columns
- Generate summary sheet
- Format cells correctly
- Preserve original data
- Handle special characters

**test_parallel_processor.py:**
- Process repos in parallel
- Thread-safe result collection
- Handle thread exceptions
- Progress tracking
- Identical results to sequential

**Coverage Target:** >80%

### Integration Tests

**test_end_to_end.py:**
- Full workflow: Excel → Clone → Calculate → Output
- Process 5 test repos (various scenarios)
- Verify output Excel correctness
- Verify summary statistics
- Verify temporary cleanup

**Test Fixtures:**
```
tests/fixtures/
├── sample_input.xlsx        # 5 test repos
├── sample_repos/            # Pre-cloned test repos
│   ├── repo_perfect/        # 100% grade (all files <130)
│   ├── repo_mixed/          # 80% grade (4/5 files <130)
│   ├── repo_monolithic/     # 0% grade (all files >130)
│   ├── repo_empty/          # 0 files (edge case)
│   └── repo_multilang/      # Mixed languages
└── expected_output.xlsx     # Expected results
```

### Manual Testing

**Test Scenarios:**
1. **Happy path:** 30 valid repos, all clone successfully
2. **Error handling:** Mix of valid/invalid repos (404, timeout, empty)
3. **Edge cases:** Repos with 0 files, all large files, binary files
4. **Performance:** 50 repos, measure time, verify speedup
5. **Cross-platform:** Test on Windows, macOS, Linux
6. **Real-world:** Use actual student homework repos

**Test Checklist:**
- [ ] Reads GmailAgent Excel correctly
- [ ] Clones repositories without errors
- [ ] Calculates metrics accurately (spot-check 10 repos manually)
- [ ] Outputs valid Excel (opens in Excel/Google Sheets)
- [ ] Summary statistics are correct
- [ ] Progress bar works smoothly
- [ ] Error messages are clear
- [ ] Handles all edge cases
- [ ] Performance targets met (<25 min for 30 repos)
- [ ] No crashes or data corruption

### Performance Testing

**Benchmark:**
- Sequential: 10, 30, 50 repos (measure time)
- Parallel (5 workers): 10, 30, 50 repos (measure speedup)
- Parallel (10 workers): 10, 30, 50 repos (measure speedup)

**Expected Results:**
| Repos | Sequential | Parallel (5) | Parallel (10) | Speedup |
|-------|------------|--------------|---------------|---------|
| 10 | ~20 min | ~8 min | ~5 min | 2-4x |
| 30 | ~60 min | ~18 min | ~12 min | 3-5x |
| 50 | ~100 min | ~25 min | ~15 min | 4-6x |

**Acceptance Criteria:**
- 30 repos in <25 minutes (parallel)
- Speedup ≥ 4x (5 workers vs. sequential)

---

## Launch Plan

### Pre-Launch (Week 7)

**Internal Testing:**
- [ ] Test with 5 real instructor users (alpha testing)
- [ ] Collect feedback on UX, errors, performance
- [ ] Fix critical bugs

**Documentation:**
- [ ] README with installation, usage, examples
- [ ] CLI help text reviewed
- [ ] Troubleshooting guide
- [ ] Example input/output files

**Preparation:**
- [ ] Create GitHub repository (public)
- [ ] Write release notes
- [ ] Prepare demo video/screenshots

### Launch (Week 8)

**Distribution:**
- [ ] Publish to GitHub
- [ ] Create PyPI package (optional)
- [ ] Share with instructor community

**Announcement:**
- [ ] Internal announcement (university/institution)
- [ ] Post to relevant forums (r/learnprogramming, teaching communities)
- [ ] Share on LinkedIn/Twitter

### Post-Launch (Week 9-12)

**Monitoring:**
- [ ] Track usage (number of instructors, repos graded)
- [ ] Monitor GitHub issues (bugs, feature requests)
- [ ] Collect user feedback (surveys)

**Support:**
- [ ] Respond to issues within 48 hours
- [ ] Fix critical bugs within 1 week
- [ ] Document common issues in FAQ

**Iteration:**
- [ ] Gather v1.1 feature requests
- [ ] Prioritize enhancements
- [ ] Plan v1.1 roadmap

---

## Risks & Mitigation

| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
| **Grading formula doesn't match instructor expectations** | Medium | High | Conduct user research with 5 instructors before development. Make formula configurable in v1.1. | PM |
| **Multithreading introduces bugs (race conditions)** | Medium | Critical | Start with sequential MVP. Extensive testing. Use well-tested concurrency patterns. | Tech Lead |
| **GitHub rate limiting for public repos** | Low | Medium | Monitor rate limits. Add retry logic. Document limits in README. | Developer |
| **Large repositories (>1GB) timeout or crash** | Medium | Medium | Set timeout (5 min). Use shallow clone. Warn on large repos. | Developer |
| **Binary files inflate line counts** | Low | Low | Exclude binary files by extension. Skip files with null bytes. | Developer |
| **Tool too slow (doesn't meet <30 min target)** | Medium | High | Profile performance. Optimize hot paths. Increase thread count if safe. | Tech Lead |
| **Students submit private repos (access denied)** | High | Low | Document limitation (public repos only). Plan private repo support for v1.1. | PM |
| **Excel corruption with multithreading** | Low | Critical | Use thread-safe queue pattern. Test extensively. Validate output. | Tech Lead |
| **Installation issues (dependency conflicts)** | Medium | Medium | Pin dependency versions. Provide installation guide. Test on fresh environments. | Developer |

---

## Dependencies & Assumptions

### Dependencies

**Internal:**
- GmailAgent (provides input Excel)
- Output directory (write access required)
- Temporary directory (disk space for cloning)

**External:**
- Python 3.8+ installed
- Git installed (for GitPython)
- Internet connection (to clone repos)
- GitHub (public repositories)

**Libraries:**
- openpyxl
- GitPython
- click
- tqdm

### Assumptions

**User Assumptions:**
- Users are instructors with programming knowledge
- Users can run command-line tools
- Users understand Git/GitHub basics
- Students submit public repositories (or provide access)

**Technical Assumptions:**
- Repository URLs are valid GitHub HTTPS URLs
- Repositories are <1GB (reasonable size)
- Students write code in supported languages (Python, JS, Java, etc.)
- Network connection is stable (at least for cloning)

**Educational Assumptions:**
- File count and line distribution are valid metrics for grading
- 130 lines per file is a reasonable threshold for "good code organization"
- Instructors want automated basic grading to focus on code review

**Business Assumptions:**
- Instructors value time savings (willing to use new tool)
- 90% time reduction is meaningful enough to drive adoption
- Grading formula aligns with teaching goals

### Constraints

**Budget:** $0 (internal tool, no external costs)

**Timeline:** 8 weeks (realistic for complexity)

**Resources:**
- 1 backend developer (full-time)
- 1 QA engineer (part-time, weeks 7-8)
- 1 product manager (oversight)

**Technical:**
- Public repositories only (v1.0)
- HTTPS clone only (no SSH)
- Code files only (no binary analysis)
- Single-threaded Git operations (GitPython limitation)

---

## Open Questions & Decisions

### RESOLVED: Grading Formula

**Question:** What formula should we use to calculate grades?

**Options Considered:**
1. `(files <130 lines / total lines) * 100` → **REJECTED** (nonsensical, yields <1%)
2. `(files <130 lines / total files) * 100` → **SELECTED** (makes sense, 0-100% range)
3. Custom weighted formula → **Deferred to v1.1**

**Decision:** Use formula #2: `(files <130 lines / total files) * 100`

**Rationale:**
- Produces meaningful percentages (0-100%)
- Directly measures what we care about: proportion of well-structured files
- Easy to explain to instructors and students
- Aligns with educational goal (encourage small, focused files)

**Owner:** Product Manager
**Date:** 2025-11-23

### RESOLVED: Line Limit Threshold

**Question:** Should 130 lines be configurable?

**Decision:** Hardcoded at 130 for v1.0, configurable in v1.1

**Rationale:**
- 130 is industry standard (Google Style Guide)
- Reduces complexity for MVP
- Can add `--line-limit` flag in v1.1 based on user feedback

### OPEN: Private Repository Support

**Question:** Should v1.0 support private repositories?

**Status:** Deferred to v1.1

**Rationale:**
- Adds complexity (SSH keys, tokens, authentication)
- Most educational repos are public
- Can ship faster without this feature
- v1.1 can add `--token` flag for private repo support

**Owner:** Product Manager
**Due:** Week 4 (finalize v1.1 scope)

### OPEN: Custom Grading Formulas

**Question:** Should instructors be able to customize the grading formula?

**Status:** Deferred to v1.1

**Rationale:**
- Adds significant complexity (formula parsing, validation)
- Need to validate that default formula works for most users first
- Can gather feedback on desired formulas during v1.0 usage

**Next Steps:**
- Survey 10 instructors on desired grading criteria
- Design formula configuration system
- Plan for v1.1 release

**Owner:** Product Manager
**Due:** Week 8 (post-launch research)

### OPEN: Multi-Language Support

**Question:** Which programming languages should we support?

**Current Decision:**
- Python, JavaScript, Java, C/C++, C#, Go, Ruby, Rust, PHP, Swift, Kotlin

**Validation Needed:**
- Survey instructors on languages taught
- Test line counting accuracy per language

**Owner:** Developer
**Due:** Week 1

---

## User Research & Validation

### Research Questions

**Before Development (Week 1):**
1. Does the grading formula align with instructor expectations?
2. What programming languages do instructors teach?
3. What is the current grading workflow and pain points?
4. What metrics matter most for basic code quality?
5. Is 130 lines the right threshold, or should it vary by language?

### Research Methods

**User Interviews (5-10 instructors):**
- Current grading workflow walkthrough
- Pain points and time estimates
- Reaction to grading formula
- Desired features and concerns

**Survey (20-30 instructors):**
- Languages taught
- Class sizes
- Current tools used
- Willingness to adopt automated grading

**Prototype Testing (Week 7):**
- Give tool to 5 alpha testers
- Observe usage and collect feedback
- Measure time savings
- Identify usability issues

### Success Criteria for Research

- 80%+ of instructors agree grading formula is reasonable
- Time savings validated (>80% reduction)
- No major blockers identified
- Feature requests align with v1.1 roadmap

---

## Appendix

### Glossary

- **Repository:** Git repository containing student code
- **Clone:** Local copy of Git repository
- **Code metrics:** Quantitative measurements (lines, files, etc.)
- **Grade:** Calculated score based on metrics (0-100%)
- **Line of code:** Non-empty, non-comment line
- **Worker thread:** Parallel execution unit
- **Thread-safe:** Safe for concurrent access

### Example Calculations

**Scenario 1: Well-Structured Code**
```
Repository: student1/homework1
Files:
  - main.py: 85 lines ✓
  - utils.py: 120 lines ✓
  - models.py: 95 lines ✓
  - tests.py: 110 lines ✓
  - config.json: (excluded)

Total files: 4
Files <130 lines: 4
Grade: (4 / 4) * 100 = 100.00%
```

**Scenario 2: Monolithic Code**
```
Repository: student2/homework1
Files:
  - solution.py: 450 lines ✗

Total files: 1
Files <130 lines: 0
Grade: (0 / 1) * 100 = 0.00%
```

**Scenario 3: Mixed**
```
Repository: student3/homework1
Files:
  - part1.py: 200 lines ✗
  - part2.py: 180 lines ✗
  - helper.py: 75 lines ✓
  - main.py: 50 lines ✓

Total files: 4
Files <130 lines: 2
Grade: (2 / 4) * 100 = 50.00%
```

### File Type Detection Examples

**Included (code files):**
```
✓ main.py
✓ app.js
✓ Component.tsx
✓ Main.java
✓ server.go
✓ utils.rb
```

**Excluded (non-code):**
```
✗ package.json (config)
✗ README.md (documentation)
✗ requirements.txt (config)
✗ .gitignore (version control)
✗ image.png (binary)
✗ node_modules/lodash.js (dependency)
```

### CLI Examples

```bash
# Basic usage
repoanalyzer analyze --input homework_emails.xlsx

# Custom output path
repoanalyzer analyze --input hw.xlsx --output graded_hw1.xlsx

# Adjust thread count
repoanalyzer analyze --input hw.xlsx --threads 10

# Show help
repoanalyzer --help
repoanalyzer analyze --help

# Version
repoanalyzer --version
```

### Expected Output Example

**Console Output:**
```
Repository Analyzer v1.0.0

Validating input: homework_emails.xlsx
✓ Found 30 valid repository URLs

Creating temporary directory: /tmp/repoanalyzer_20251123_143000/
Processing with 5 worker threads...

[████████████████████████] 30/30 (100%) - 18:32 elapsed

Results:
✓ student1/hw1 - Grade: 80.00% (4/5 files <130 lines)
✓ student2/hw1 - Grade: 100.00% (3/3 files <130 lines)
✗ student3/hw1 - ERROR: Repository not found
✓ student4/hw1 - Grade: 50.00% (2/4 files <130 lines)
... (26 more)

Summary:
  Successfully graded: 28/30
  Failed: 2/30
  Average grade: 72.50%
  Processing time: 18 minutes 32 seconds

Output saved to: output/homework_emails_graded.xlsx

✓ Cleanup complete. Temporary files removed.
```

---

## Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-23 | Architecture Reviewer | Initial PRD draft with grading formula question |
| 2.0 | 2025-11-23 | Product Strategist | Comprehensive product strategy review:<br>- Resolved grading formula (BLOCKING issue)<br>- Added user problem statement and persona<br>- Defined clear value proposition<br>- Enhanced success metrics (North Star, KPIs)<br>- Added 15 detailed user stories with acceptance criteria<br>- Expanded functional requirements with edge cases<br>- Added user research section<br>- Refined technical design with clear architecture<br>- Realistic 8-week incremental implementation plan<br>- Comprehensive testing plan with fixtures<br>- Risk analysis with mitigation strategies<br>- Open questions documented and resolved<br>- Example calculations and CLI usage |

---

## Next Steps

1. **Product Review** (Week 0):
   - [ ] Stakeholder review of PRD
   - [ ] Approval of grading formula
   - [ ] Confirm success metrics
   - [ ] Allocate resources (developer, QA)

2. **User Research** (Week 1):
   - [ ] Interview 5 instructors
   - [ ] Survey 20 instructors on languages and workflow
   - [ ] Validate grading formula
   - [ ] Confirm line limit threshold (130)

3. **Technical Design** (Week 1):
   - [ ] Tech lead reviews architecture
   - [ ] Finalize technology choices
   - [ ] Set up development environment
   - [ ] Create project structure

4. **Development Kickoff** (Week 1):
   - [ ] Create GitHub repository
   - [ ] Set up CI/CD (optional)
   - [ ] Sprint 1 planning (sequential MVP)
   - [ ] Begin coding

---

**Status:** ✅ READY FOR DEVELOPMENT
**Blocker:** RESOLVED (grading formula clarified)
**Confidence:** HIGH (comprehensive product strategy, clear requirements, validated assumptions)

---

*This PRD has been reviewed and enhanced by the Product Strategy team to ensure clarity, user-centricity, and alignment with educational goals. All critical decisions have been made, and the product is ready for technical implementation.*
