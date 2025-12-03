# GmailAgent

**Version:** 1.0.0

GmailAgent is a Gmail automation tool that retrieves emails from Gmail using the Gmail API based on specific filters (folder, recipient, subject, tags) and exports them to a structured Excel document with automatic URL extraction.

## Features

- **Gmail API Integration**: Secure OAuth 2.0 authentication with readonly access
- **Flexible Filtering**: Filter emails by folder, label, tag, sender, recipient, or subject
- **URL Extraction**: Automatically extract URLs from both plain text and HTML email bodies
- **Smart Filename Generation**: Auto-generated filenames based on active filters
  - Format: `DD.MM.YYYY_HHMMSS_mails_<filter_description>.xlsx`
  - Example: `22.11.2024_143022_mails_by_tag_Important_from_sender_boss@company.com.xlsx`
- **Organized Exports**: All exports saved to `./exports/` directory (auto-created)
- **Excel Export**: Professional Excel format with 4 columns:
  - ID (UUID)
  - Date (YYYY-MM-DD HH:MM:SS)
  - Subject
  - URL (comma-separated if multiple)
- **Progress Indicators**: Real-time feedback during email retrieval
- **Error Handling**: Comprehensive error handling with clear user messages

## Installation

### Prerequisites

- Python 3.8 or higher
- Gmail account
- Google Cloud Console project with Gmail API enabled

### Install from source

```bash
# Clone the repository
git clone https://github.com/yourusername/gmailagent.git
cd gmailagent

# Install dependencies
pip install -r requirements.txt

# Install package
pip install -e .
```

### Install from PyPI (once published)

```bash
pip install gmailagent
```

## Setup

### 1. Enable Gmail API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gmail API for your project
4. Create OAuth 2.0 credentials (Desktop application type)
5. Download the credentials JSON file

### 2. Authenticate GmailAgent

```bash
# Copy your downloaded credentials file to the default location
gmailagent auth --credentials /path/to/downloaded/credentials.json

# Or place credentials.json in ~/.gmailagent/credentials.json and run:
gmailagent auth
```

A browser window will open for you to authorize the application. After authorization, your credentials will be saved securely for future use.

## Usage

### Basic Commands

```bash
# Authenticate with Gmail API
gmailagent auth

# Export emails (basic examples)
gmailagent export --label "Work"
gmailagent export --folder "INBOX"
gmailagent export --from "boss@company.com"
gmailagent export --subject "invoice"
gmailagent export --tag "clients"

# List available Gmail labels
gmailagent list-labels

# List common Gmail folders
gmailagent list-folders

# Check authentication status
gmailagent info

# Revoke authentication
gmailagent revoke

# Help
gmailagent --help
```

### Filter Options

| Option | Description | Example |
|--------|-------------|---------|
| `--folder` | Gmail folder (INBOX, SENT, IMPORTANT, etc.) | `--folder "INBOX"` |
| `--label` | Gmail label name | `--label "Work"` |
| `--tag` | Gmail tag (synonym for label) | `--tag "Important"` |
| `--from` | Sender email or name | `--from "boss@company.com"` |
| `--to` | Recipient email or name | `--to "client@example.com"` |
| `--subject` | Subject text (contains) | `--subject "invoice"` |
| `--output` | Custom output path (overrides auto-naming) | `--output "custom.xlsx"` |
| `--limit` | Maximum emails to retrieve (default: 1000) | `--limit 500` |

### Advanced Examples

#### Export emails from specific label
```bash
gmailagent export --label "Work"
# Output: exports/22.11.2024_143022_mails_by_label_Work.xlsx
```

#### Export emails from specific sender
```bash
gmailagent export --from "boss@company.com"
# Output: exports/22.11.2024_143530_mails_from_sender_boss@company.com.xlsx
```

#### Export emails with subject containing specific text
```bash
gmailagent export --subject "invoice"
# Output: exports/22.11.2024_144015_mails_by_subject_invoice.xlsx
```

#### Combine multiple filters
```bash
gmailagent export --label "Important" --from "client@example.com" --subject "meeting"
# Output: exports/22.11.2024_145522_mails_by_label_Important_from_sender_client@example.com_by_subject_meeting.xlsx
```

#### Export from Gmail folder
```bash
gmailagent export --folder "SENT"
# Output: exports/22.11.2024_144522_mails_from_folder_SENT.xlsx
```

#### Custom output path
```bash
gmailagent export --label "Work" --output "/path/to/custom_export.xlsx"
# Output: /path/to/custom_export.xlsx
```

#### Limit number of emails
```bash
gmailagent export --label "Work" --limit 100
# Exports maximum 100 emails
```

## Output Format

### Excel File Structure

All Excel files contain 4 columns:

| Column | Description | Example |
|--------|-------------|---------|
| **ID** | Unique identifier (UUID) | `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |
| **Date** | Email date/timestamp | `2024-11-21 09:30:00` |
| **Subject** | Email subject line | `Meeting Invitation` |
| **URL** | Extracted URLs (comma-separated) | `https://zoom.us/j/123456, https://docs.google.com/...` |

### Filename Format

Auto-generated filenames follow this pattern:

```
DD.MM.YYYY_HHMMSS_mails_<filter_description>.xlsx
```

