# Fix "400 Redirect URI Mismatch" Error

## 🔴 What's the Problem?

The error **"400 redirect URI mismatch"** means:
- Your app is trying to use: `http://localhost:45797/`
- But Google OAuth client expects a different redirect URI

## ✅ Solution: Fix in Google Cloud Console

### Step 1: Go to Google Cloud Console

Visit: https://console.cloud.google.com/

### Step 2: Navigate to Credentials

1. Click on your project (top bar)
2. Go to: **APIs & Services** → **Credentials** (left menu)

### Step 3: Find Your OAuth Client

1. Under **"OAuth 2.0 Client IDs"** section
2. Find the client with ID: `184344902751-h40ql7clun2pccs9nstlo1fi8pt9opjc`
3. Click on the **client name** (or the pencil/edit icon)

### Step 4: Add Redirect URIs

In the **"Authorized redirect URIs"** section, make sure you have ALL of these:

```
http://localhost:8080/
http://localhost:45797/
http://localhost/
http://localhost:8888/
http://127.0.0.1:8080/
http://127.0.0.1/
```

**How to add them:**
1. Click **"+ ADD URI"** button
2. Paste each URI (one at a time)
3. Press Enter after each one

### Step 5: Save Changes

1. Click **"SAVE"** at the bottom
2. Wait for "Credentials updated" message

### Step 6: Download New Credentials (Important!)

1. After saving, go back to **Credentials** page
2. Find your OAuth client again
3. Click the **download icon** (⬇️) on the right
4. Save the new JSON file
5. Replace the old credentials file:

```powershell
# In PowerShell
copy "C:\Users\YourName\Downloads\client_secret_*.json" "C:\AIDevelopmentCourse\L-19\"
```

---

## 🔄 Alternative: Recreate OAuth Client with Correct Settings

If editing doesn't work, create a new OAuth client:

### Option A: Desktop Application (Recommended)

1. **Go to:** https://console.cloud.google.com/apis/credentials
2. **Click:** "+ CREATE CREDENTIALS" → "OAuth client ID"
3. **Application type:** Choose **"Desktop app"**
4. **Name:** GmailAgent Desktop
5. **Click:** "CREATE"
6. **Download** the JSON file
7. **Save to:** `C:\AIDevelopmentCourse\L-19\`

Desktop apps automatically include the correct redirect URIs!

### Option B: Web Application (Advanced)

Only if you specifically need web application:

1. **Application type:** "Web application"
2. **Authorized redirect URIs:** Add these:
   ```
   http://localhost:8080/
   http://localhost:45797/
   http://localhost/
   ```
3. **Click:** "CREATE"
4. **Download** the JSON file

---

## 🚀 After Fixing

### Step 1: Update Credentials

```powershell
cd C:\AIDevelopmentCourse\L-19\EmailSkillAgents

# Remove old credentials
Remove-Item -Force "$env:USERPROFILE\.gmailagent\credentials.json"

# Copy new credentials
copy "C:\AIDevelopmentCourse\L-19\client_secret_*.json" "$env:USERPROFILE\.gmailagent\credentials.json"
```

### Step 2: Authenticate Again

```powershell
python -m gmailagent.cli auth
```

This time it should work! ✅

---

## 📋 Quick Checklist

- [ ] Go to Google Cloud Console
- [ ] Navigate to APIs & Services → Credentials
- [ ] Edit OAuth Client ID
- [ ] Add redirect URIs (especially `http://localhost:45797/`)
- [ ] Save changes
- [ ] Download new credentials JSON
- [ ] Replace old credentials file
- [ ] Run `python -m gmailagent.cli auth` again

---

## ❓ Common Questions

**Q: Why does the port number keep changing?**
A: The application uses a random available port. Adding multiple localhost URIs covers all cases.

**Q: Which redirect URIs should I add?**
A: Add all of these to be safe:
- `http://localhost:8080/`
- `http://localhost:45797/`
- `http://localhost/`

**Q: Can I use "Desktop app" type instead?**
A: Yes! Desktop app type includes the necessary redirect URIs automatically. This is the easiest option.

**Q: Do I need to wait after saving?**
A: Changes are usually instant, but occasionally take a few minutes. If it still doesn't work, wait 5 minutes and try again.

---

## 🎯 Recommended Quick Fix

**The fastest solution:**

1. **Delete the current OAuth client** (or create a new one)
2. **Create new OAuth client** with type: **"Desktop app"**
3. **Download the JSON**
4. **Replace credentials:**
   ```powershell
   copy "Downloads\client_secret_*.json" "$env:USERPROFILE\.gmailagent\credentials.json"
   ```
5. **Run:** `python -m gmailagent.cli auth`

Desktop app type automatically works with all localhost ports! ✅

---

## 📸 Visual Guide

### What You Should See:

**In OAuth Client Edit Screen:**

```
Application type: Desktop app  ← or Web application
Name: GmailAgent

Authorized redirect URIs:  ← Only for Web application type
  http://localhost:8080/
  http://localhost:45797/
  http://localhost/
  [+ ADD URI]

[SAVE]
```

---

**After fixing this, your authentication will work smoothly!** 🚀
