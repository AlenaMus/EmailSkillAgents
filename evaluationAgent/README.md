# Evaluation Gmail Sender Agent

**Version:** 1.0.0
**Status:** Production Ready

Automatically creates and sends personalized grade evaluation emails to students based on graded Excel files.

## Overview

The **Evaluation Gmail Sender Agent** is the fourth and final agent in the automated homework grading workflow. It completes the feedback loop by sending personalized evaluation emails to students.

### Workflow Position

```
1. GmailAgent           → Export homework emails to Excel
2. Repository Analyzer  → Analyze repos, calculate grades
3. Personalized Greetings → Add persona-based feedback
4. Evaluation Sender    → Send feedback to students (THIS AGENT)
```

### Key Features

- Read Excel files with grades and personalized greetings
- Generate professional HTML email templates
- **Safe Mode:** Save emails as HTML files (default, no API needed)
- **Gmail API Mode:** Create drafts in Gmail (optional, requires setup)
- **Test Mode:** Send all emails to one recipient
- **Dry-Run Mode:** Preview without creating anything
- UTF-8 support (Hebrew characters)
- Mobile-responsive email design
- Comprehensive error handling

## Installation

### Prerequisites

```bash
# Python 3.8+
python --version

# Required packages (already in requirements.txt)
pip install openpyxl click
```

### Optional (for Gmail API mode)

```bash
pip install google-api-python-client google-auth-oauthlib
```

## Quick Start

### 1. Basic Usage (Safe Mode - HTML Files)

Create email drafts as HTML files (no Gmail API required):

```bash
python -m evaluationAgent.cli create-drafts
```

This will:
- Read `greetings_results/homework_emails_with_greetings.xlsx`
- Generate HTML emails for each student
- Save to `email_drafts/` folder
- Create a summary report

**Output:**
```
email_drafts/
├── email_1_grade_100_test_at_example_com.html
├── email_2_grade_75_test_at_example_com.html
├── email_3_grade_100_test_at_example_com.html
└── summary.txt
```

### 2. Test Mode (Send to Yourself)

Test with your own email address:

```bash
python -m evaluationAgent.cli create-drafts --to your@email.com
```

### 3. Custom Input File

Use a different Excel file:

```bash
python -m evaluationAgent.cli create-drafts --input path/to/your/file.xlsx
```

### 4. Dry Run (Preview Only)

Preview what would happen without creating files:

```bash
python -m evaluationAgent.cli create-drafts --dry-run
```

### 5. Gmail API Mode (Optional)

Create drafts directly in Gmail:

```bash
# First-time setup: Authenticate
python -m evaluationAgent.cli auth

# Create drafts in Gmail
python -m evaluationAgent.cli create-drafts --use-gmail
```

## Usage Examples

### Example 1: Default (Safe Mode)

```bash
python -m evaluationAgent.cli create-drafts
```

**Result:**
- Reads: `greetings_results/homework_emails_with_greetings.xlsx`
- Creates: HTML files in `email_drafts/`
- No Gmail API needed
- Safe to run anytime

### Example 2: Test with Your Email

```bash
python -m evaluationAgent.cli create-drafts --to instructor@school.edu
```

**Result:**
- All emails sent to `instructor@school.edu`
- Perfect for testing email format
- Review before sending to students

### Example 3: Verbose Output

```bash
python -m evaluationAgent.cli create-drafts --verbose
```

**Result:**
- Detailed progress information
- Shows skipped students with reasons
- Useful for debugging

### Example 4: Custom Instructor Name

```bash
python -m evaluationAgent.cli create-drafts --instructor-name "Prof. Smith"
```

**Result:**
- Email signature: "Best regards, Prof. Smith"
- Personalized instructor name

### Example 5: Gmail API Mode

```bash
# Authenticate (one-time)
python -m evaluationAgent.cli auth

# Create drafts in Gmail
python -m evaluationAgent.cli create-drafts --use-gmail

# Create and apply label
python -m evaluationAgent.cli create-drafts --use-gmail --verbose
```

**Result:**
- Drafts created in your Gmail account
- Label "lesson19Agents" applied
- Review drafts before sending

## Input File Format

