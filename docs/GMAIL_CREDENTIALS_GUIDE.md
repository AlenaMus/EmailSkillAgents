# Complete Guide: Getting Gmail API Credentials

## 📋 What You Need to Understand

There are **TWO types** of Google credentials:

### 1. ❌ API Key (What You Have)
- File: `apiKeyGmail.txt`
- Contains: `AIzaSy...` (Google API Key)
- **Cannot access Gmail emails** (only for public data)
- Used for: Maps, YouTube public data, etc.

### 2. ✅ OAuth 2.0 Credentials (What You NEED)
- File: `client_secret_XXXXX.apps.googleusercontent.com.json`
- Contains: `client_id`, `client_secret`, `redirect_uris`
- **CAN access Gmail emails** (with user authorization)
- Used for: Reading emails, accessing private data

## ✅ Good News: You Already Have OAuth Credentials!

You have this file:
```
C:\AIDevelopmentCourse\L-19\client_secret_184344902751-h40ql7clun2pccs9nstlo1fi8pt9opjc.apps.googleusercontent.com.json
```

**This is the correct file for Gmail access!**

---

## 🔐 How OAuth 2.0 Works (2-Step Process)

### Step 1: OAuth Credentials (You Have This ✅)
The JSON file with `client_id` and `client_secret`
- Created once in Google Cloud Console
- Like a "key to your app"
- Stored on your computer

### Step 2: User Authorization Token (You Need This ⚠️)
The browser authorization to access YOUR Gmail
- User clicks "Allow" in browser (ONE TIME)
- Token saved to `~/.gmailagent/token.json`
- Valid for long time (months/years)
- Renewed automatically

---

## 🚀 What You Need To Do NOW

You already have Step 1 (OAuth credentials). You just need Step 2 (user authorization):

### From Windows PowerShell:

```powershell
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents
python -m gmailagent.cli auth
```

**What happens:**
1. Browser opens automatically
2. Google asks: "Allow GmailAgent to read your Gmail?"
3. You click **"Allow"**
4. Token saved to `~/.gmailagent/token.json`
5. ✅ **Done forever!** (token auto-renews)

---

## 📖 Complete Guide: Creating OAuth Credentials from Scratch

If you ever need to create new credentials, here's the full process:

### Step 1: Go to Google Cloud Console

Visit: https://console.cloud.google.com/

### Step 2: Create or Select Project

**Option A: Create New Project**
1. Click "Select a project" (top bar)
2. Click "NEW PROJECT"
3. Enter project name: "GmailAgent"
4. Click "CREATE"
5. Wait for project creation

**Option B: Use Existing Project**
1. Click "Select a project"
2. Choose your existing project

### Step 3: Enable Gmail API

1. In the left menu, go to: **APIs & Services** → **Library**
2. Search for: "Gmail API"
3. Click on "Gmail API"
4. Click **"ENABLE"** button
5. Wait for it to enable

### Step 4: Create OAuth 2.0 Credentials

1. Go to: **APIs & Services** → **Credentials**
2. Click **"+ CREATE CREDENTIALS"** (top)
3. Select **"OAuth client ID"**

### Step 5: Configure OAuth Consent Screen (if prompted)

If this is your first time:

1. Choose **"External"** (for personal Gmail)
2. Click **"CREATE"**

**Fill out the form:**
- **App name**: GmailAgent
- **User support email**: [Your email]
- **Developer email**: [Your email]
- Click **"SAVE AND CONTINUE"**

**Scopes** (next page):
- Click **"ADD OR REMOVE SCOPES"**
- Search for: `gmail.readonly`
- Check: `https://www.googleapis.com/auth/gmail.readonly`
- Click **"UPDATE"**
- Click **"SAVE AND CONTINUE"**

**Test Users** (next page):
- Click **"+ ADD USERS"**
- Add your Gmail address
- Click **"ADD"**
- Click **"SAVE AND CONTINUE"**

**Summary:**
- Click **"BACK TO DASHBOARD"**

### Step 6: Create OAuth Client ID

Back to: **APIs & Services** → **Credentials**

1. Click **"+ CREATE CREDENTIALS"** → **"OAuth client ID"**
2. **Application type**: Choose **"Desktop app"**
3. **Name**: "GmailAgent Desktop"
4. Click **"CREATE"**

