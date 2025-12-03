# How to Download OAuth Credentials from Google Cloud Console

## 🎯 Step-by-Step Guide with Screenshots Description

---

## Step 1: Go to Google Cloud Console

**Open your browser and visit:**
```
https://console.cloud.google.com/
```

**Sign in** with your Google account (the same one you use for Gmail)

---

## Step 2: Select Your Project

**At the top of the page**, you'll see the project selector:
- Look for: **"Select a project"** or the current project name
- Click on it
- You should see: **"manifest-glyph-475616-a8"** (your project)
- Click on that project name

---

## Step 3: Navigate to Credentials Page

**Option A: Direct Link** (Easiest)
```
https://console.cloud.google.com/apis/credentials
```
Just paste this in your browser (make sure your project is selected)

**Option B: Manual Navigation**
1. On the left sidebar, click **☰ (hamburger menu)**
2. Scroll down to **"APIs & Services"**
3. Click **"Credentials"**

---

## Step 4: Find OAuth 2.0 Client IDs Section

On the Credentials page, you'll see several sections:
- API Keys
- **OAuth 2.0 Client IDs** ← This is what you need
- Service Accounts

---

## Step 5: Two Options - Create New OR Edit Existing

### 🆕 OPTION A: Create New Desktop App Credentials (RECOMMENDED)

**This is easier and works better!**

1. **Click the blue button:** **"+ CREATE CREDENTIALS"** (top of page)

2. **Select:** **"OAuth client ID"**

3. **You'll see a form:**
   - **Application type:** Click the dropdown
   - **SELECT:** **"Desktop app"** ⭐ (This is important!)
   - **Name:** Type "GmailAgent" or "My Gmail App"

4. **Click:** **"CREATE"** (blue button at bottom)

5. **Popup appears:** "OAuth client created"
   - You'll see your Client ID and Client secret
   - **Click:** **"DOWNLOAD JSON"** button
   - **OR** Click the **⬇️ download icon**

6. **Save the file:**
   - Your browser will download a file named like:
     `client_secret_184344902751-xxxxx.apps.googleusercontent.com.json`
   - Save it to: **`C:\AIDevelopmentCourse\L-19\`**

7. **Click "OK"** to close the popup

✅ **Done! Skip to Step 6 below**

---

### ✏️ OPTION B: Edit Existing Credentials (Alternative)

**Only do this if you want to fix your existing credentials**

1. **In the "OAuth 2.0 Client IDs" section**, you'll see a table with columns:
   - Name
   - Client ID
   - Creation date
   - Actions

2. **Find the row** with:
   - Client ID: `184344902751-h40ql7clun2pccs9nstlo1fi8pt9opjc`

3. **On the right side of that row**, you'll see icons:
   - 📝 (Edit/Pencil icon) - Click this
   - ⬇️ (Download icon)
   - 🗑️ (Delete icon)

4. **Click the 📝 Pencil/Edit icon**

5. **In the edit page**, scroll down to:
   **"Authorized redirect URIs"**

6. **Add these URIs** (click "+ ADD URI" for each):
   ```
   http://localhost:8080/
   http://localhost:45797/
   http://localhost/
   http://localhost:8888/
   http://127.0.0.1:8080/
   http://127.0.0.1/
   ```

7. **Click "SAVE"** at the bottom

8. **Go back to Credentials page**

9. **Click the ⬇️ Download icon** next to your OAuth client

10. **Save the file** to: `C:\AIDevelopmentCourse\L-19\`

---

## Step 6: Verify the Downloaded File

**Open File Explorer:**
```
C:\AIDevelopmentCourse\L-19\
```

**You should see a file named something like:**
```
client_secret_184344902751-h40ql7clun2pccs9nstlo1fi8pt9opjc.apps.googleusercontent.com.json
```

**File size:** Should be around 300-500 bytes

---

## Step 7: Use the Downloaded Credentials

**Open PowerShell** and run:

```powershell
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents

