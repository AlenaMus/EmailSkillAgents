# GmailAgent - Product Requirements Document

**Version:** 1.0
**Date:** November 21, 2024
**Author:** Product Team
**Status:** Draft

---

## Executive Summary

GmailAgent is a Gmail automation tool that retrieves emails from Gmail using the Gmail API based on specific filters (folder, recipient, subject, tags) and exports them to a structured Excel document. This tool helps users organize, track, and analyze their emails efficiently, particularly useful for extracting URLs and maintaining email databases for business workflows, lead tracking, and email management.

---

## Problem Statement

### Background
Users receive hundreds of emails daily, making it difficult to:
- Track specific emails from particular senders or with certain subjects
- Extract URLs from email bodies for follow-up actions
- Maintain organized records of important emails
- Export email data for reporting or analysis

### User Problem
"I need to extract and organize emails from my Gmail account based on specific criteria (sender, subject, labels) and export them with extracted URLs to Excel for tracking and analysis, but doing this manually is time-consuming and error-prone."

### Business Problem
Manual email management and data extraction is inefficient, leading to:
- Lost productivity (hours spent searching and copying email data)
- Missed opportunities (URLs and action items buried in emails)
- Inconsistent tracking (no standardized format for email records)
- Poor reporting (difficult to analyze email trends and patterns)

---

## Goals & Success Metrics

### Objectives
1. **Primary:** Enable users to automatically retrieve and export Gmail emails to Excel based on filters with 95%+ accuracy
2. **Secondary:** Reduce email data extraction time by 80% compared to manual process
3. **Tertiary:** Extract URLs from email bodies with 90%+ accuracy

### Success Metrics

| Metric | Baseline | Target | Timeline |
|--------|----------|--------|----------|
| Email retrieval accuracy | N/A | 95%+ | Launch |
| URL extraction accuracy | N/A | 90%+ | Launch |
| Time to export 100 emails | 30 min (manual) | <2 min | Launch |
| User satisfaction (CSAT) | N/A | 4.5/5 | Month 1 |
| Daily active users | 0 | 100 | Month 3 |

### Key Performance Indicators (KPIs)
- **Leading Indicators:** Installation rate, first successful export completion rate
- **Lagging Indicators:** Weekly active users, average emails exported per user, user retention

---

## Target Users

### Primary Users
- **Who:** Business professionals, sales teams, marketing professionals, project managers
- **Characteristics:**
  - Receive 50-200 emails per day
  - Need to track emails from specific sources
  - Extract data for reporting or CRM systems
  - Use Gmail as primary email client
- **Pain Points:**
  - Spending 1-2 hours daily on email management
  - Difficulty tracking URLs and links from emails
  - Need structured data for analysis
  - Manual copy-paste is tedious and error-prone

### Secondary Users
- Researchers tracking correspondence
- Customer support teams logging email interactions
- Legal/compliance teams archiving communications
- Freelancers managing client emails

### User Personas

**Sarah - Sales Manager**
- Needs to track emails from prospects with meeting links
- Wants to export calendar invites and Zoom links
- Uses Gmail labels to organize leads
- Requires Excel export for CRM import

**Mike - Project Manager**
- Tracks project-related emails by client name
- Extracts document URLs and file links
- Needs date-sorted email logs
- Shares reports with team in Excel

---

## Scope

### In Scope (v1.0)
- Gmail API integration with OAuth 2.0 authentication
- Email retrieval with filters:
  - By Gmail folder
  - By Gmail label
  - By Gmail tag
  - By recipient name (from/to)
  - By email subject (contains text)
- Organized export folder structure:
  - Auto-create `./exports/` directory
  - Store all Excel files in exports folder
- Smart Excel filename generation:
  - Auto-generated filename based on filters used
  - Format: `DD.MM.YYYY_HHMMSS_mails_<filter_description>.xlsx`
  - Examples:
    - `22.11.2024_143022_mails_by_tag_Important.xlsx`
    - `22.11.2024_143022_mails_from_folder_Work.xlsx`
    - `22.11.2024_143530_mails_by_tag_Work_from_sender_john@example.com.xlsx`
  - Optional custom output path override
- Excel export with 4 columns:
  - Auto-generated unique ID (UUID)
  - Email date/timestamp (YYYY-MM-DD HH:MM:SS format)
  - Email subject
  - Extracted URL(s) from email body (comma-separated if multiple)
