import tkinter as tk
from tkinter import ttk, messagebox

dataset = []

# ---------------- COMPUTE FUNCTION ---------------- #
def compute_grade():
    try:
        student_id = student_id_entry.get()
        student_name = student_name_entry.get()
        course = course_combobox.get()
        subject = subject_entry.get()

        prelim = float(prelim_entry.get())
        midterm = float(midterm_entry.get())
        final = float(final_entry.get())

        if not (0 <= prelim <= 100 and 0 <= midterm <= 100 and 0 <= final <= 100):
            raise ValueError("Grades must be between 0 and 100")

        average = (prelim * 0.30) + (midterm * 0.30) + (final * 0.40)

        if 97 <= average <= 100:
            numerical, remark = 1.00, "Excellent"
        elif 94 <= average <= 96:
            numerical, remark = 1.25, "Very Good"
        elif 91 <= average <= 93:
            numerical, remark = 1.50, "Very Good"
        elif 88 <= average <= 90:
            numerical, remark = 1.75, "Above Average"
        elif 85 <= average <= 87:
            numerical, remark = 2.00, "Above Average"
        elif 82 <= average <= 84:
            numerical, remark = 2.25, "Above Average"
        elif 79 <= average <= 81:
            numerical, remark = 2.50, "Average"
        elif 76 <= average <= 78:
            numerical, remark = 2.75, "Average"
        elif average == 75:
            numerical, remark = 3.00, "Passing"
        elif 72 <= average <= 74:
            numerical, remark = 3.25, "Conditional"
        elif 69 <= average <= 71:
            numerical, remark = 3.50, "Conditional"
        elif 66 <= average <= 68:
            numerical, remark = 3.75, "Failed"
        elif average == 65:
            numerical, remark = 4.00, "Failed"
        else:
            numerical, remark = 5.00, "Failed"

        avg_label.config(text=f"Computed Average: {average:.2f}")
        num_label.config(text=f"Numerical Grade: {numerical}")
        remark_label.config(text=f"Remarks: {remark}")

        data = (
            student_id, student_name, course, subject,
            prelim, midterm, final,
            f"{average:.2f}", numerical, remark
        )

        dataset.append(data)
        table.insert("", "end", values=data)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric grades.")


# ---------------- CLEAR FUNCTION ---------------- #
def clear_fields():
    student_id_entry.delete(0, tk.END)
    student_name_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    prelim_entry.delete(0, tk.END)
    midterm_entry.delete(0, tk.END)
    final_entry.delete(0, tk.END)
    course_combobox.set("Select Course")

    avg_label.config(text="Computed Average:")
    num_label.config(text="Numerical Grade:")
    remark_label.config(text="Remarks:")


# ---------------- WINDOW ---------------- #
window = tk.Tk()
window.title("Student Grading System")
window.geometry("1000x650")
window.configure(bg="#eef2f7")

# ---------------- HEADER ---------------- #
header = tk.Label(
    window,
    text="STUDENT GRADING SYSTEM",
    font=("Arial", 18, "bold"),
    bg="#1f4e79",
    fg="white",
    pady=10
)
header.pack(fill="x")

# ---------------- INPUT FRAME ---------------- #
input_frame = tk.Frame(window, bg="#eef2f7")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Student ID", bg="#eef2f7").grid(row=0, column=0, padx=10, pady=5)
student_id_entry = tk.Entry(input_frame)
student_id_entry.grid(row=0, column=1)

tk.Label(input_frame, text="Student Name", bg="#eef2f7").grid(row=1, column=0, padx=10, pady=5)
student_name_entry = tk.Entry(input_frame)
student_name_entry.grid(row=1, column=1)

tk.Label(input_frame, text="Course", bg="#eef2f7").grid(row=2, column=0, padx=10, pady=5)

course_combobox = ttk.Combobox(input_frame, state="readonly", width=27)
course_combobox["values"] = (
    "BTLED","BTVTEd","BSA","BSCE","BSECE","BSEE","BSME","BSCpE","BSGE",
    "BSDS","BSIT","BSTCM","BSAP","BSAM","BSCHEM","BSES","BSFT",
    "BSAUTOTRONICS","BSET","BSESM","BSEMT","BSMET","BSCS"
)
course_combobox.set("Select Course")
course_combobox.grid(row=2, column=1)

tk.Label(input_frame, text="Subject", bg="#eef2f7").grid(row=3, column=0, padx=10, pady=5)
subject_entry = tk.Entry(input_frame)
subject_entry.grid(row=3, column=1)

# ---------------- GRADES FRAME ---------------- #
grades_frame = tk.Frame(window, bg="#eef2f7")
grades_frame.pack(pady=10)

tk.Label(grades_frame, text="Prelim Grade", bg="#eef2f7").grid(row=0, column=0, padx=10)
prelim_entry = tk.Entry(grades_frame)
prelim_entry.grid(row=0, column=1)

tk.Label(grades_frame, text="Midterm Grade", bg="#eef2f7").grid(row=1, column=0, padx=10)
midterm_entry = tk.Entry(grades_frame)
midterm_entry.grid(row=1, column=1)

tk.Label(grades_frame, text="Final Grade", bg="#eef2f7").grid(row=2, column=0, padx=10)
final_entry = tk.Entry(grades_frame)
final_entry.grid(row=2, column=1)

# ---------------- BUTTONS ---------------- #
button_frame = tk.Frame(window, bg="#eef2f7")
button_frame.pack(pady=10)

compute_btn = tk.Button(
    button_frame, text="Compute Grade",
    bg="#2e8b57", fg="white",
    font=("Arial",10,"bold"),
    width=15,
    command=compute_grade
)
compute_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(
    button_frame, text="Clear",
    bg="#c0392b", fg="white",
    font=("Arial",10,"bold"),
    width=15,
    command=clear_fields
)
clear_btn.grid(row=0, column=1, padx=10)

# ---------------- RESULTS ---------------- #
result_frame = tk.Frame(window, bg="#eef2f7")
result_frame.pack(pady=5)

avg_label = tk.Label(result_frame, text="Computed Average:", font=("Arial",10,"bold"), bg="#eef2f7")
avg_label.pack()

num_label = tk.Label(result_frame, text="Numerical Grade:", font=("Arial",10,"bold"), bg="#eef2f7")
num_label.pack()

remark_label = tk.Label(result_frame, text="Remarks:", font=("Arial",10,"bold"), bg="#eef2f7")
remark_label.pack()

# ---------------- TABLE ---------------- #
columns = ("ID","Name","Course","Subject","Prelim","Midterm","Final","Average","Numerical","Remarks")

table_frame = tk.Frame(window)
table_frame.pack(pady=20)

table = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=90)

table.pack(side="left")

scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=table.yview)
scrollbar.pack(side="right", fill="y")

table.configure(yscrollcommand=scrollbar.set)

# ---------------- RUN ---------------- #
window.mainloop()