Examples:
- `22.11.2024_143022_mails_by_tag_Important.xlsx`
- `22.11.2024_143022_mails_from_folder_Work.xlsx`
- `22.11.2024_143530_mails_from_sender_john@example.com.xlsx`
- `22.11.2024_143530_mails_by_tag_Work_from_sender_boss@company.com.xlsx`

### Exports Directory

All exports are saved to `./exports/` directory by default. The directory is automatically created if it doesn't exist.

## Configuration

Optional configuration file: `~/.gmailagent/config.yaml`

Copy the example configuration:

```bash
cp config.yaml.example ~/.gmailagent/config.yaml
```

See `config.yaml.example` for available configuration options.

## Project Structure

```
gmailagent/
├── gmailagent/
│   ├── __init__.py          # Package initialization
│   ├── auth.py              # OAuth 2.0 authentication
│   ├── gmail_client.py      # Gmail API wrapper
│   ├── url_extractor.py     # URL extraction logic
│   ├── excel_exporter.py    # Excel generation with smart naming
│   └── cli.py               # Command-line interface
├── exports/                 # Output directory (auto-created)
├── setup.py                 # Package setup
├── requirements.txt         # Python dependencies
├── config.yaml.example      # Example configuration
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## API Documentation

### Authentication

```python
from gmailagent import GmailAuthenticator

# Initialize authenticator
auth = GmailAuthenticator()

# Authenticate and get Gmail service
service = auth.get_service()

# Check if authenticated
if auth.is_authenticated():
    print("Authenticated!")
```

### Email Retrieval

```python
from gmailagent import GmailClient

# Initialize client
client = GmailClient(service)

# Retrieve emails with filters
emails = client.retrieve_emails(
    label="Work",
    from_email="boss@company.com",
    subject="invoice",
    max_results=100
)
```

### URL Extraction

```python
from gmailagent import extract_urls_from_emails

# Extract URLs from emails
emails = extract_urls_from_emails(emails)

# Each email now has 'urls' field
for email in emails:
    print(f"Subject: {email['subject']}")
    print(f"URLs: {email['urls']}")
```

### Excel Export

```python
from gmailagent import export_emails_to_excel

# Export to Excel with smart naming
output_file = export_emails_to_excel(
    emails=emails,
    filters={'label': 'Work', 'from': 'boss@company.com'}
)

print(f"Exported to: {output_file}")
```

## Troubleshooting

### Authentication Issues

**Problem:** "Credentials file not found"

**Solution:**
1. Download OAuth credentials from Google Cloud Console
2. Run: `gmailagent auth --credentials /path/to/credentials.json`

**Problem:** "Authentication expired"

**Solution:** Run `gmailagent auth` to re-authenticate

### No Emails Found

**Problem:** "No emails found matching the specified filters"

**Solutions:**
- Check if filters are correct (case-sensitive for labels)
- Use `gmailagent list-labels` to see available labels
- Try broader filters or remove some filters

### API Rate Limits

**Problem:** "Gmail API rate limit exceeded"

**Solution:**
- Wait a few minutes before trying again
- Reduce the number of emails using `--limit`
- Gmail API quota: 1 billion quota units/day (default)

### Import Errors

**Problem:** "ModuleNotFoundError"

**Solution:**
```bash
pip install -r requirements.txt
```

## Security

- **OAuth 2.0**: Secure authentication without storing passwords
- **Readonly Access**: Uses `gmail.readonly` scope - cannot modify emails
- **Credential Storage**: Credentials stored locally in `~/.gmailagent/` with restricted permissions
- **No Data Transmission**: All processing is local - no data sent to third parties

## Performance

- **100 emails**: ~30 seconds (typical)
- **1000 emails**: ~2-3 minutes (typical)
- Performance depends on:
  - Email size and complexity
  - Number of URLs to extract
  - Internet connection speed
  - Gmail API response time

## Limitations

- Maximum 1000 emails per export (configurable)
- Gmail API readonly scope only (no sending/modifying emails)
- Requires internet connection
- Subject to Gmail API quotas
- No attachment download in v1.0

## Future Enhancements

Planned features for future versions:

- [ ] Date range filtering
- [ ] Attachment download
- [ ] Multiple Gmail account support
- [ ] Scheduled/automated exports
- [ ] CSV export format
- [ ] GUI interface
- [ ] Integration with CRM systems
- [ ] Advanced analytics and visualization

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Testing

Run tests (when implemented):

```bash
pytest tests/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or contributions:

- **Issues**: [GitHub Issues](https://github.com/yourusername/gmailagent/issues)
- **Documentation**: [GitHub Wiki](https://github.com/yourusername/gmailagent/wiki)
- **Email**: team@example.com

## Acknowledgments

- Gmail API by Google
- openpyxl library for Excel generation
- Click library for CLI interface
- BeautifulSoup for HTML parsing

## Changelog

### Version 1.0.0 (2024-11-21)

- Initial release
- OAuth 2.0 authentication
- Email retrieval with filters (folder, label, tag, sender, recipient, subject)
- URL extraction from plain text and HTML emails
- Excel export with smart filename generation
- Organized exports directory structure
- Command-line interface with helpful messages
- Progress indicators
- Error handling

---

**Made with ❤️ by the GmailAgent Team**
