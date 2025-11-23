import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

def student_file():
    students = []

    with open("studentMarks.txt", "r") as file:
            lines = file.readlines()

    num_students = int(lines[0].strip())

    for line in lines[1:]:
            parts = line.strip().split(",")
            code = int(parts[0])
            name = parts[1]
            c1, c2, c3 = map(int, parts[2:5])
            exam = int(parts[5])

            coursework_total = c1 + c2 + c3
            total_marks = coursework_total + exam
            percentage = round((total_marks / 160) * 100, 2)

            if percentage >= 70:
                grade = "A"
            elif percentage >= 60:
                grade = "B"
            elif percentage >= 50:
                grade = "C"
            elif percentage >= 40:
                grade = "D"
            else:
                grade = "F"

            students.append({
            "code": code,
            "name": name,
            "coursework": coursework_total,
            "exam": exam,
            "percentage": percentage,
            "grade": grade
        })


    return students, num_students

class StudentManager:
    def __init__(self, manage):
        self.manage = manage
        self.manage.title("Student Manager")
        self.manage.geometry("650x500")

        self.students, self.count = student_file()

     
        menu_frame = tk.Frame(manage, padx=20, pady=20)
        menu_frame.pack(side="left", anchor="nw")

        tk.Label(menu_frame, text="Student Manager", font=("Arial", 18, "bold")).pack(pady=10, anchor="w")

        tk.Button(menu_frame, text="View ALL Student Records",
                  width=30, command=self.all_student).pack(pady=5, anchor="w")

        tk.Button(menu_frame, text="View Individual Student Record",
                  width=30, command=self.view_individual).pack(pady=5, anchor="w")

        tk.Button(menu_frame, text="Show Highest Overall Mark",
                  width=30, command=self.highesst_score).pack(pady=5, anchor="w")

        tk.Button(menu_frame, text="Show Lowest Overall Mark",
                  width=30, command=self.lowest_score).pack(pady=5, anchor="w")

        self.output = tk.Text(manage, height=18, width=90, wrap="word")
        self.output.pack(side="left", padx=10, pady=10)

    def display_student_details(self, s):
        return (
            f"Name: {s['name']}\n"
            f"Student Number: {s['code']}\n"
            f"Coursework Total: {s['coursework']} / 60\n"
            f"Exam Mark: {s['exam']} / 100\n"
            f"Percentage: {s['percentage']}%\n"
            f"Grade: {s['grade']}\n"
            f"{'-'*45}\n"
        )

    def all_student(self):
        self.output.delete("1.0", tk.END)

        total_percentage = 0
        self.output.insert(tk.END, "ALL STUDENT RECORDS\n")
        self.output.insert(tk.END, "-"*45 + "\n\n")

        for s in self.students:
            self.output.insert(tk.END, self.display_student_details(s))
            total_percentage += s["percentage"]

        average = round(total_percentage / len(self.students), 2)

        self.output.insert(tk.END, f"\nNumber of Students: {self.count}\n")
        self.output.insert(tk.END, f"Class Average Percentage: {average}%\n")

    def view_individual(self):
        student_code = simpledialog.askinteger("Select Student", "Enter Student Number:")

        if student_code is None:
            return

        for s in self.students:
            if s["code"] == student_code:
                self.output.delete("1.0", tk.END)
                self.output.insert(tk.END, "INDIVIDUAL STUDENT RECORD\n")
                self.output.insert(tk.END, "-"*45 + "\n\n")
                self.output.insert(tk.END, self.display_student_details(s))
                return

        messagebox.showerror("Not Found", "Student number not found!")

    def highesst_score(self):
        highest = max(self.students, key=lambda x: x["percentage"])
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "STUDENT WITH HIGHEST MARK\n")
        self.output.insert(tk.END, "-"*45 + "\n\n")
        self.output.insert(tk.END, self.display_student_details(highest))

    def lowest_score(self):
        lowest = min(self.students, key=lambda x: x["percentage"])
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, "STUDENT WITH LOWEST MARK\n")
        self.output.insert(tk.END, "-"*45 + "\n\n")
        self.output.insert(tk.END, self.display_student_details(lowest))


manage = tk.Tk()
app = StudentManager(manage)
manage.mainloop()
