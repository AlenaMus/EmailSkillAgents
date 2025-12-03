# GmailAgent - Installation Guide

## Quick Start

### Prerequisites

1. **Python 3.8+**
   ```bash
   python --version  # Should be 3.8 or higher
   ```

2. **Google Cloud Project with Gmail API**
   - Create project at [Google Cloud Console](https://console.cloud.google.com/)
   - Enable Gmail API
   - Create OAuth 2.0 credentials (Desktop application)
   - Download credentials JSON file

### Installation Steps

#### Step 1: Clone or Download

```bash
cd /path/to/EmailSkillAgents
```

#### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Expected output:
```
Successfully installed google-auth-oauthlib-1.1.0 google-auth-httplib2-0.1.1
google-api-python-client-2.108.0 openpyxl-3.1.2 beautifulsoup4-4.12.2
click-8.1.7 pyyaml-6.0.1 lxml-4.9.3
```

#### Step 3: Install GmailAgent Package

```bash
pip install -e .
```

Expected output:
```
Successfully installed gmailagent-1.0.0
```

#### Step 4: Verify Installation

```bash
gmailagent --version
```

Expected output:
```
gmailagent, version 1.0.0
```

```bash
gmailagent info
```

Expected output:
```
============================================================
GmailAgent v1.0.0
============================================================

Gmail Email Exporter with URL Extraction

Authentication: ✗ Not authenticated
  Run 'gmailagent auth' to authenticate

Exports Directory: ./exports/
Exported Files: 0

For help: gmailagent --help
Documentation: https://github.com/yourusername/gmailagent
```

### Step 5: Setup Authentication

#### 5.1 Prepare Credentials

Place your downloaded OAuth credentials file somewhere accessible:
```bash
# Example path
/path/to/client_secret_xxxxx.json
```

#### 5.2 Authenticate

```bash
gmailagent auth --credentials /path/to/client_secret_xxxxx.json
```

This will:
1. Copy credentials to `~/.gmailagent/credentials.json`
2. Open a browser window for OAuth authorization
3. Save authentication token to `~/.gmailagent/token.pickle`

Expected flow:
```
============================================================
GmailAgent - Gmail API Authentication
============================================================

Setting up credentials from: /path/to/client_secret_xxxxx.json

Credentials setup complete!
Starting authentication process...

A browser window will open for you to authorize the application.

✓ Authentication successful!
You can now use 'gmailagent export' to retrieve emails.
```

#### 5.3 Verify Authentication

```bash
gmailagent info
```

Should now show:
```
Authentication: ✓ Authenticated
```

## First Export

Try your first export:

```bash
# List available labels
gmailagent list-labels

# Export emails from INBOX (limited to 10 for testing)
gmailagent export --folder INBOX --limit 10
```

Expected output:
```
============================================================
GmailAgent - Email Export
============================================================

Authenticating with Gmail API...
✓ Authenticated successfully

Active filters:
  - folder: INBOX

Retrieving emails (max: 10)...
Search query: in:INBOX
Fetching message IDs...
Found 10 messages. Retrieving details...
Processing: 10/10 emails...
✓ Retrieved 10 emails

Extracting URLs from email bodies...
✓ Extracted X URLs from Y emails

Generating Excel file...
✓ Excel file created

============================================================
✓ Exported 10 emails to: exports/21.11.2024_150322_mails_from_folder_INBOX.xlsx
============================================================
```

## Testing the Installation

### Test 1: Authentication
```bash
gmailagent info
# Should show "✓ Authenticated"
```

### Test 2: List Labels
```bash
gmailagent list-labels
# Should display your Gmail labels
```

### Test 3: List Folders
```bash
gmailagent list-folders
# Should display common Gmail folders
```

### Test 4: Export Test
```bash
gmailagent export --folder INBOX --limit 5
# Should create an Excel file in ./exports/
```

### Test 5: Verify Export
```bash
ls -la exports/
# Should show the generated .xlsx file

# Open the Excel file and verify:
# - 4 columns: ID, Date, Subject, URL
# - 5 rows of data (plus header)
# - UUIDs in ID column
# - Dates in YYYY-MM-DD HH:MM:SS format
# - URLs in URL column (if emails contained URLs)
```

## Troubleshooting

### Issue: "Command not found: gmailagent"

**Solution:**
```bash
# Reinstall the package
pip install -e .

# Or run directly
python -m gmailagent.cli --help
```

### Issue: "Credentials file not found"

**Solution:**
```bash
# Make sure you run auth with credentials path
gmailagent auth --credentials /path/to/credentials.json

# Or manually copy to default location
mkdir -p ~/.gmailagent
cp /path/to/credentials.json ~/.gmailagent/credentials.json
gmailagent auth
```

### Issue: "Import Error: No module named 'google'"

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "Permission denied" when saving token

**Solution:**
```bash
# Ensure home directory is writable
mkdir -p ~/.gmailagent
chmod 755 ~/.gmailagent
```

### Issue: OAuth consent screen error

**Solution:**
1. Go to Google Cloud Console
2. Navigate to APIs & Services > OAuth consent screen
3. Add your email to test users
4. Make sure app is in testing mode

### Issue: "API not enabled"

**Solution:**
1. Go to Google Cloud Console
2. Navigate to APIs & Services > Library
3. Search for "Gmail API"
4. Click Enable

## Development Installation

For development with live code changes:

```bash
# Install in development mode
pip install -e .

# Install development dependencies (if any)
pip install pytest pytest-cov black flake8

# Run tests (when implemented)
pytest tests/

# Format code
black gmailagent/

# Lint code
flake8 gmailagent/
```

## Uninstallation

To completely remove GmailAgent:

```bash
# Uninstall package
pip uninstall gmailagent

# Remove credentials and tokens
rm -rf ~/.gmailagent

# Remove exports (optional)
rm -rf exports/
```

## Virtual Environment (Recommended)

It's recommended to use a virtual environment:

```bash
# Create virtual environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install in virtual environment
pip install -r requirements.txt
pip install -e .

# Deactivate when done
deactivate
```

## Docker Installation (Optional)

Create a Dockerfile:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install -e .

ENTRYPOINT ["gmailagent"]
CMD ["--help"]
```

Build and run:

```bash
docker build -t gmailagent .
docker run -v ~/.gmailagent:/root/.gmailagent -v ./exports:/app/exports gmailagent export --folder INBOX
```

## Getting Help

```bash
# General help
gmailagent --help

# Command-specific help
gmailagent auth --help
gmailagent export --help

# Check version
gmailagent --version

# Check status
gmailagent info
```

## Next Steps

After successful installation:

1. Read the [README.md](README.md) for detailed usage
2. Review [PRD-GmailAgent.md](PRD-GmailAgent.md) for feature details
3. Check [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for technical overview
4. Try different export filters
5. Customize configuration in `~/.gmailagent/config.yaml` (optional)

## Support

For issues or questions:
- Check [README.md](README.md) troubleshooting section
- Review [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
- Open an issue on GitHub
- Contact: team@example.com

---

**Installation Complete!**

You're ready to start exporting emails from Gmail.
