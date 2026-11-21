"""
Student Grade Calculator
Codomax Internship - Module 02: Python Mini Project
"""

SUBJECTS = ["English", "Mathematics", "Science", "Computer", "Social Science"]
PASS_MARKS = 35


def get_student_name():
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("Name cannot be empty. Please try again.")


def get_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            print("Please enter a mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_grade(percentage, has_failed):
    if has_failed:
        return "F (Fail)"
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    return "F (Fail)"


def main():
    print("=" * 48)
    print("          STUDENT GRADE CALCULATOR")
    print("=" * 48)

    student_name = get_student_name()
    marks = {}

    print("\nEnter marks for the following subjects:")
    for subject in SUBJECTS:
        marks[subject] = get_mark(subject)

    total = sum(marks.values())
    maximum_total = len(SUBJECTS) * 100
    percentage = (total / maximum_total) * 100
    has_failed = any(mark < PASS_MARKS for mark in marks.values())
    result = "FAIL" if has_failed else "PASS"
    grade = calculate_grade(percentage, has_failed)

    print("\n" + "=" * 48)
    print("                 MARKSHEET")
    print("=" * 48)
    print(f"Student Name : {student_name}")
    print("-" * 48)
    print(f"{'Subject':<22}{'Marks':>12}")
    print("-" * 48)

    for subject, mark in marks.items():
        print(f"{subject:<22}{mark:>12.1f}")

    print("-" * 48)
    print(f"{'Total':<22}{total:>12.1f} / {maximum_total}")
    print(f"{'Percentage':<22}{percentage:>11.2f}%")
    print(f"{'Result':<22}{result:>12}")
    print(f"{'Grade':<22}{grade:>12}")
    print("=" * 48)

    if result == "PASS":
        print("Congratulations! You passed.")
    else:
        print(f"You need at least {PASS_MARKS} marks in every subject to pass.")

    print("\nThank you for using Student Grade Calculator!")


if __name__ == "__main__":
    main()
