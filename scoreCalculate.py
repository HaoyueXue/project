# Topic: Grade Calculator
# Name: Haoyue Xue
# Date: 8/17/2024
# Detail: he application allows the user to
#         dynamically add up to 10 students, input their names
#         and scores, and calculate their corresponding grades
#         based on the best score among all students.

import tkinter as tk
from tkinter import messagebox
from typing import List

class scoreCalculator:
    def __init__(self, root):
        """
        Initializes the GradeCalculator application with a GUI.

        Args:
            root (tk.Tk): The root window of the tkinter GUI.
        """
        self.root = root
        self.root.title("Grade Calculator")
        self.root.geometry("500x400")

        self.student_names = []
        self.score_entries = []

        self.create_window()

    # Create the window
    def create_window(self):
        """
        Creates the GUI windows, including buttons, labels, and entry fields.
        """
        # Title
        title_label = tk.Label(self.root, text="Grades Calculator", font=("Helvetica", 16))
        title_label.pack(side="top", pady=10)

        # Frame for student entries
        self.student_frame = tk.Frame(self.root)
        self.student_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.add_student_button = tk.Button(self.root, text="Add Student", command=self.add_student)
        self.add_student_button.pack(side="top", pady=5)

        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate)
        self.calculate_button.pack(side="top", pady=5)

        self.result_text = tk.StringVar()
        self.result_label = tk.Label(self.root, textvariable=self.result_text, justify="left")
        self.result_label.pack(side="top", pady=10)

    # Calculate the level
    def calculate_level(self, score: int, best_score: int) -> str:
        """
        Calculate the grade level based on the score relative to the best score.

        Args:
            score (int): The score of the student.
            best_score (int): The highest score among all students.

        Returns:
            str: The grade level ('A' to 'F') based on the score.
        """
        if score >= best_score - 10:
            return 'A'
        elif score >= best_score - 20:
            return 'B'
        elif score >= best_score - 30:
            return 'C'
        elif score >= best_score - 40:
            return 'D'
        else:
            return 'F'

    # Find the best scores
    def calculate_grades(self, scores: List[int]) -> List[str]:
        """
        Calculate grades for each score in the list.

        Args:
            scores (List[int]): A list of student scores.

        Returns:
            List[str]: A list of grades corresponding to the scores.
        """
        best_score = max(scores)
        return [self.calculate_level(score, best_score) for score in scores]

    # Calculate the level for each student
    def calculate(self):
        """
        Event handler for the 'Calculate' button click.
        Validates input, calculates grades, and displays the results.
        """
        try:
            scores = []
            for entry in self.score_entries:
                score = int(entry.get())
                if not (0 <= score <= 100):
                    raise ValueError("Scores must be between 0 and 100.")
                scores.append(score)

            grades = self.calculate_grades(scores)
            best_score = max(scores)
            result_lines = [
                f"Student {self.student_names[i].get()}: Score {scores[i]}, Grade {grades[i]}"
                for i in range(len(scores))
            ]
            self.result_text.set(f"Best Score: {best_score}\n" + "\n".join(result_lines))
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid integer scores between 0 and 100.")

    # Add student button
    def add_student(self):
        """
        Event handler for the 'Add Student' button click.
        Adds a new student entry row for name and score.
        """
        if len(self.score_entries) < 10:
            row = len(self.student_names)
            student_name_var = tk.StringVar()
            self.student_names.append(student_name_var)
            student_score_var = tk.StringVar()

            tk.Label(self.student_frame, text=f"Student {row + 1} Name:").grid(row=row, column=0, sticky="w")
            tk.Entry(self.student_frame, textvariable=student_name_var).grid(row=row, column=1, padx=5)

            tk.Label(self.student_frame, text="Score:").grid(row=row, column=2, sticky="w")
            score_entry = tk.Entry(self.student_frame, textvariable=student_score_var)
            score_entry.grid(row=row, column=3, padx=5)
            self.score_entries.append(score_entry)
        else:
            messagebox.showwarning("Limit Reached", "You can only add up to 10 students.")

if __name__ == "__main__":
    root = tk.Tk()
    app = scoreCalculator(root)
    root.mainloop()
