# GmailAgent - Quick Start Guide

Get started with GmailAgent in 5 minutes!

## Prerequisites

- Python 3.8+
- Gmail account
- Google Cloud Project with Gmail API enabled

## Installation (2 minutes)

```bash
# Navigate to project directory
cd EmailSkillAgents

# Install dependencies
pip install -r requirements.txt

# Install GmailAgent
pip install -e .

# Verify installation
gmailagent --version
```

## Setup (3 minutes)

### Step 1: Get OAuth Credentials

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create new project (or select existing)
3. Enable Gmail API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download credentials JSON

### Step 2: Authenticate

```bash
gmailagent auth --credentials /path/to/downloaded/credentials.json
```

Browser opens → Sign in → Authorize → Done!

## Your First Export (30 seconds)

```bash
# Export 10 emails from INBOX
gmailagent export --folder INBOX --limit 10
```

Output will be in: `exports/DD.MM.YYYY_HHMMSS_mails_from_folder_INBOX.xlsx`

## Common Use Cases

### Export Work Emails
```bash
gmailagent export --label "Work"
```

### Export from Specific Sender
```bash
gmailagent export --from "boss@company.com"
```

### Export with Subject Filter
```bash
gmailagent export --subject "invoice"
```

### Combine Filters
```bash
gmailagent export --label "Important" --from "client@example.com"
```

### Custom Output Location
```bash
gmailagent export --label "Work" --output "my_emails.xlsx"
```

## Available Commands

```bash
gmailagent auth              # Authenticate with Gmail
gmailagent export            # Export emails to Excel
gmailagent list-labels       # Show your Gmail labels
gmailagent list-folders      # Show common folders
gmailagent info              # Check status
gmailagent revoke            # Remove credentials
gmailagent --help            # Get help
```

## What Gets Exported?

Excel file with 4 columns:

| ID | Date | Subject | URL |
|----|------|---------|-----|
| UUID | 2024-11-21 09:30:00 | Meeting invite | https://zoom.us/j/123 |

- **ID**: Unique identifier (UUID)
- **Date**: Email date/time
- **Subject**: Email subject line
- **URL**: Extracted URLs (comma-separated if multiple)

## Filter Options

| Filter | Example |
|--------|---------|
| `--folder` | `--folder INBOX` |
| `--label` | `--label "Work"` |
| `--tag` | `--tag "Important"` |
| `--from` | `--from "boss@company.com"` |
| `--to` | `--to "client@example.com"` |
| `--subject` | `--subject "invoice"` |
| `--limit` | `--limit 100` |
| `--output` | `--output custom.xlsx` |

## Smart Filenames

Files are auto-named based on your filters:

```
22.11.2024_143022_mails_by_label_Work.xlsx
22.11.2024_143530_mails_from_sender_john@example.com.xlsx
22.11.2024_145522_mails_by_tag_Work_from_sender_boss@company.com.xlsx
```

## Where Are My Exports?

All exports go to: `./exports/`

```bash
ls exports/
```

## Troubleshooting

### Can't find gmailagent command?
```bash
pip install -e .
```

### Authentication failed?
```bash
# Make sure Gmail API is enabled in Google Cloud Console
# Re-run auth
gmailagent auth
```

### No emails found?
```bash
# Check your labels
gmailagent list-labels

# Check your filters
gmailagent export --folder INBOX --limit 5
```

### Need help?
```bash
gmailagent --help
gmailagent export --help
```

## Tips

1. **Start Small**: Use `--limit 10` for testing
2. **Check Labels**: Use `list-labels` to see available labels
3. **Combine Filters**: Use multiple filters for precise results
4. **Custom Output**: Use `--output` for specific filenames
5. **Progress**: Watch the progress messages during export

## Example Workflow

```bash
# 1. Check authentication
gmailagent info

# 2. See available labels
gmailagent list-labels

# 3. Export work emails
gmailagent export --label "Work" --limit 50

# 4. Export from specific sender
gmailagent export --from "important@company.com"

# 5. Export with subject filter
gmailagent export --subject "meeting" --label "Calendar"

# 6. Check exports
ls exports/
```

## What's Extracted?

- Email ID
- Date and time
- Subject line
- **All URLs** from email body (plain text and HTML)
- Sorted by date (newest first)

## Limitations

- Max 1000 emails per export (configurable with `--limit`)
- Readonly access (cannot send/modify emails)
- Requires internet connection
- Subject to Gmail API quotas

## Next Steps

- Read [README.md](README.md) for detailed documentation
- Review [INSTALLATION.md](INSTALLATION.md) for troubleshooting
- Check [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for technical details

## Support

- GitHub Issues: Report bugs or request features
- Documentation: See README.md
- Email: team@example.com

---

**Ready to export? Start with:**

```bash
gmailagent export --folder INBOX --limit 10
```

**Happy exporting!**