- Support for multiple URL extraction from single email
- URL extraction from both plain text and HTML emails
- Basic error handling and logging
- Command-line interface (CLI) with helpful output messages
- Configuration file for API credentials

### Out of Scope (Future Considerations)
- Email sending capabilities
- Attachment download
- Email body text export (full content)
- GUI/web interface
- Scheduled/automated runs
- Multiple Gmail account support
- Email filtering by date range
- Advanced analytics or visualization
- Email response/reply functionality
- Integration with CRM systems

### MVP Definition
Minimum viable version includes:
- Gmail API authentication
- Filter by at least one criterion (folder, recipient, or subject)
- Export to Excel with all 4 columns
- Extract first URL from email body
- Handle up to 100 emails per export

---

## User Stories

### Core User Flows

**User Story 1: Authentication and Setup**
```
As a user
I want to authenticate GmailAgent with my Gmail account
So that the tool can access my emails securely

Acceptance Criteria:
- [ ] Given I run the setup command, when I follow the OAuth flow, then I'm redirected to Google login
- [ ] Given I authorize the app, when authentication completes, then credentials are saved locally
- [ ] Given credentials exist, when I run the tool again, then I'm not prompted to re-authenticate
- [ ] Given credentials are invalid, when I run the tool, then I receive a clear error message to re-authenticate

Priority: High
Estimated Effort: 5 story points
```

**User Story 2: Filter Emails by Recipient**
```
As a user
I want to retrieve emails from a specific sender
So that I can export all emails from a particular person or company

Acceptance Criteria:
- [ ] Given I specify a sender email, when I run the tool, then only emails from that sender are retrieved
- [ ] Given I specify a sender name (partial), when I run the tool, then emails matching that name are retrieved
- [ ] Given sender doesn't exist, when I run the tool, then I get a message "0 emails found"
- [ ] Given multiple matching emails, when I run the tool, then all matching emails are included

Priority: High
Estimated Effort: 3 story points
```

**User Story 3: Filter by Gmail Label/Folder**
```
As a user
I want to retrieve emails from a specific Gmail label
So that I can export organized sets of emails

Acceptance Criteria:
- [ ] Given I specify a label name, when I run the tool, then only emails with that label are retrieved
- [ ] Given label doesn't exist, when I run the tool, then I get an error message with available labels
- [ ] Given nested labels, when I specify parent label, then child label emails are also included
- [ ] Given an email has multiple labels, when any match my filter, then the email is included

Priority: High
Estimated Effort: 3 story points
```

**User Story 4: Filter by Subject**
```
As a user
I want to retrieve emails with specific text in the subject
So that I can export emails about particular topics

Acceptance Criteria:
- [ ] Given I specify subject text, when I run the tool, then emails containing that text (case-insensitive) are retrieved
- [ ] Given partial subject match, when I run the tool, then emails with partial matches are included
- [ ] Given multiple search terms, when I run the tool, then emails matching any term are retrieved
- [ ] Given no matches, when I run the tool, then I get "0 emails found" message

Priority: High
Estimated Effort: 2 story points
```

**User Story 5: Export to Excel**
```
As a user
I want to export filtered emails to an Excel file
So that I can analyze and share the data

Acceptance Criteria:
- [ ] Given emails are retrieved, when export runs, then an Excel file is created with .xlsx extension
- [ ] Given the export, when I open the file, then I see 4 columns: ID, Date, Subject, URL
- [ ] Given the export, when I check IDs, then each row has a unique ID (e.g., UUID or sequential)
- [ ] Given the export, when I check dates, then they're formatted as YYYY-MM-DD HH:MM:SS
- [ ] Given the export, when I check subjects, then they match the original email subjects exactly
- [ ] Given multiple emails, when I open Excel, then rows are sorted by date (newest first)

Priority: High
Estimated Effort: 5 story points
```

