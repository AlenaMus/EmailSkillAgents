# Repository Analyzer - Quick Start Guide

## 30-Second Quick Start

```bash
# 1. Make sure you have the dependencies installed
pip install GitPython tqdm

# 2. Run the analyzer
python -m repo_analyzer.cli analyze --input exports/homework_emails.xlsx

# 3. Check the output
# Opens: output/homework_emails_graded.xlsx
```

Done! Your graded Excel file is ready.

---

## What It Does

Takes an Excel file with GitHub repository URLs and produces:
- ✅ Graded results (based on file size distribution)
- ✅ Code metrics (lines, files)
- ✅ Summary statistics
- ✅ Error reports

**Grading Formula:** `(Files with <130 lines / Total files) × 100`

---

## Input Format

Your Excel file needs at least a **URL** column:

| ID | Date | Subject | URL |
|----|------|---------|-----|
| 1 | 2025-11-23 | HW1 | https://github.com/student1/project |
| 2 | 2025-11-23 | HW2 | https://github.com/student2/code |

---

## Output Format

**Two sheets:**

### Sheet 1: Graded Results
- All original columns PLUS:
  - **Grade** - Calculated grade (0-100%)
  - **Total Files** - Number of code files
  - **Files <130** - Files under 130 lines
  - **Total Lines** - Total lines of code
  - **Status** - Success/Error
  - **Error Message** - If failed

### Sheet 2: Summary
- Total repositories
- Success/failure counts
- Average, median, min, max grades
- Grade distribution
- Error report
- Processing time

---

## Common Commands

```bash
# Basic usage
python -m repo_analyzer.cli analyze --input hw.xlsx

# Custom output
python -m repo_analyzer.cli analyze --input hw.xlsx --output graded.xlsx

# Verbose mode
python -m repo_analyzer.cli analyze --input hw.xlsx --verbose

# Help
python -m repo_analyzer.cli analyze --help
```

---

## Supported Languages

Python, JavaScript/TypeScript, Java, C/C++, Go, Rust, Ruby, PHP, Swift, Kotlin, C#, Scala

---

## Troubleshooting

### "Excel file not found"
Check the file path. Use full path if needed.

### "Missing required columns: URL"
Your Excel needs at least a "URL" column.

### "Repository not found or deleted"
The GitHub URL is invalid or the repository doesn't exist.

### "Invalid GitHub URL format"
Make sure URLs are in format: `https://github.com/user/repo`

### Cleanup warning
Ignore it. Windows file locking issue, directory will be cleaned up later.

---

## What Gets Counted

**Included:**
- Code files (`.py`, `.js`, `.java`, `.cpp`, etc.)
- All non-empty lines (including comments)

**Excluded:**
- Config files (`package.json`, `requirements.txt`)
- Documentation (`.md`, `.txt`)
- Dependencies (`node_modules/`, `venv/`)
- Build artifacts (`dist/`, `build/`)
- Version control (`.git/`)

---

## Example Output

```
Repository Analyzer v1.0.0
==================================================

Reading input: exports/homework_emails.xlsx
Found 4 repository URLs

Processing repositories...

[1/4] Analyzing https://github.com/student1/hw1...
  Grade: 100.00%

[2/4] Analyzing https://github.com/student2/hw2...
  Grade: 75.00%

[3/4] Analyzing https://github.com/student3/hw3...
  Error: Repository not found or deleted

[4/4] Analyzing https://github.com/student4/hw4...
  Grade: 85.00%

Summary
==================================================
Successfully Analyzed: 3/4
Failed: 1/4
Average Grade: 86.67%
Processing Time: 0m 45s

Output: output/homework_emails_graded.xlsx

Analysis complete!
```

---

## Performance

- **4 repos:** ~30 seconds
- **30 repos:** ~3-5 minutes
- **Processing:** Sequential (one at a time)

*Phase 2 will add multithreading for 5-10x speedup*

---

## Need More Help?

- Full documentation: `repo_analyzer/README.md`
- Implementation details: `REPO_ANALYZER_IMPLEMENTATION_REPORT.md`
- Product requirements: `PRD-RepositoryAnalyzer.md`

---

**Version:** 1.0.0
**Status:** Production Ready
**Contact:** AI Development Course - Lesson 19
