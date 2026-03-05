import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Function to compute the weighted average and determine the grade
def compute_grade():
    try:
        # Fetch the values entered by the user
        student_id = student_id_entry.get()
        student_name = student_name_entry.get()
        course = course_combobox.get()
        subject = subject_entry.get()
        prelim_grade = float(prelim_grade_entry.get())
        midterm_grade = float(midterm_grade_entry.get())
        final_grade = float(final_grade_entry.get())

        # Check if grades are within the valid range
        if not (0 <= prelim_grade <= 100 and 0 <= midterm_grade <= 100 and 0 <= final_grade <= 100):
            raise ValueError("Grades must be between 0 and 100.")

        # Calculate the weighted average
        average = (prelim_grade * 0.30) + (midterm_grade * 0.30) + (final_grade * 0.40)

        # Determine the numerical grade and remarks
        if 97 <= average <= 100:
            numerical = 1.00
            remark = "Excellent"
        elif 94 <= average <= 96:
            numerical = 1.25
            remark = "Very Good"
        elif 91 <= average <= 93:
            numerical = 1.50
            remark = "Very Good"
        elif 88 <= average <= 90:
            numerical = 1.75
            remark = "Above Average"
        elif 85 <= average <= 87:
            numerical = 2.00
            remark = "Above Average"
        elif 82 <= average <= 84:
            numerical = 2.25
            remark = "Above Average"
        elif 79 <= average <= 81:
            numerical = 2.50
            remark = "Average"
        elif 76 <= average <= 78:
            numerical = 2.75
            remark = "Average"
        elif 75 <= average <= 75:
            numerical = 3.00
            remark = "Passing"
        elif 72 <= average <= 74:
            numerical = 3.25
            remark = "Conditional"
        elif 69 <= average <= 71:
            numerical = 3.50
            remark = "Conditional"
        elif 66 <= average <= 68:
            numerical = 3.75
            remark = "Failed"
        elif 65 <= average <= 65:
            numerical = 4.00
            remark = "Failed"
        else:
            numerical = 5.00
            remark = "Failed"

        # Display the results in the output section
        avg_label.config(text=f"Computed Average: {average:.2f}")
        numerical_label.config(text=f"Numerical Grade: {numerical}")
        remarks_label.config(text=f"Remarks: {remark}")

    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")


# Function to clear all the input fields
def clear_fields():
    student_id_entry.delete(0, tk.END)
    student_name_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    prelim_grade_entry.delete(0, tk.END)
    midterm_grade_entry.delete(0, tk.END)
    final_grade_entry.delete(0, tk.END)
    course_combobox.set('')
    avg_label.config(text="Computed Average:")
    numerical_label.config(text="Numerical Grade:")
    remarks_label.config(text="Remarks:")


# Setting up the main window
window = tk.Tk()
window.title("Student Grading System")
window.geometry("500x450")
window.config(bg="#f0f0f0")  # Background color

# Header Label
header_label = tk.Label(window, text="Student Grading System", font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white")
header_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

# Labels and Entry Fields for Student Details
tk.Label(window, text="Student ID", font=("Helvetica", 10), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5,
                                                                               sticky="e")
student_id_entry = tk.Entry(window, font=("Helvetica", 10))
student_id_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Student Name", font=("Helvetica", 10), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=5,
                                                                                 sticky="e")
student_name_entry = tk.Entry(window, font=("Helvetica", 10))
student_name_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(window, text="Course", font=("Helvetica", 10), bg="#f0f0f0").grid(row=3, column=0, padx=10, pady=5, sticky="e")
course_combobox = ttk.Combobox(window, font=("Helvetica", 10), state="readonly")
course_combobox["values"] = [
    "BTLED", "BTVTEd", "BSA", "BSCE", "BSECE", "BSEE", "BSME", "BSCpE", "BSGE", "BSDS",
    "BSIT", "BSTCM", "BSAP", "BSAM", "BSCHEM", "BSES", "BSFT", "BSAUTOTRONICS", "BSET",
    "BSESM", "BSEMT", "BSMET", "BSCS"
]
course_combobox.set('Select Course')
course_combobox.grid(row=3, column=1, padx=10, pady=5)

tk.Label(window, text="Subject", font=("Helvetica", 10), bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=5,
                                                                            sticky="e")
subject_entry = tk.Entry(window, font=("Helvetica", 10))
subject_entry.grid(row=4, column=1, padx=10, pady=5)

# Labels and Entry Fields for Grades
tk.Label(window, text="Prelim Grade", font=("Helvetica", 10), bg="#f0f0f0").grid(row=5, column=0, padx=10, pady=5,
                                                                                 sticky="e")
prelim_grade_entry = tk.Entry(window, font=("Helvetica", 10))
prelim_grade_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(window, text="Midterm Grade", font=("Helvetica", 10), bg="#f0f0f0").grid(row=6, column=0, padx=10, pady=5,
                                                                                  sticky="e")
midterm_grade_entry = tk.Entry(window, font=("Helvetica", 10))
midterm_grade_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(window, text="Final Grade", font=("Helvetica", 10), bg="#f0f0f0").grid(row=7, column=0, padx=10, pady=5,
                                                                                sticky="e")
final_grade_entry = tk.Entry(window, font=("Helvetica", 10))
final_grade_entry.grid(row=7, column=1, padx=10, pady=5)

# Compute and Clear Buttons
compute_button = tk.Button(window, text="Compute", font=("Helvetica", 12), bg="#4CAF50", fg="white",
                           command=compute_grade)
compute_button.grid(row=8, column=0, padx=10, pady=20, sticky="ew")

clear_button = tk.Button(window, text="Clear", font=("Helvetica", 12), bg="#FF5722", fg="white", command=clear_fields)
clear_button.grid(row=8, column=1, padx=10, pady=20, sticky="ew")

# Output Labels
avg_label = tk.Label(window, text="Computed Average:", font=("Helvetica", 10), bg="#f0f0f0")
avg_label.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

numerical_label = tk.Label(window, text="Numerical Grade:", font=("Helvetica", 10), bg="#f0f0f0")
numerical_label.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

remarks_label = tk.Label(window, text="Remarks:", font=("Helvetica", 10), bg="#f0f0f0")
remarks_label.grid(row=11, column=0, columnspan=2, padx=10, pady=5)

# Run the application
window.mainloop()