### Step 7: Download Credentials

1. A popup appears with your credentials
2. Click **"DOWNLOAD JSON"**
3. Save the file (name will be like):
   ```
   client_secret_XXXXX.apps.googleusercontent.com.json
   ```
4. Move it to: `C:\AIDevelopmentCourse\L-19\`

---

## 🔧 Using Your Credentials with GmailAgent

### Option A: Automatic Setup

Place credentials file in project directory:
```powershell
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents
python -m gmailagent.cli auth --credentials "C:\AIDevelopmentCourse\L-19\client_secret_XXXXX.json"
```

### Option B: Manual Setup

Copy to default location:
```powershell
mkdir $env:USERPROFILE\.gmailagent
copy "C:\AIDevelopmentCourse\L-19\client_secret_XXXXX.json" "$env:USERPROFILE\.gmailagent\credentials.json"
python -m gmailagent.cli auth
```

---

## 🎯 Complete Flow Diagram

```
┌─────────────────────────────────────────────────────┐
│ Google Cloud Console                                │
│                                                     │
│ 1. Create Project                                   │
│ 2. Enable Gmail API                                 │
│ 3. Create OAuth 2.0 Client ID                       │
│ 4. Download credentials.json                        │
└─────────────────┬───────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────┐
│ Your Computer                                       │
│                                                     │
│ 5. Run: python -m gmailagent.cli auth               │
│    → Browser opens                                  │
│    → Sign in to Gmail                               │
│    → Click "Allow"                                  │
│    → Token saved to ~/.gmailagent/token.json        │
└─────────────────┬───────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────┐
│ ✅ Ready to Use!                                     │
│                                                     │
│ python -m gmailagent.cli export --tag "work"        │
│ → Exports emails automatically                      │
│ → No browser needed anymore                         │
│ → Token auto-renews                                 │
└─────────────────────────────────────────────────────┘
```

---

## 🔑 What's in the Credentials File?

**credentials.json (OAuth 2.0):**
```json
{
  "installed": {
    "client_id": "XXXXX.apps.googleusercontent.com",
    "client_secret": "GOCSPX-XXXXX",
    "redirect_uris": ["http://localhost"],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token"
  }
}
```

**token.json (After Authorization):**
```json
{
  "token": "ya29.a0AfH6SMBxxxxx",
  "refresh_token": "1//0gxxxxx",
  "expiry": "2024-11-22T12:00:00Z",
  "scopes": ["https://www.googleapis.com/auth/gmail.readonly"]
}
```

---

## ❓ FAQ

### Q: Why can't I use the API key?
**A:** API keys are for public data only. Gmail emails are private, so OAuth 2.0 with user authorization is required for security.

### Q: Do I need to authorize every time?
**A:** No! Only once. The token is saved and auto-renewed.

### Q: Is it safe to authorize?
**A:** Yes! You're only granting "readonly" permission. The app cannot send emails or delete anything.

### Q: Can I revoke access?
**A:** Yes! Go to: https://myaccount.google.com/permissions
Or run: `python -m gmailagent.cli revoke`

### Q: What if I get "App not verified" warning?
**A:** Click "Advanced" → "Go to GmailAgent (unsafe)". This appears because you created the app yourself. It's safe.

### Q: How long is the token valid?
**A:** Refresh tokens can last indefinitely. They auto-renew when needed.

---

## 🎯 Your Current Status

✅ **You have:** OAuth 2.0 credentials file (client_secret JSON)
⚠️ **You need:** User authorization token (browser authorization)

**Next step:** Run from Windows PowerShell:
```powershell
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents
python -m gmailagent.cli auth
```

Browser will open → Sign in → Click "Allow" → Done! 🎉

---

## 📞 Troubleshooting

### Error: "Redirect URI mismatch"
Make sure OAuth client type is "Desktop app", not "Web application"

### Error: "Access blocked: This app's request is invalid"
1. Make sure Gmail API is enabled in Cloud Console
2. Make sure your Gmail is added as a test user

### Error: "The user did not consent"
You clicked "Deny" instead of "Allow". Run `auth` command again.

### Error: "invalid_grant"
Token expired. Delete `~/.gmailagent/token.json` and run `auth` again.

---

**Ready to authorize?** Just run the commands in Windows PowerShell! 🚀
