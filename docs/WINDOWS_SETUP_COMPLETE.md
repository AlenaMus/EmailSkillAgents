# Windows PowerShell Setup - Ready to Authenticate!

## ✅ Setup Complete!

Your credentials from the private directory have been configured successfully.

---

## 🚀 Next Steps (Run from Windows PowerShell)

### Step 1: Authenticate with Gmail (ONE-TIME)

**Right-click on this file and select "Run with PowerShell":**
```
C:\AIDevelopmentCourse\L-19\EmailSkillAgents\AUTHENTICATE.ps1
```

**Or open PowerShell and run:**
```powershell
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents
.\AUTHENTICATE.ps1
```

**What will happen:**
1. Browser window opens automatically
2. Sign in to your Gmail account
3. Click "Allow" to grant readonly access
4. Authentication token saved
5. Done! (No need to repeat this)

---

### Step 2: Export Emails

**After authenticating, run:**
```powershell
.\EXPORT_EMAILS.ps1
```

**Or manually:**
```powershell
python -m gmailagent.cli export --tag "aiDevelopmentCourse"
```

**Output location:**
```
C:\AIDevelopmentCourse\L-19\EmailSkillAgents\exports\
```

---

## 📋 What Was Set Up

✅ **Credentials configured:**
- Source: `C:\AIDevelopmentCourse\L-19\private\client_secret_*.json`
- Copied to: `%USERPROFILE%\.gmailagent\credentials.json`

✅ **Scripts created:**
- `AUTHENTICATE.ps1` - One-time Gmail authorization
- `EXPORT_EMAILS.ps1` - Export emails by tag

---

## 🔧 Credentials Details

**Client ID:** `184344902751-bdc92tjt9t9omprtouc2h8koarj8vvbf.apps.googleusercontent.com`

**Project:** `manifest-glyph-475616-a8`

**Type:** Desktop Application (OAuth 2.0)

**Scopes:** Gmail readonly access only

---

## ⚠️ Important Notes

1. **WSL Cannot Open Browser:** You must run authentication from Windows PowerShell, not from WSL/Ubuntu terminal

2. **One-Time Authentication:** After the first successful authentication, the token is saved and will work from both Windows and WSL

3. **Security:** The credentials grant readonly access only - the app cannot send emails or delete anything

---

## 🎯 Quick Reference

### From Windows PowerShell:
```powershell
# First time only - authenticate
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents
.\AUTHENTICATE.ps1

# Export emails
.\EXPORT_EMAILS.ps1

# Or export manually
python -m gmailagent.cli export --tag "aiDevelopmentCourse"
```

### After Authentication Works:
You can then use the CLI from anywhere (Windows or WSL):
```bash
python -m gmailagent.cli export --tag "aiDevelopmentCourse"
```

---

## ❓ Troubleshooting

### "Python not found"
Make sure Python is installed and in your PATH. Try:
```powershell
python --version
```

If not found, install Python from python.org or Microsoft Store.

### "Module not found"
Install dependencies:
```powershell
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents
pip install -r requirements.txt
```

### "Redirect URI mismatch"
The credentials file is configured as Desktop Application type, which should work automatically. If you still get this error, see `FIX_REDIRECT_URI.md`.

### "Browser doesn't open"
Look for the authorization URL in the terminal output and manually copy it to your browser.

---

## 🎉 Ready to Authenticate!

Run `AUTHENTICATE.ps1` from Windows PowerShell to get started!

After authentication, you can export emails with one click using `EXPORT_EMAILS.ps1`.
