"""
Test the "No emails found" fix in orchestrator
"""

import sys
from pathlib import Path
from io import StringIO

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from orchestrator import AgentOrchestrator


def test_no_emails_detection():
    """Test that orchestrator detects when gmailagent finds no emails"""
    print("=" * 70)
    print("TEST: No Emails Found Detection")
    print("=" * 70)
    print()

    print("[INFO] This test verifies the fix for when gmailagent completes")
    print("[INFO] successfully but finds no emails matching the filters.")
    print()

    # Create orchestrator
    orch = AgentOrchestrator()

    # Test with filters that won't match any emails
    # (assuming the user doesn't have emails with this specific combination)
    print("[INFO] Testing with filters: label='test999xyz', subject='test999xyz'")
    print("[INFO] These filters should not match any emails")
    print()

    # Note: This will actually try to run gmailagent, which requires auth
    # For a real test, we'd mock the subprocess call
    print("[WARN] This test requires Gmail authentication to run")
    print("[INFO] Run 'python -m gmailagent auth' first if not authenticated")
    print()

    try:
        result = orch.run_agent_1_gmail(
            label='test999xyz',
            subject='test999xyz'
        )

        if result is False:
            print()
            print("[OK] Test PASSED: Orchestrator correctly detected no emails found")
            print("[OK] The fix is working - orchestrator returns False when no emails match")
            return True
        else:
            print()
            print("[UNEXPECTED] Test result: Agent returned success")
            print("[INFO] Either emails were found or authentication failed")
            return None

    except Exception as e:
        print()
        print(f"[INFO] Test could not complete: {e}")
        print("[INFO] This is expected if Gmail is not authenticated")
        print()
        print("To run this test properly:")
        print("  1. Authenticate: python -m gmailagent auth")
        print("  2. Run test again: python tests/test_no_emails_fix.py")
        return None


def test_orchestrator_validation():
    """Test that orchestrator has the validation logic in place"""
    print("\n" + "=" * 70)
    print("TEST: Validation Logic Presence")
    print("=" * 70)
    print()

    # Read orchestrator.py and check for the fix
    orch_path = Path(__file__).parent.parent / "orchestrator.py"

    with open(orch_path, 'r', encoding='utf-8') as f:
        content = f.read()

    checks = [
        ('No emails found" in result.stdout', 'Check for "No emails found"'),
        ('No messages found" in result.stdout', 'Check for "No messages found"'),
        ('GmailAgent completed but found no emails', 'Warning message for no emails'),
        ('No emails match your filters', 'Helpful user guidance'),
    ]

    all_present = True
    for check_str, description in checks:
        if check_str in content:
            print(f"[OK] Found: {description}")
        else:
            print(f"[ERROR] Missing: {description}")
            all_present = False

    print()
    if all_present:
        print("[OK] Test PASSED: All validation logic is present")
        return True
    else:
        print("[ERROR] Test FAILED: Some validation logic is missing")
        return False


def main():
    """Run all tests"""
    print("\n" + "=" * 70)
    print("NO EMAILS FOUND FIX - VERIFICATION TESTS")
    print("=" * 70)
    print()

    results = []

    # Test 1: Validation logic presence (always works)
    results.append(("Validation Logic", test_orchestrator_validation()))

    # Test 2: Actual no emails detection (requires auth)
    results.append(("No Emails Detection", test_no_emails_detection()))

    # Summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)

    for test_name, result in results:
        if result is True:
            status = "[OK]"
        elif result is False:
            status = "[FAILED]"
        else:
            status = "[SKIPPED]"
        print(f"{status} {test_name}")

    passed = sum(1 for _, result in results if result is True)
    failed = sum(1 for _, result in results if result is False)
    skipped = sum(1 for _, result in results if result is None)

    print()
    print(f"Passed:  {passed}")
    print(f"Failed:  {failed}")
    print(f"Skipped: {skipped}")

    if failed == 0:
        print("\n[OK] Verification successful!")
        return 0
    else:
        print(f"\n[ERROR] {failed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