# Remove old credentials (if any)
Remove-Item -Force "$env:USERPROFILE\.gmailagent\credentials.json" -ErrorAction SilentlyContinue

# Copy new credentials
copy "C:\AIDevelopmentCourse\L-19\client_secret_*.json" "$env:USERPROFILE\.gmailagent\credentials.json"

# Verify it copied
Test-Path "$env:USERPROFILE\.gmailagent\credentials.json"
# Should show: True

# Now authenticate
python -m gmailagent.cli auth
```

**This will:**
1. Open your browser
2. Ask you to sign in
3. Show authorization screen
4. You click "Allow"
5. ✅ Done!

---

## 📸 What You'll See (Visual Guide)

### On Credentials Page:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
APIs & Services > Credentials

[+ CREATE CREDENTIALS ▼]  [Filter]  [Download]

API Keys
(none or existing keys listed here)

OAuth 2.0 Client IDs
┌────────────────────────────────────────────────┐
│ Name          │ Client ID      │ Created    │📝⬇️🗑️│
├────────────────────────────────────────────────┤
│ Your App Name │ 184344...googleusercontent │ Nov 20 │📝⬇️🗑️│
└────────────────────────────────────────────────┘
                                                 ↑
                                    Click download icon

Service Accounts
(if any)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### When Creating New OAuth Client:
```
┌─────────────────────────────────────────┐
│ Create OAuth client ID                   │
├─────────────────────────────────────────┤
│ Application type *                       │
│ [Desktop app ▼]  ← SELECT THIS!          │
│                                          │
│ Name *                                   │
│ [GmailAgent_______________]              │
│                                          │
│              [CREATE]  [CANCEL]          │
└─────────────────────────────────────────┘
```

### After Creating:
```
┌─────────────────────────────────────────┐
│ OAuth client created                     │
├─────────────────────────────────────────┤
│ Your Client ID:                          │
│ 184344...apps.googleusercontent.com      │
│                                          │
│ Your Client Secret:                      │
│ GOCSPX-xxxxx                             │
│                                          │
│ [⬇️ DOWNLOAD JSON]              [OK]      │
└─────────────────────────────────────────┘
              ↑
         Click this!
```

---

## ❓ Troubleshooting

### Problem: "Can't find the download button"
**Solution:**
- Go back to the Credentials page
- Look in the "OAuth 2.0 Client IDs" table
- Find the **⬇️ icon** on the far right of your client's row
- Click it

### Problem: "File downloads with weird name"
**Solution:**
- That's normal! The file name includes the client ID
- Just save it anywhere you can find it
- Use the `copy` command to put it in the right place

### Problem: "I don't see OAuth 2.0 Client IDs section"
**Solution:**
- Make sure you selected the correct project at the top
- Check that you're on the "Credentials" page
- URL should be: `https://console.cloud.google.com/apis/credentials`

### Problem: "CREATE CREDENTIALS is grayed out"
**Solution:**
- You might not have permissions
- Try refreshing the page
- Make sure you're signed in with the correct Google account

---

## 🎯 Quick Summary

1. **Go to:** https://console.cloud.google.com/apis/credentials
2. **Click:** "+ CREATE CREDENTIALS" → "OAuth client ID"
3. **Choose:** "Desktop app"
4. **Name:** "GmailAgent"
5. **Click:** "CREATE"
6. **Click:** "DOWNLOAD JSON"
7. **Save to:** `C:\AIDevelopmentCourse\L-19\`
8. **Done!**

---

## ✅ After Downloading

Run in PowerShell:
```powershell
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents
copy "C:\AIDevelopmentCourse\L-19\client_secret_*.json" "$env:USERPROFILE\.gmailagent\credentials.json"
python -m gmailagent.cli auth
```

**Browser opens → Sign in → Click "Allow" → ✅ Done forever!**

---

**Need help with any step? Let me know which step you're stuck on!** 🚀
