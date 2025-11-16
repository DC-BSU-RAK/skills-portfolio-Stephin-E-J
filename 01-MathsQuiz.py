from tkinter import *
import tkinter as tk
import random

class MathsQuizProject:
    def __init__(self, quiz):
        self.quiz = quiz
        self.quiz.title("Math's Quiz")
        self.quiz.geometry("500x500")

        self.difficulty= None
        self.score = 0
        self.question_count = 0
        self.attempts = 0 
        self.num1 = 0
        self.num2 = 0
        self.operation = ''

        self.front_menu()

    def clear_screen(self):
        for widget in self.quiz.winfo_children():
            widget.destroy()

    def front_menu(self):
        self.clear_screen()

        tk.Label(self.quiz, text="Maths Quiz", font=('Goudy Stout', 35)).pack(pady=20)
        
        tk.Button(self.quiz, text="Easy", font=('Goudy Stout'),
                  command=lambda: self.start_button("easy"), width=15).pack()
        tk.Button(self.quiz, text="Moderate", font=('Goudy Stout'),
                  command=lambda: self.start_button("moderate"), width=15).pack()
        tk.Button(self.quiz, text="Advanced", font=('Goudy Stout'),
                  command=lambda: self.start_button("advanced"), width=15).pack()
        
        
    def randomInt(quiz, difficulty):
        if difficulty == "easy":
            return random.randint(0,9)
        elif difficulty == "moderate":
            return random.randint(10, 99)
        else:
            return random.randint(1000, 9999)
    
    def decideCalculation(quiz):
        return random.choice(['+','-'])
    
    def next_question(self):
        self.clear_screen()

        tk.Label(self.quiz, text=f"Score: {self.score}", font=('Goudy Stout', 16)).pack(pady=5)
        tk.Label(self.quiz, text=f"Question {self.question_count + 1}/10", font=('Goudy Stout', 14)).pack()
    

        self.num1 = quiz.randomInt(quiz.difficulty)
        self.num2 = quiz.randomInt(quiz.difficulty)
        self.operation = quiz.decideCalculation()

        if self.operation == '-' and self.num1 < self.num2:
            self.num1, self.num2 = self.num2, self.num1

        problem_text = f"{self.num1} {self.operation} {self.num2} = ?"
        tk.Label(self.quiz, text= problem_text, font= ('Goudy Stout', 30, 'bold')).pack()

        self.answer_entry = tk.Entry(self.quiz, font=('Goudy Stout', 20), width= 10)
        self.answer_entry.pack(pady=20)
        self.answer_entry.focus()

        tk.Button(self.quiz, text="Submit", font=('Goudy Stout', 16), command=self.check_answer).pack(pady=10)

    def check_answer(self):
        try:
            user_answer = int(self.answer_entry.get())
        except:
            return
        
        if self.operation == '+':
            correct_answer = self.num1 + self.num2
        else:
            correct_answer = self.num1 + self.num2

        if user_answer == correct_answer:
            self.score += 10

        self.question_count += 1

        if self.question_count < 10:
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.clear_screen()

        grade = self.calculate_grade()

        tk.Label(self.quiz, text="Completed Quiz!", 
                font=('Goudy Stout', 26,'bold')).pack(pady=30)
        tk.Label(self.quiz, text=f"Final Score: {self.score}/100", font=('Goudy Stout', 22)).pack(pady=10)
        tk.Label(self.quiz, text= f"Grade: {grade}", font=('Goudy Stout', 22, 'bold')).pack(pady=10)

        tk.Button(self.quiz, text="Play Again", font=('Goudy Stout', 18), command=self.front_menu, width=12)


    def calculate_grade(self):
        if self.score >= 90:
            return "A+"
        elif self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        elif self.score >= 60:
            return "C"
        elif self.score >= 50:
            return "D"
        else:
            return "F"
        
if __name__ == "__main__":
    quiz = Tk()
    app= MathsQuizProject(quiz)
    quiz.mainloop()