The agent expects an Excel file with these columns:

| Column | Description | Required |
|--------|-------------|----------|
| ID | Unique student ID | Yes |
| Date | Submission date | No |
| Subject | Email subject | Yes |
| URL | Repository URL | Yes |
| Grade | Numeric grade (0-100) | Yes |
| Total Files | File count | No |
| Files <130 | Files under 130 lines | No |
| Total Lines | Total code lines | No |
| Status | Success/Failed | Yes |
| Error Message | Error details | No |
| Personalized Greeting | Feedback message | Yes |
| Greeting Persona | Persona type | No |

### Valid Student Criteria

A student is considered **valid for email** if:
- `Status == 'Success'`
- `Grade > 0`
- `Personalized Greeting` is not empty
- `URL` starts with `http://` or `https://`

Students not meeting these criteria are **skipped**.

## Email Template

### HTML Email Structure

```html
Hi there,

Your grade for this assignment: 95%

Feedback:
EXCELLENT! 95%! This is what I call WINNING!
Your work is outstanding, just outstanding...

Repository: https://github.com/student/repo

Best regards,
Your Instructor
```

### Template Features

- **Professional design** with inline CSS
- **Mobile-responsive** layout
- **UTF-8 encoding** (supports Hebrew, emojis)
- **Clickable repository links**
- **Styled feedback box** (highlighted)
- **Grade prominently displayed**

## CLI Commands

### `create-drafts`

Create email drafts for all students.

```bash
python -m evaluationAgent.cli create-drafts [OPTIONS]
```

**Options:**

| Option | Description | Default |
|--------|-------------|---------|
| `--input PATH` | Path to Excel file | `greetings_results/homework_emails_with_greetings.xlsx` |
| `--use-gmail` | Use Gmail API (create drafts in Gmail) | False (save to files) |
| `--to EMAIL` | Override recipient (for testing) | None |
| `--dry-run` | Preview only, don't create | False |
| `--verbose` | Enable verbose output | False |
| `--instructor-name TEXT` | Instructor name for signature | "Your Instructor" |

**Examples:**

```bash
# Default: Save to HTML files
python -m evaluationAgent.cli create-drafts

# Use Gmail API
python -m evaluationAgent.cli create-drafts --use-gmail

# Test mode
python -m evaluationAgent.cli create-drafts --to test@example.com

# Dry run
python -m evaluationAgent.cli create-drafts --dry-run

# Verbose
python -m evaluationAgent.cli create-drafts --verbose

# Custom instructor name
python -m evaluationAgent.cli create-drafts --instructor-name "Dr. Johnson"

# Combine options
python -m evaluationAgent.cli create-drafts \
  --input custom.xlsx \
  --to test@example.com \
  --instructor-name "Prof. Smith" \
  --verbose
```

### `auth`

Authenticate with Gmail API (required for `--use-gmail` mode).

```bash
python -m evaluationAgent.cli auth
```

This will:
1. Open browser for Google authentication
2. Request Gmail API permissions
3. Save credentials to `~/.gmailagent/token.json`

### `test`

Test reading Excel file without creating emails.

```bash
python -m evaluationAgent.cli test [--input PATH]
```

This will:
- Read Excel file
- Validate structure
- Show valid/invalid students
- Display reasons for skipped students

## Output

### HTML Email Files (Default Mode)

When running in default mode (no `--use-gmail`), emails are saved as HTML files:

```
email_drafts/
├── email_1_grade_100_test_at_example_com.html
├── email_2_grade_75_test_at_example_com.html
├── email_3_grade_100_test_at_example_com.html
└── summary.txt
```

**Filename format:** `email_{index}_grade_{grade}_{recipient}.html`

### Summary Report

A summary file is created after each run:

