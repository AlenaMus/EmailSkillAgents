# Run GmailAgent from Windows PowerShell

## Quick Start Guide

### Step 1: Open Windows PowerShell

Press `Win + X` and select **"Windows PowerShell"** or **"Windows Terminal"**

### Step 2: Navigate to Project Directory

```powershell
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents
```

### Step 3: Install Dependencies (if not already installed)

```powershell
pip install -r requirements.txt
```

If you get an error about pip not found, try:
```powershell
python -m pip install -r requirements.txt
```

### Step 4: Authenticate with Gmail (ONE-TIME)

```powershell
python -m gmailagent.cli auth
```

**What will happen:**
- Your browser will automatically open
- You'll be asked to sign in to Gmail
- Click **"Allow"** to grant readonly access
- The browser will redirect to localhost (this is normal!)
- Authentication completes automatically
- You'll see: **✓ Authentication successful!**

### Step 5: Export Emails with Tag "aiDevelopmentCourse"

```powershell
python -m gmailagent.cli export --tag "aiDevelopmentCourse"
```

**Output will be saved to:**
```
exports/22.11.2024_HHMMSS_mails_by_tag_aiDevelopmentCourse.xlsx
```

The Excel file will contain:
- **ID**: Unique identifier for each email
- **Date**: Email timestamp (YYYY-MM-DD HH:MM:SS)
- **Subject**: Email subject line
- **URL**: Any URLs found in the email body

---

## Additional Commands

### List all Gmail labels
```powershell
python -m gmailagent.cli list-labels
```

### Export by different filters
```powershell
# By sender
python -m gmailagent.cli export --from "sender@example.com"

# By subject
python -m gmailagent.cli export --subject "meeting"

# Multiple filters
python -m gmailagent.cli export --tag "work" --from "boss@company.com"
```

### Check authentication status
```powershell
python -m gmailagent.cli info
```

### View help
```powershell
python -m gmailagent.cli --help
```

---

## Troubleshooting

### If browser doesn't open automatically:

1. Look for a URL in the terminal output
2. Copy the URL manually
3. Open it in your browser
4. Complete authorization
5. The terminal will detect it and continue

### If you get "module not found" errors:

Make sure you're in the correct directory:
```powershell
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents
```

And install dependencies:
```powershell
pip install -r requirements.txt
```

### If authentication fails:

1. Delete old credentials:
```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\.gmailagent"
```

2. Try authenticating again:
```powershell
python -m gmailagent.cli auth
```

---

## What Happens After First Authentication?

After you authenticate once:
- ✅ Token is saved to `~/.gmailagent/token.json`
- ✅ Future runs work automatically (no browser needed)
- ✅ Token is valid for a long time
- ✅ You can export emails anytime without re-authenticating

---

## Quick Reference

```powershell
# ONE-TIME: Authenticate
python -m gmailagent.cli auth

# Export by tag
python -m gmailagent.cli export --tag "aiDevelopmentCourse"

# Check output
ls exports\

# Open the Excel file
explorer exports\
```

---

**Ready to run!** Copy the commands above into your Windows PowerShell terminal.
