"""
Test Option 5 (Run All Agents) workflow
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from orchestrator import AgentOrchestrator


def test_orchestrator_creation():
    """Test that orchestrator can be created"""
    print("=" * 70)
    print("TEST 1: Orchestrator Creation")
    print("=" * 70)

    try:
        orch = AgentOrchestrator()
        print("[OK] Orchestrator created successfully")
        print(f"[INFO] Project root: {orch.PROJECT_ROOT}")
        print(f"[INFO] Exports dir: {orch.EXPORTS_DIR}")
        print(f"[INFO] Output dir: {orch.OUTPUT_DIR}")
        print(f"[INFO] Greetings dir: {orch.GREETINGS_RESULTS_DIR}")
        print(f"[INFO] Email drafts dir: {orch.EMAIL_DRAFTS_DIR}")
        print(f"[INFO] Default email: {orch.DEFAULT_EMAIL}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to create orchestrator: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_check_status_function():
    """Test status checking function"""
    print("\n" + "=" * 70)
    print("TEST 2: Status Check Function")
    print("=" * 70)

    try:
        orch = AgentOrchestrator()

        # Test with non-existent file
        ready, msg = orch.check_status_ready(Path("nonexistent.xlsx"))
        print(f"[INFO] Non-existent file: ready={ready}, msg={msg}")

        # Test with existing file (if any)
        test_file = orch.GREETINGS_OUTPUT
        if test_file.exists():
            ready, msg = orch.check_status_ready(test_file)
            print(f"[INFO] Existing file: ready={ready}, msg={msg}")
        else:
            print(f"[INFO] No existing greetings output to test with")

        print("[OK] Status check function works")
        return True
    except Exception as e:
        print(f"[ERROR] Status check failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_agent_functions_exist():
    """Test that all agent functions exist"""
    print("\n" + "=" * 70)
    print("TEST 3: Agent Functions Exist")
    print("=" * 70)

    try:
        orch = AgentOrchestrator()

        # Check if methods exist
        assert hasattr(orch, 'run_agent_1_gmail'), "run_agent_1_gmail missing"
        print("[OK] run_agent_1_gmail exists")

        assert hasattr(orch, 'run_agent_2_repo_analyzer'), "run_agent_2_repo_analyzer missing"
        print("[OK] run_agent_2_repo_analyzer exists")

        assert hasattr(orch, 'run_agent_3_greetings'), "run_agent_3_greetings missing"
        print("[OK] run_agent_3_greetings exists")

        assert hasattr(orch, 'run_agent_4_evaluation_sender'), "run_agent_4_evaluation_sender missing"
        print("[OK] run_agent_4_evaluation_sender exists")

        assert hasattr(orch, 'run_all_agents'), "run_all_agents missing"
        print("[OK] run_all_agents exists")

        assert hasattr(orch, 'reset_all'), "reset_all missing"
        print("[OK] reset_all exists")

        print("[OK] All agent functions exist")
        return True
    except Exception as e:
        print(f"[ERROR] Function check failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_file_checks():
    """Test file checking function"""
    print("\n" + "=" * 70)
    print("TEST 4: File Checking")
    print("=" * 70)

    try:
        orch = AgentOrchestrator()

        # Test check_file_exists
        exists = orch.check_file_exists(Path("orchestrator.py"))
        print(f"[INFO] orchestrator.py exists: {exists}")
        assert exists, "orchestrator.py should exist"
        print("[OK] orchestrator.py found")

        exists = orch.check_file_exists(Path("nonexistent.txt"))
        print(f"[INFO] nonexistent.txt exists: {exists}")
        assert not exists, "nonexistent.txt should not exist"
        print("[OK] Correctly detected non-existent file")

        print("[OK] File checking works")
        return True
    except Exception as e:
        print(f"[ERROR] File check failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_menu_display():
    """Test that menu can be displayed"""
    print("\n" + "=" * 70)
    print("TEST 5: Menu Display")
    print("=" * 70)

    try:
        orch = AgentOrchestrator()
        print("[INFO] Displaying menu...")
        print()
        orch.show_menu()
        print()
        print("[OK] Menu displayed successfully")
        return True
    except Exception as e:
        print(f"[ERROR] Menu display failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests"""
    print("\n" + "=" * 70)
    print("ORCHESTRATOR OPTION 5 TESTS")
    print("=" * 70)
    print()

    results = []

    # Run tests
    results.append(("Orchestrator Creation", test_orchestrator_creation()))
    results.append(("Status Check Function", test_check_status_function()))
    results.append(("Agent Functions Exist", test_agent_functions_exist()))
    results.append(("File Checking", test_file_checks()))
    results.append(("Menu Display", test_menu_display()))

    # Summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)

    passed = sum(1 for _, result in results if result)
    failed = len(results) - passed

    for test_name, result in results:
        status = "[OK]" if result else "[FAILED]"
        print(f"{status} {test_name}")

    print()
    print(f"Total: {len(results)} tests")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

    if failed == 0:
        print("\n[OK] All tests passed!")
        return 0
    else:
        print(f"\n[ERROR] {failed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