```
============================================================
EVALUATION GMAIL SENDER - SUMMARY
============================================================

Mode: Dry-Run (HTML files)
Timestamp: 2025-11-23 15:30:45

STATISTICS
------------------------------------------------------------
Total Students:        4
Valid for Email:       3
Emails Created:        3
Skipped:               1
Failed:                0

SKIPPED STUDENTS
------------------------------------------------------------
  - ID: 2f01b47c... | Reason: Status: Invalid URL

CREATED EMAILS
------------------------------------------------------------
  Output Directory: email_drafts/
  Files Created:
    - email_1_grade_100_test_at_example_com.html
    - email_2_grade_75_test_at_example_com.html
    - email_3_grade_100_test_at_example_com.html

NEXT STEPS
------------------------------------------------------------
  1. Review email content in email_drafts/
  2. To send via Gmail, use --use-gmail flag
  3. Set up Gmail API credentials if needed

============================================================
```

## Gmail API Setup (Optional)

To use `--use-gmail` mode, you need to set up Gmail API credentials.

### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project: "Evaluation Gmail Sender"
3. Enable Gmail API

### Step 2: Create OAuth Credentials

1. Go to APIs & Services > Credentials
2. Create OAuth 2.0 Client ID
3. Application type: Desktop app
4. Download `credentials.json`

### Step 3: Save Credentials

```bash
# Create directory
mkdir -p ~/.gmailagent

# Copy credentials
cp ~/Downloads/credentials.json ~/.gmailagent/credentials.json
```

### Step 4: Authenticate

```bash
python -m evaluationAgent.cli auth
```

This will open a browser for authentication. After successful authentication, credentials are saved to `~/.gmailagent/token.json`.

### Step 5: Use Gmail API

```bash
python -m evaluationAgent.cli create-drafts --use-gmail
```

## Error Handling

The agent handles various error scenarios gracefully:

### Missing Excel File

```
✗ Excel file not found: path/to/file.xlsx
```

**Solution:** Verify file path, ensure file exists.

### Invalid Excel Structure

```
✗ Invalid Excel file structure: Missing required columns: Grade, URL
```

**Solution:** Ensure Excel has all required columns.

### No Valid Students

```
⚠ No valid students to process. All students were skipped.
```

**Solution:** Check Excel data, ensure students have:
- `Status == 'Success'`
- `Grade > 0`
- Valid `URL`
- Non-empty `Personalized Greeting`

### Gmail Authentication Failed

```
✗ Gmail authentication failed: Credentials file not found
```

**Solution:** Run `python -m evaluationAgent.cli auth` to authenticate.

### Gmail API Error

```
✗ Gmail API error during 'create_draft': Rate limit exceeded
```

**Solution:** Wait and retry. The agent has built-in retry logic.

## Configuration

### Default Settings

Edit `evaluationAgent/config.py` to change defaults:

```python
# Email Settings
DEFAULT_INSTRUCTOR_NAME = "Your Instructor"
DEFAULT_RECIPIENT = "test@example.com"

# Gmail Settings
GMAIL_LABEL_NAME = "lesson19Agents"

# Paths
EMAIL_DRAFTS_DIR = PROJECT_ROOT / "email_drafts"
DEFAULT_INPUT_FILE = GREETINGS_RESULTS_DIR / "homework_emails_with_greetings.xlsx"
```

## Architecture

### Module Structure

```
evaluationAgent/
├── __init__.py              # Package initialization
├── cli.py                   # Click-based CLI
├── email_sender.py          # Main orchestrator
├── excel_reader.py          # Excel file parsing
├── gmail_client.py          # Gmail API wrapper
├── email_template.py        # HTML email generation
├── config.py                # Configuration constants
├── errors.py                # Custom exceptions
└── README.md                # This file
```

### Data Flow

```
Excel File
    ↓
ExcelReader (parse students)
    ↓
EmailSender (orchestrate)
    ↓
EmailTemplate (generate HTML)
    ↓
GmailClient (save/send)
    ↓
Output (HTML files or Gmail drafts)
```

### Key Classes

**StudentData:** Represents a student's grading information
- Properties: id, grade, subject, url, greeting, etc.
- Methods: `is_valid_for_email()`, `get_skip_reason()`

**ExcelReader:** Reads and parses Excel files
- Methods: `read()`, `_validate_headers()`, `_parse_rows()`

**EmailSender:** Main orchestrator
- Methods: `create_drafts()`, `_process_student()`, `_generate_summary()`

**GmailClient:** Gmail API wrapper
- Methods: `create_draft()`, `send_email()`, `_authenticate()`

