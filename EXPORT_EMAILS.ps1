# Gmail Agent Email Export Script for Windows PowerShell
# This script exports emails with the "aiDevelopmentCourse" tag

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "GmailAgent - Export Emails" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Navigate to project directory
Set-Location "C:\AIDevelopmentCourse\L-19\EmailSkillAgents"

# Check if authenticated
$tokenPath = "$env:USERPROFILE\.gmailagent\token.pickle"
if (-Not (Test-Path $tokenPath)) {
    Write-Host "ERROR: Not authenticated yet!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please run AUTHENTICATE.ps1 first to authorize the application." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Press any key to exit..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit 1
}

Write-Host "Exporting emails with tag: aiDevelopmentCourse" -ForegroundColor Yellow
Write-Host ""

# Run export
python -m gmailagent.cli export --tag "aiDevelopmentCourse"

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host "✓ Export successful!" -ForegroundColor Green
    Write-Host "============================================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Excel file saved to:" -ForegroundColor Cyan
    Write-Host "  C:\AIDevelopmentCourse\L-19\EmailSkillAgents\exports\" -ForegroundColor White
    Write-Host ""
    Write-Host "Opening exports folder..." -ForegroundColor Yellow
    Start-Process "C:\AIDevelopmentCourse\L-19\EmailSkillAgents\exports"
} else {
    Write-Host ""
    Write-Host "============================================================" -ForegroundColor Red
    Write-Host "Export failed" -ForegroundColor Red
    Write-Host "============================================================" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please check the error messages above." -ForegroundColor Yellow
    Write-Host ""
}

Write-Host "Press any key to continue..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
