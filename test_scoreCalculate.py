import pytest
from scoreCalculate import scoreCalculator
import tkinter as tk

def create_score_calculator():
    root = tk.Tk()  # Create the root Tkinter window
    app = scoreCalculator(root)  # Create an instance of the scoreCalculator
    return app

def test_calculate_level():
    calculator = create_score_calculator()

    assert calculator.calculate_level(95, 100) == 'A'
    assert calculator.calculate_level(85, 100) == 'B'
    assert calculator.calculate_level(75, 100) == 'C'
    assert calculator.calculate_level(65, 100) == 'D'
    assert calculator.calculate_level(55, 100) == 'F'

def test_calculate_example1():
    # Sample Output 1
    calculator = create_score_calculator()

    calculator.student_names.append(tk.StringVar(value="1"))
    calculator.score_entries.append(tk.StringVar(value="70"))

    calculator.calculate()

    expected_result_text = "Best Score: 70\nStudent 1: Score 70, Grade A"

    assert calculator.result_text.get() == expected_result_text

def test_calculate_example2():
    # Sample Output 2
    calculator = create_score_calculator()

    calculator.student_names.append(tk.StringVar(value="1"))
    calculator.student_names.append(tk.StringVar(value="2"))
    calculator.student_names.append(tk.StringVar(value="3"))

    calculator.score_entries.append(tk.StringVar(value="55"))
    calculator.score_entries.append(tk.StringVar(value="40"))
    calculator.score_entries.append(tk.StringVar(value="70"))

    calculator.calculate()

    expected_result_text = (
        "Best Score: 70\n"
        "Student 1: Score 55, Grade B\n"
        "Student 2: Score 40, Grade C\n"
        "Student 3: Score 70, Grade A"
    )

    assert calculator.result_text.get() == expected_result_text


def test_calculate_example3():
    # Sample Output 3
    calculator = create_score_calculator()

    calculator.student_names.append(tk.StringVar(value="1"))
    calculator.student_names.append(tk.StringVar(value="2"))
    calculator.student_names.append(tk.StringVar(value="3"))

    calculator.score_entries.append(tk.StringVar(value="40"))
    calculator.score_entries.append(tk.StringVar(value="55"))
    calculator.score_entries.append(tk.StringVar(value="70"))

    calculator.calculate()

    expected_result_text = (
        "Best Score: 70\n"
        "Student 1: Score 40, Grade C\n"
        "Student 2: Score 55, Grade B\n"
        "Student 3: Score 70, Grade A"
    )

    assert calculator.result_text.get() == expected_result_text


def test_calculate_example4():
    # Sample Output 4
    calculator = create_score_calculator()

    calculator.student_names.append(tk.StringVar(value="1"))
    calculator.student_names.append(tk.StringVar(value="2"))

    calculator.score_entries.append(tk.StringVar(value="7"))
    calculator.score_entries.append(tk.StringVar(value="100"))

    calculator.calculate()

    expected_result_text = (
        "Best Score: 100\n"
        "Student 1: Score 7, Grade F\n"
        "Student 2: Score 100, Grade A"
    )

    assert calculator.result_text.get() == expected_result_text

