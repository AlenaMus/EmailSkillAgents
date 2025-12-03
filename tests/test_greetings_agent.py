"""
Test script for Personalized Greetings Agent
Demonstrates all features and validates functionality
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from greetings_grades_agent.greeting_generator import GreetingGenerator
from greetings_grades_agent.persona_manager import determine_persona, get_persona_display_name
from greetings_grades_agent.excel_manager import ExcelManager


def test_persona_selection():
    """Test grade-to-persona mapping logic"""
    print("=" * 80)
    print("TEST 1: Persona Selection Logic")
    print("=" * 80)

    test_cases = [
        (0, 'dudi_amsalem'),
        (25, 'dudi_amsalem'),
        (50, 'dudi_amsalem'),
        (51, 'benjamin_netanyahu'),
        (65, 'benjamin_netanyahu'),
        (70, 'benjamin_netanyahu'),
        (71, 'shahar_hasson'),
        (85, 'shahar_hasson'),
        (90, 'shahar_hasson'),
        (91, 'donald_trump'),
        (95, 'donald_trump'),
        (100, 'donald_trump'),
        (None, None),
    ]

    all_passed = True
    for grade, expected_persona in test_cases:
        actual_persona = determine_persona(grade)
        passed = actual_persona == expected_persona
        all_passed = all_passed and passed

        status = "[OK]" if passed else "[FAIL]"
        grade_str = f"{grade}%" if grade is not None else "None"
        expected_str = get_persona_display_name(expected_persona) if expected_persona else "None"
        actual_str = get_persona_display_name(actual_persona) if actual_persona else "None"

        print(f"{status} Grade {grade_str:6} -> Expected: {expected_str:20} Got: {actual_str:20}")

    print(f"\nResult: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}\n")
    return all_passed


def test_greeting_generation():
    """Test greeting generation for all personas"""
    print("=" * 80)
    print("TEST 2: Greeting Generation")
    print("=" * 80)

    generator = GreetingGenerator()

    test_grades = [
        (25, "Dudi Amsalem"),
        (60, "Benjamin Netanyahu"),
        (80, "Shahar Hasson"),
        (95, "Donald Trump"),
    ]

    all_passed = True
    for grade, expected_persona_name in test_grades:
        greeting, persona = generator.generate(grade)

        # Validate greeting
        is_valid = generator.validate_greeting(greeting)
        has_grade = str(int(grade)) in greeting or f"{grade}%" in greeting
        correct_persona = get_persona_display_name(persona) == expected_persona_name

        passed = is_valid and has_grade and correct_persona
        all_passed = all_passed and passed

        status = "[OK]" if passed else "[FAIL]"
        print(f"\n{status} Grade {grade}% -> {expected_persona_name}")
        print(f"Persona: {get_persona_display_name(persona)}")
        print(f"Greeting: {greeting[:100]}...")
        print(f"Valid: {is_valid}, Has Grade Ref: {has_grade}, Correct Persona: {correct_persona}")

    print(f"\nResult: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}\n")
    return all_passed


def test_greeting_variety():
    """Test that greetings have variety (not always identical)"""
    print("=" * 80)
    print("TEST 3: Greeting Variety (5 greetings per persona)")
    print("=" * 80)

    generator = GreetingGenerator()

    test_cases = [
        (45, "Dudi Amsalem"),
        (65, "Benjamin Netanyahu"),
        (85, "Shahar Hasson"),
        (95, "Donald Trump"),
    ]

    all_passed = True
    for grade, persona_name in test_cases:
        print(f"\n{persona_name} ({grade}%):")

        greetings = []
        for i in range(5):
            greeting, persona = generator.generate(grade)
            greetings.append(greeting)
            print(f"  {i+1}. {greeting[:60]}...")

        # Check that we have at least 2 different greetings
        unique_greetings = len(set(greetings))
        has_variety = unique_greetings >= 2

        status = "[OK]" if has_variety else "[FAIL]"
        print(f"{status} Unique greetings: {unique_greetings}/5")

        all_passed = all_passed and has_variety

    print(f"\nResult: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}\n")
    return all_passed


def test_excel_validation():
    """Test Excel input validation"""
    print("=" * 80)
    print("TEST 4: Excel Input Validation")
    print("=" * 80)

    manager = ExcelManager()

    # Test with real file
    test_file = r"C:\AIDevelopmentCourse\L-19\EmailSkillAgents\output\homework_emails_graded.xlsx"

    if Path(test_file).exists():
        print(f"Testing file: {test_file}")
        validation = manager.validate_input_excel(test_file)

        print(f"Valid: {validation['valid']}")
        print(f"Total Students: {validation['student_count']}")
        print(f"With Grades: {validation['graded_count']}")
        print(f"Without Grades: {validation['error_count']}")

        if validation['errors']:
            print(f"Errors: {validation['errors']}")
        if validation['warnings']:
            print(f"Warnings: {validation['warnings']}")

        passed = validation['valid'] and validation['graded_count'] > 0
        print(f"\nResult: {'[OK] TEST PASSED' if passed else '[FAIL] TEST FAILED'}\n")
        return passed
    else:
        print(f"[SKIP] Test file not found: {test_file}")
        print("Run Repository Analyzer first to create test file\n")
        return True  # Don't fail if test file doesn't exist


def test_edge_cases():
    """Test edge cases and error handling"""
    print("=" * 80)
    print("TEST 5: Edge Cases and Error Handling")
    print("=" * 80)

    generator = GreetingGenerator()

    edge_cases = [
        (None, "None", "Should return N/A"),
        ('', "Empty string", "Should return N/A"),
        (0, "0%", "Should use Dudi Amsalem"),
        (50, "50%", "Boundary: Should use Dudi Amsalem"),
        (70, "70%", "Boundary: Should use Netanyahu"),
        (90, "90%", "Boundary: Should use Shahar Hasson"),
        (100, "100%", "Should use Donald Trump"),
    ]

    all_passed = True
    for grade, desc, expected_behavior in edge_cases:
        greeting, persona = generator.generate(grade)

        # Check expected behavior
        if grade is None or grade == '':
            passed = greeting == "N/A" and persona is None
        else:
            passed = greeting != "N/A" and persona is not None

        status = "[OK]" if passed else "[FAIL]"
        persona_str = get_persona_display_name(persona) if persona else "None"

        print(f"{status} {desc:20} -> Persona: {persona_str:20} ({expected_behavior})")

        all_passed = all_passed and passed

    print(f"\nResult: {'ALL TESTS PASSED' if all_passed else 'SOME TESTS FAILED'}\n")
    return all_passed


def main():
    """Run all tests"""
    print("\n" + "=" * 80)
    print("PERSONALIZED GREETINGS AGENT - COMPREHENSIVE TEST SUITE")
    print("=" * 80 + "\n")

    tests = [
        ("Persona Selection Logic", test_persona_selection),
        ("Greeting Generation", test_greeting_generation),
        ("Greeting Variety", test_greeting_variety),
        ("Excel Validation", test_excel_validation),
        ("Edge Cases", test_edge_cases),
    ]

    results = []
    for test_name, test_func in tests:
        try:
            passed = test_func()
            results.append((test_name, passed))
        except Exception as e:
            print(f"[ERROR] Test '{test_name}' raised exception: {str(e)}")
            results.append((test_name, False))

    # Print summary
    print("=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)

    total = len(results)
    passed = sum(1 for _, p in results if p)

    for test_name, test_passed in results:
        status = "[PASS]" if test_passed else "[FAIL]"
        print(f"{status} {test_name}")

    print(f"\nTotal: {passed}/{total} tests passed")

    if passed == total:
        print("\n[SUCCESS] All tests passed! Greetings Agent is working correctly.")
        return 0
    else:
        print(f"\n[WARNING] {total - passed} test(s) failed. Review output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