**User Story 6: Extract URLs from Email Body**
```
As a user
I want URLs extracted from email bodies automatically
So that I can quickly access links without opening each email

Acceptance Criteria:
- [ ] Given an email with one URL, when exported, then the URL appears in the URL column
- [ ] Given an email with multiple URLs, when exported, then all URLs are in the URL column (comma-separated or first URL only)
- [ ] Given an email with no URLs, when exported, then the URL column is empty for that row
- [ ] Given URLs in various formats (http, https, shortened), when exported, then all are correctly extracted
- [ ] Given URLs in HTML links, when exported, then the actual URL is extracted (not display text)

Priority: High
Estimated Effort: 5 story points
```

### Edge Cases & Error Handling

**Edge Case 1:** No internet connection
- **Expected behavior:** Display error "No internet connection. Please check your network and try again."

**Edge Case 2:** API rate limit exceeded
- **Expected behavior:** Display warning "Gmail API rate limit exceeded. Please try again in X minutes."

**Edge Case 3:** Large number of emails (>1000)
- **Expected behavior:** Display warning "Found 1000+ emails. Processing first 1000. Use additional filters to narrow results."

**Error State 1:** Invalid Gmail label specified
- **Expected behavior:** "Label 'xyz' not found. Available labels: [list]"

**Error State 2:** Gmail API credentials expired
- **Expected behavior:** "Authentication expired. Run 'gmailagent auth' to re-authenticate."

**Error State 3:** Excel file already exists
- **Expected behavior:** Prompt "File exists. Overwrite? (y/n)" or auto-append timestamp to filename

---

## Functional Requirements

### Feature 1: Gmail API Authentication

**Description:**
Secure OAuth 2.0 authentication with Gmail API to access user's email data.

**User Interface:**
- Command: `gmailagent auth`
- Opens browser for Google OAuth consent
- Saves credentials to `~/.gmailagent/credentials.json`

**Business Logic:**
- Use OAuth 2.0 with readonly scope: `https://www.googleapis.com/auth/gmail.readonly`
- Store refresh token for persistent access
- Validate credentials before each API call

**Data Requirements:**
- Input: Gmail API client ID and client secret (from config)
- Processing: OAuth flow, token exchange
- Output: Saved credentials file

### Feature 2: Email Retrieval with Filters

**Description:**
Query Gmail API to retrieve emails based on user-specified filters.

**User Interface:**
```bash
gmailagent export \
  --folder "Important" \
  --from "sender@example.com" \
  --subject "invoice" \
  --label "work" \
  --output "emails.xlsx"
```

**Business Logic:**
- Build Gmail API query from filters
- Support AND logic (all filters must match)
- Retrieve email metadata: id, date, from, to, subject, body
- Limit results to 1000 emails (configurable)

**Data Requirements:**
- Input: Filter parameters (folder, from, subject, label)
- Processing: Gmail API search query, pagination handling
- Output: List of email objects

### Feature 3: URL Extraction

**Description:**
Parse email body (plain text and HTML) to extract all URLs.

**User Interface:**
- Automatic during export process
- No user interaction required

**Business Logic:**
- Use regex to find URLs: `http(s)?://[^\s]+`
- Parse HTML emails to extract href attributes from `<a>` tags
- Handle both plain text and HTML email formats
- Store multiple URLs as comma-separated values (or first URL only)

**Data Requirements:**
- Input: Email body (plain text or HTML)
- Processing: Regex matching, HTML parsing
- Output: String of URLs (comma-separated) or empty string

### Feature 4: Excel Export with Smart Naming

**Description:**
Generate Excel (.xlsx) file with structured email data and save to organized folder with intelligent filename based on filters used.