## Testing

### Test with Real Data

```bash
# Test reading Excel
python -m evaluationAgent.cli test

# Dry run (preview)
python -m evaluationAgent.cli create-drafts --dry-run

# Create HTML files
python -m evaluationAgent.cli create-drafts

# Review files
ls email_drafts/
cat email_drafts/email_1_grade_100_test_at_example_com.html
```

### Test with Custom Email

```bash
python -m evaluationAgent.cli create-drafts --to your@email.com --verbose
```

### Verify Output

1. **Check email_drafts/ folder** - Verify HTML files created
2. **Open HTML files in browser** - Verify formatting
3. **Check summary.txt** - Verify statistics
4. **Test UTF-8 encoding** - Verify Hebrew characters display correctly

## Troubleshooting

### Issue: No emails created

**Symptoms:** "Emails Created: 0"

**Causes:**
- All students skipped (invalid data)
- No students in Excel file
- Excel file format incorrect

**Solution:**
1. Run `python -m evaluationAgent.cli test` to diagnose
2. Check Excel file has valid students
3. Verify `Status == 'Success'` and `Grade > 0`

### Issue: Gmail API authentication fails

**Symptoms:** "Gmail authentication failed"

**Solution:**
1. Verify credentials.json exists at `~/.gmailagent/credentials.json`
2. Delete `~/.gmailagent/token.json` and re-authenticate
3. Check Google Cloud Console for API errors

### Issue: Hebrew characters broken

**Symptoms:** Garbled Hebrew text in emails

**Solution:**
- Ensure Excel file is UTF-8 encoded
- HTML files use UTF-8: `<meta charset="UTF-8">`
- Already handled by agent, should work automatically

## FAQ

### Q: Do I need Gmail API to use this agent?

**A:** No! By default, the agent saves emails as HTML files. Gmail API is optional for creating drafts in Gmail.

### Q: How do I preview emails before sending?

**A:** Run without `--use-gmail` flag. Emails are saved as HTML files in `email_drafts/` folder. Open them in a browser to preview.

### Q: Can I customize the email template?

**A:** Yes! Edit `evaluationAgent/email_template.py` and modify the `generate_email_html()` function.

### Q: How do I change the instructor name?

**A:** Use `--instructor-name` flag:
```bash
python -m evaluationAgent.cli create-drafts --instructor-name "Prof. Smith"
```

### Q: What happens to students with 0% grade?

**A:** They are automatically skipped. Only students with `Status == 'Success'` and `Grade > 0` receive emails.

### Q: Can I send test emails to myself?

**A:** Yes! Use `--to` flag:
```bash
python -m evaluationAgent.cli create-drafts --to your@email.com
```

### Q: How do I see detailed logs?

**A:** Use `--verbose` flag:
```bash
python -m evaluationAgent.cli create-drafts --verbose
```

## Best Practices

### 1. Always Test First

```bash
# Preview what will happen
python -m evaluationAgent.cli create-drafts --dry-run

# Test with your email
python -m evaluationAgent.cli create-drafts --to your@email.com

# Review HTML files
python -m evaluationAgent.cli create-drafts
```

### 2. Use Safe Mode by Default

Start with HTML files (default), then upgrade to Gmail API when ready:

```bash
# Safe: Create HTML files
python -m evaluationAgent.cli create-drafts

# Review files in browser
open email_drafts/email_1_grade_100_test_at_example_com.html

# When satisfied, use Gmail
python -m evaluationAgent.cli create-drafts --use-gmail
```

### 3. Review Summary

Always check `email_drafts/summary.txt` after running:
- Verify counts (total, created, skipped, failed)
- Check skip reasons
- Review error messages

### 4. Customize Instructor Name

Use your actual name for professional emails:

```bash
python -m evaluationAgent.cli create-drafts --instructor-name "Prof. David Chen"
```

## License

Part of the AI Development Course - Lesson 19 Email Skill Agents.

## Support

For issues, questions, or contributions:
- Check this README
- Review error messages
- Use `--verbose` flag for details
- Run `test` command to diagnose

---

**Evaluation Gmail Sender Agent v1.0.0** - Completing the automated grading workflow!
