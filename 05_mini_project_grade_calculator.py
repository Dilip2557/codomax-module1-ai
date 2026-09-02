"""
05_mini_project_grade_calculator.py
Mini Project: Student Grade Calculator
Combines variables, functions, loops, and lists.
"""

def calculate_grade(score):
    """Return a letter grade based on numeric score."""
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "F"


def process_students(student_scores):
    """Take a dict of {name: score} and print a report."""
    print(f"{'Name':<10}{'Score':<10}{'Grade':<10}")
    print("-" * 30)

    total = 0
    for name, score in student_scores.items():
        grade = calculate_grade(score)
        print(f"{name:<10}{score:<10}{grade:<10}")
        total += score

    average = total / len(student_scores)
    print("-" * 30)
    print(f"Class Average: {average:.2f}")


# Sample data - list of students with scores
student_scores = {
    "Riya": 92,
    "Karan": 67,
    "Meena": 45,
    "Aditya": 78,
    "Zoya": 30,
}

process_students(student_scores)