**User Interface:**
- Output folder: `./exports/` (auto-created if doesn't exist)
- Filename format: `DD.MM.YYYY_HHMMSS_mails_<filter_description>.xlsx`
- Custom output path via `--output` flag (optional override)

**Filename Examples:**
- By tag: `22.11.2024_143022_mails_by_tag_Important.xlsx`
- By folder: `22.11.2024_143022_mails_from_folder_Work.xlsx`
- By sender: `22.11.2024_143022_mails_from_sender_john@example.com.xlsx`
- By subject: `22.11.2024_143022_mails_by_subject_invoice.xlsx`
- Multiple filters: `22.11.2024_143022_mails_by_tag_Work_from_sender_boss@company.com.xlsx`

**Business Logic:**
- Create `./exports/` directory if it doesn't exist
- Generate filename from active filters:
  - Format: `{date}_{time}_mails_{filter_type}_{filter_value}.xlsx`
  - Date format: `DD.MM.YYYY`
  - Time format: `HHMMSS` (24-hour)
  - Sanitize filter values (remove special characters, limit length)
  - Multiple filters: concatenate with underscores
- Create Excel workbook with single sheet "Emails"
- Add header row: "ID", "Date", "Subject", "URL"
- Populate rows with email data
- Auto-size columns for readability
- Format date column as datetime
- Display saved location to user: "Exported X emails to: exports/22.11.2024_143022_mails_by_tag_Important.xlsx"

**Data Requirements:**
- Input: List of email objects with extracted URLs + active filters
- Processing: Excel file creation using openpyxl, filename generation from filters
- Output: .xlsx file saved to `./exports/` directory

**Excel Structure:**
```
| ID | Date | Subject | URL |
|----|------|---------|-----|
| 1 | 2024-11-21 09:30:00 | Meeting Invitation | https://zoom.us/j/123456 |
| 2 | 2024-11-21 08:15:00 | Invoice #1234 | https://example.com/invoice |
| 3 | 2024-11-20 16:45:00 | Project Update | |
```

---

## Non-Functional Requirements

### Performance
- Email retrieval: Process 100 emails in < 30 seconds
- URL extraction: < 1 second per email
- Excel generation: < 5 seconds for 100 emails
- Total end-to-end time: < 2 minutes for 100 emails

### Security
- OAuth 2.0 authentication (never store plain passwords)
- Credentials stored in secure local file with restricted permissions (600)
- Use readonly Gmail API scope (no modification permissions)
- No logging of sensitive email content
- Clear documentation on data privacy

### Reliability
- Handle API rate limits gracefully (retry with exponential backoff)
- Validate API responses before processing
- Graceful error handling with user-friendly messages
- Log errors to `~/.gmailagent/error.log` for debugging

### Usability
- Clear command-line help: `gmailagent --help`
- Informative progress indicators ("Processing 50/100 emails...")
- Validation of user inputs with helpful error messages
- Example commands in documentation

### Compatibility
- Python 3.8+ required
- Cross-platform: Windows, macOS, Linux
- Gmail API v1
- Excel format: .xlsx (Excel 2007+)

### Maintainability
- Modular code structure (separate modules for auth, api, parsing, export)
- Comprehensive error handling
- Unit tests for core functions (>80% coverage)
- Clear code documentation and docstrings

---

## User Experience (UX)

### Command-Line Interface

**Installation:**
```bash
pip install gmailagent
gmailagent auth  # First-time setup
```

**Basic Usage:**
```bash
# Export all emails from a label (auto-named: exports/22.11.2024_143022_mails_by_label_Work.xlsx)
gmailagent export --label "Work"
# Output: Exported 45 emails to: exports/22.11.2024_143022_mails_by_label_Work.xlsx

# Export emails from specific sender (auto-named with sender)
gmailagent export --from "boss@company.com"
# Output: Exported 23 emails to: exports/22.11.2024_143530_mails_from_sender_boss@company.com.xlsx

# Export emails with subject containing "invoice" (auto-named with subject)
gmailagent export --subject "invoice"
# Output: Exported 12 emails to: exports/22.11.2024_144015_mails_by_subject_invoice.xlsx

# Export from Gmail folder (auto-named with folder name)
gmailagent export --folder "Important"
# Output: Exported 67 emails to: exports/22.11.2024_144522_mails_from_folder_Important.xlsx

# Export by tag (auto-named with tag)
gmailagent export --tag "clients"
# Output: Exported 89 emails to: exports/22.11.2024_145033_mails_by_tag_clients.xlsx

# Combine filters (auto-named with all filters)
gmailagent export --label "Important" --from "client@example.com"
# Output: Exported 8 emails to: exports/22.11.2024_145522_mails_by_label_Important_from_sender_client@example.com.xlsx

# Custom output path (override auto-naming)
gmailagent export --label "Work" --output "custom_export.xlsx"
# Output: Exported 45 emails to: custom_export.xlsx
```

**Help Output:**
```bash
$ gmailagent --help

GmailAgent - Gmail Email Exporter

Commands:
  auth              Authenticate with Gmail API
  export            Export emails to Excel
  list-labels       List all available Gmail labels
  list-folders      List all available Gmail folders

Export Options:
  --label TEXT      Filter by Gmail label
  --folder TEXT     Filter by Gmail folder name
  --tag TEXT        Filter by Gmail tag
  --from TEXT       Filter by sender email or name
  --to TEXT         Filter by recipient email or name
  --subject TEXT    Filter by subject (contains text)
  --output PATH     Custom output file path (default: auto-generated in ./exports/)
                    Auto-naming format: DD.MM.YYYY_HHMMSS_mails_<filter_description>.xlsx
  --limit INT       Maximum emails to retrieve (default: 1000)
  --help            Show this message and exit

Examples:
  gmailagent export --label "Work"
  gmailagent export --folder "Important"
  gmailagent export --tag "clients"
  gmailagent export --from "boss@company.com"
  gmailagent export --subject "invoice"
  gmailagent export --label "Work" --from "john@example.com"

Output:
  All exports are saved to ./exports/ directory with smart filenames
  Example: exports/22.11.2024_143022_mails_by_tag_Important.xlsx
```

### User Flow Diagram

```
Start
  ↓
[First Time?] ——Yes——> [Run: gmailagent auth]
  ↓                           ↓
  No                    [OAuth Flow]
  ↓                           ↓
[Run: gmailagent export]  [Save Credentials]
  ↓                           ↓
[Specify Filters] <———————————┘
  ↓
[Create ./exports/ folder if not exists]
  ↓
[Generate smart filename from filters]
  (e.g., 22.11.2024_143022_mails_by_tag_Work.xlsx)
  ↓
[Retrieve Emails from Gmail API]
  ↓
[Extract URLs from Email Bodies]
  ↓
[Generate Excel File in ./exports/]
  ↓
[Display: "Exported X emails to: exports/22.11.2024_143022_mails_by_tag_Work.xlsx"]
  ↓
End
```

---

## Technical Design

### Architecture Overview

```
┌─────────────────┐
│   User (CLI)    │
└────────┬────────┘
         │
    ┌────▼────┐
    │  Main   │
    │ Controller│
    └────┬────┘
         │
    ┌────▼──────────────────────┐
    │                            │
┌───▼────┐  ┌─────▼─────┐  ┌───▼─────┐
│  Auth  │  │Gmail API  │  │ Export  │
│ Module │  │  Module   │  │ Module  │
└────┬───┘  └─────┬─────┘  └────┬────┘
     │            │              │
     │       ┌────▼────┐    ┌────▼────┐
     │       │  URL    │    │ Excel   │
     │       │Extractor│    │Generator│
     │       └─────────┘    └─────────┘
     │
┌────▼─────────┐
│Gmail API v1  │
└──────────────┘
```

### Technology Stack

**Language:** Python 3.8+

**Key Libraries:**
- `google-auth-oauthlib` - OAuth 2.0 authentication
- `google-api-python-client` - Gmail API client
- `openpyxl` - Excel file generation
- `beautifulsoup4` - HTML parsing for URL extraction
- `click` or `argparse` - CLI interface
- `python-dotenv` - Configuration management

### API Endpoints

**Gmail API Usage:**

1. **Authentication:**
   - Endpoint: OAuth 2.0 flow
   - Scope: `https://www.googleapis.com/auth/gmail.readonly`

2. **List Labels:**
   - Method: `users.labels.list`
   - Purpose: Get available Gmail labels

3. **Search Messages:**
   - Method: `users.messages.list`
   - Query: Build from filters (e.g., `from:sender@example.com label:important`)
   - Response: List of message IDs

4. **Get Message:**
   - Method: `users.messages.get`
   - Purpose: Retrieve full message details (headers, body)
   - Format: `full` (includes body)

### Database Schema

**No Database Required** - This is a stateless CLI tool.

Optional: Configuration file (`~/.gmailagent/config.yaml`)
```yaml
gmail_api:
  client_id: "your-client-id"
  client_secret: "your-client-secret"

export:
  default_limit: 1000
  date_format: "%Y-%m-%d %H:%M:%S"

output:
  default_filename: "gmail_export_{timestamp}.xlsx"
  default_directory: "./exports"
```

### URL Extraction Logic

**Regex Pattern:**
```python
# Simple URL pattern
r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)'

# Or use existing library
import re
from urllib.parse import urlparse

def extract_urls(text):
    """Extract all URLs from text"""
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.findall(url_pattern, text)
```

**HTML Parsing:**
```python
from bs4 import BeautifulSoup

def extract_urls_from_html(html):
    """Extract URLs from HTML email body"""
    soup = BeautifulSoup(html, 'html.parser')
    urls = []
    for link in soup.find_all('a', href=True):
        urls.append(link['href'])
    return urls
```

### Smart Filename Generation

```python
import os
import re
from datetime import datetime

def generate_filename(filters):
    """Generate smart filename based on active filters"""
    # Get current date and time
    now = datetime.now()
    date_str = now.strftime("%d.%m.%Y")  # DD.MM.YYYY
    time_str = now.strftime("%H%M%S")    # HHMMSS

    # Build filter description
    filter_parts = []

    if filters.get('label'):
        label = sanitize_filename(filters['label'])
        filter_parts.append(f"by_label_{label}")

    if filters.get('folder'):
        folder = sanitize_filename(filters['folder'])
        filter_parts.append(f"from_folder_{folder}")

    if filters.get('tag'):
        tag = sanitize_filename(filters['tag'])
        filter_parts.append(f"by_tag_{tag}")

    if filters.get('from'):
        sender = sanitize_filename(filters['from'])
        filter_parts.append(f"from_sender_{sender}")

    if filters.get('to'):
        recipient = sanitize_filename(filters['to'])
        filter_parts.append(f"to_recipient_{recipient}")

    if filters.get('subject'):
        subject = sanitize_filename(filters['subject'])
        filter_parts.append(f"by_subject_{subject}")

    # Combine all parts
    if not filter_parts:
        filter_parts = ["all_mails"]

    filter_desc = "_".join(filter_parts)

    # Generate filename
    filename = f"{date_str}_{time_str}_mails_{filter_desc}.xlsx"

    return filename

def sanitize_filename(text, max_length=50):
    """Remove special characters and limit length for filename"""
    # Remove or replace special characters
    text = re.sub(r'[<>:"/\\|?*@]', '_', text)
    # Replace spaces with underscores
    text = text.replace(' ', '_')
    # Remove multiple underscores
    text = re.sub(r'_+', '_', text)
    # Limit length
    if len(text) > max_length:
        text = text[:max_length]
    # Remove trailing underscores
    text = text.strip('_')
    return text

def ensure_exports_folder():
    """Create exports folder if it doesn't exist"""
    exports_dir = "./exports"
    if not os.path.exists(exports_dir):
        os.makedirs(exports_dir)
    return exports_dir

# Usage example
filters = {
    'tag': 'Important',
    'from': 'boss@company.com'
}

exports_dir = ensure_exports_folder()
filename = generate_filename(filters)
output_path = os.path.join(exports_dir, filename)
# Result: ./exports/22.11.2024_143022_mails_by_tag_Important_from_sender_boss@company.com.xlsx
```

### Excel Generation

```python
from openpyxl import Workbook
from openpyxl.styles import Font
import uuid
from datetime import datetime

def create_excel(emails, output_path):
    """Generate Excel file from email data"""
    wb = Workbook()
    ws = wb.active
    ws.title = "Emails"

    # Header row
    headers = ["ID", "Date", "Subject", "URL"]
    ws.append(headers)

    # Style header
    for cell in ws[1]:
        cell.font = Font(bold=True)

    # Data rows
    for email in emails:
        row = [
            str(uuid.uuid4()),  # Unique ID
            email['date'].strftime("%Y-%m-%d %H:%M:%S"),
            email['subject'],
            ", ".join(email['urls']) if email['urls'] else ""
        ]
        ws.append(row)

    # Auto-adjust column widths
    for column in ws.columns:
        max_length = 0
        column = [cell for cell in column]
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column[0].column_letter].width = adjusted_width

    wb.save(output_path)
```

---

## Implementation Plan

### Development Phases

**Phase 1: Foundation (Sprint 1 - Week 1-2)**
- Set up project structure and dependencies
- Implement OAuth 2.0 authentication module
- Create Gmail API client wrapper
- Basic CLI interface with auth command
- **Deliverable:** Working authentication flow

**Phase 2: Core Features (Sprint 2 - Week 3-4)**
- Implement email retrieval with filters
  - Filter by label
  - Filter by sender (from)
  - Filter by subject
- Build URL extraction module (regex + HTML parsing)
- **Deliverable:** Email retrieval and URL extraction working

**Phase 3: Export & Polish (Sprint 3 - Week 5-6)**
- Implement Excel generation
- Add error handling and logging
- Progress indicators and user feedback
- Documentation and help text
- **Deliverable:** Complete working tool

**Phase 4: Testing & Launch (Sprint 4 - Week 7-8)**
- Unit tests (>80% coverage)
- Integration tests with Gmail API
- User acceptance testing
- Documentation and README
- Package for distribution (PyPI)
- **Deliverable:** Production-ready release v1.0

### Timeline

| Milestone | Date | Owner | Deliverable |
|-----------|------|-------|-------------|
| Project kickoff | Week 1 | Tech Lead | Project setup complete |
| Authentication complete | Week 2 | Backend Dev | OAuth working |
| Email retrieval complete | Week 4 | Backend Dev | All filters working |
| URL extraction complete | Week 5 | Backend Dev | URLs extracted accurately |
| Excel export complete | Week 6 | Backend Dev | Excel files generated |
| Testing complete | Week 7 | QA | All tests passing |
| Documentation complete | Week 8 | Tech Writer | README and docs ready |
| **v1.0 Launch** | **Week 8** | **PM** | **Public release** |

---

## Testing Plan

### Test Scenarios

**1. Authentication Tests**
- Scenario: First-time auth flow completes successfully
- Scenario: Re-authentication when credentials expire
- Scenario: Invalid credentials show error message
- Expected: OAuth flow works, credentials saved securely

**2. Email Retrieval Tests**
- Scenario: Filter by label returns correct emails
- Scenario: Filter by sender returns correct emails
- Scenario: Filter by subject returns correct emails
- Scenario: Combined filters work with AND logic
- Scenario: No matching emails returns empty result
- Expected: Correct emails retrieved for all filter combinations

**3. URL Extraction Tests**
- Scenario: Single URL in plain text email extracted
- Scenario: Multiple URLs in HTML email extracted
- Scenario: No URLs returns empty URL column
- Scenario: Malformed URLs handled gracefully
- Expected: 90%+ URL extraction accuracy

**4. Excel Export Tests**
- Scenario: Excel file created with correct columns
- Scenario: Data populated correctly in all rows
- Scenario: Unique IDs generated for each row
- Scenario: Dates formatted correctly
- Scenario: File overwrites handled properly
- Expected: Valid Excel file with all data

**5. Error Handling Tests**
- Scenario: No internet connection shows error
- Scenario: API rate limit shows appropriate message
- Scenario: Invalid label shows available labels
- Scenario: Large result set (>1000) shows warning
- Expected: User-friendly error messages

### QA Requirements

**Unit Tests:**
- Auth module: Credential storage, token refresh
- API module: Query building, response parsing
- URL extraction: Regex matching, HTML parsing
- Excel module: File generation, formatting
- Target: >80% code coverage

**Integration Tests:**
- End-to-end: Auth → Retrieve → Extract → Export
- Gmail API integration (use test account)
- File system operations

**Manual Testing:**
- Install on fresh machine
- Follow user documentation
- Test with real Gmail account (various email types)
- Verify Excel output in Microsoft Excel and Google Sheets

**Performance Testing:**
- Test with 10, 100, 1000 emails
- Measure execution time
- Monitor memory usage
- Test API rate limit handling

---

## Launch Plan

### Go-to-Market Strategy

**Target Audience:**
- Developers and tech-savvy professionals
- Sales and marketing teams using Gmail
- Small business owners

**Distribution Channels:**
- PyPI (Python Package Index)
- GitHub repository
- Product Hunt launch
- Hacker News post
- Dev.to article

### Launch Checklist

**Pre-Launch (Week 7):**
- [ ] All features complete and tested
- [ ] Documentation complete (README, API docs)
- [ ] Example usage videos/GIFs created
- [ ] PyPI package prepared
- [ ] GitHub repository public
- [ ] Product Hunt listing drafted

**Launch Week (Week 8):**
- [ ] Publish to PyPI
- [ ] GitHub repository live
- [ ] Product Hunt launch
- [ ] Post on Hacker News
- [ ] Share on Twitter/LinkedIn
- [ ] Blog post/tutorial published

**Post-Launch (Week 9-12):**
- [ ] Monitor user feedback (GitHub issues)
- [ ] Track installation metrics
- [ ] Address critical bugs within 24 hours
- [ ] Gather feature requests
- [ ] Plan v1.1 based on feedback

### Rollout Strategy

**Approach:** Public open-source release (Big Bang)

**Phases:**
1. **Alpha (Week 6):** Internal testing with team (5 users)
2. **Beta (Week 7):** Invite 20 users from network for feedback
3. **Launch (Week 8):** Public release on PyPI and GitHub

**Monitoring:**
- GitHub stars and forks
- PyPI download statistics
- GitHub issues and feedback
- User testimonials and reviews

---

## Risks & Mitigation

| Risk | Probability | Impact | Mitigation Strategy | Owner |
|------|-------------|--------|---------------------|-------|
| Gmail API rate limits hit | High | Medium | Implement exponential backoff, document limits, add rate limit warnings | Backend Dev |
| URL extraction accuracy <90% | Medium | Medium | Extensive testing, support multiple regex patterns, HTML parser fallback | Backend Dev |
| OAuth flow confusing for users | Medium | High | Clear documentation with screenshots, video tutorial, example workflow | Tech Writer |
| Excel file corruption with large datasets | Low | High | Test with datasets up to 10,000 emails, implement batch export if needed | Backend Dev |
| Security concerns with credential storage | Low | Critical | Use OS keyring for credential storage, clear security documentation | Backend Dev |
| Gmail API access denied | Low | Critical | Clear instructions for API setup, troubleshooting guide | Tech Writer |

---

## Dependencies

### Internal Dependencies
- Python development environment
- Gmail API credentials (client ID, secret)
- Testing Gmail account with sample emails

### External Dependencies
- Google Cloud Platform account (for Gmail API)
- Gmail API enabled
- PyPI account (for package distribution)
- GitHub account (for repository)

---

## Assumptions & Constraints

### Assumptions
- Users have Gmail accounts (not GSuite with restricted API access)
- Users can access Google Cloud Console to create API credentials
- Users have Python 3.8+ installed
- Users understand basic command-line usage
- Emails don't exceed Gmail API quotas (1 billion quota units/day)

### Constraints
- **Budget:** $0 (open-source project, free Gmail API tier)
- **Timeline:** 8 weeks to v1.0
- **Resources:** 1 backend developer, 1 QA, 1 PM
- **Technical:**
  - Gmail API readonly scope only
  - Python-only (no cross-language support)
  - Command-line only (no GUI in v1.0)
  - Excel format only (no CSV in v1.0)

---

## Open Questions

- [ ] **Multiple URLs:** Should we export all URLs (comma-separated) or just the first URL?
  - **Owner:** PM
  - **Due:** Week 2
  - **Decision:** Export all URLs comma-separated; add config option to limit to first URL only

- [ ] **Date range filtering:** Should v1.0 include date range filter (after/before date)?
  - **Owner:** PM
  - **Due:** Week 1
  - **Decision:** Defer to v1.1; prioritize other filters for v1.0

- [ ] **Duplicate emails:** How to handle same email in multiple labels?
  - **Owner:** Backend Dev
  - **Due:** Week 3
  - **Decision:** Include once with first label found

- [ ] **Attachment URLs:** Should we extract URLs from attachments?
  - **Owner:** PM
  - **Due:** Week 2
  - **Decision:** No, out of scope for v1.0; body text only

---

## Appendix

### References
- Gmail API Documentation: https://developers.google.com/gmail/api
- OAuth 2.0 for Python: https://google-auth.readthedocs.io/
- openpyxl Documentation: https://openpyxl.readthedocs.io/

### Glossary
- **Gmail API:** Google's RESTful API for accessing Gmail
- **OAuth 2.0:** Authorization framework for secure API access
- **Label:** Gmail's organizational system (similar to folders)
- **MIME:** Email format standard (for parsing email structure)

### Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-11-21 | Product Team | Initial draft |

---

**Next Steps:**
1. Review and approve PRD
2. Tech lead reviews technical feasibility
3. Create detailed implementation tasks
4. Begin Sprint 1 development

