# Gmail Agent Authentication Script for Windows PowerShell
# This script authenticates GmailAgent with your Gmail account

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "GmailAgent - Gmail API Authentication" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to project directory
Set-Location "C:\AIDevelopmentCourse\L-19\EmailSkillAgents"

# Check if credentials exist
$credentialsPath = "$env:USERPROFILE\.gmailagent\credentials.json"
if (-Not (Test-Path $credentialsPath)) {
    Write-Host "Setting up credentials..." -ForegroundColor Yellow

    # Create directory if it doesn't exist
    $gmailAgentDir = "$env:USERPROFILE\.gmailagent"
    if (-Not (Test-Path $gmailAgentDir)) {
        New-Item -ItemType Directory -Path $gmailAgentDir -Force | Out-Null
    }

    # Copy credentials from private directory
    $privateCredentials = "C:\AIDevelopmentCourse\L-19\private\client_secret_184344902751-bdc92tjt9t9omprtouc2h8koarj8vvbf.apps.googleusercontent.com.json"

    if (Test-Path $privateCredentials) {
        Copy-Item $privateCredentials $credentialsPath
        Write-Host "✓ Credentials copied successfully" -ForegroundColor Green
    } else {
        Write-Host "ERROR: Credentials file not found at:" -ForegroundColor Red
        Write-Host $privateCredentials -ForegroundColor Red
        Write-Host ""
        Write-Host "Please make sure the credentials file exists in the private directory." -ForegroundColor Yellow
        exit 1
    }
}

Write-Host ""
Write-Host "Starting authentication process..." -ForegroundColor Yellow
Write-Host "This will open a browser window for you to authorize the application." -ForegroundColor Yellow
Write-Host ""

# Run authentication
python -m gmailagent.cli auth

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host "✓ Authentication successful!" -ForegroundColor Green
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "You can now export emails using:" -ForegroundColor Cyan
    Write-Host '  python -m gmailagent.cli export --tag "aiDevelopmentCourse"' -ForegroundColor White
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Red
    Write-Host "Authentication failed" -ForegroundColor Red
    Write-Host "============================================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please check the error messages above." -ForegroundColor Yellow
    Write-Host ""
}

Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
