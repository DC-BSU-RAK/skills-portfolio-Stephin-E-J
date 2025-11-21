import tkinter as tk
from tkinter import messagebox
import random

class GoogleAssistant:
    def __init__(self, alexa):
        self.alexa = alexa
        self.alexa.title("Alexa")
        self.alexa.geometry("500x300")        
        
        self.jokes = self.random_joke()
                
    
        self.create_widgets()
        
    
    def random_joke(self):
        with open('randomJokes.txt','r') as file:
            jokes = file.readlines()
        return [joke.strip() for joke in jokes if joke.strip()]

    def create_widgets(self):
        
        title_label = tk.Label(self.alexa, text="Alexa")
        title_label.pack(pady=10)
        
        
        self.setup_label = tk.Label(self.alexa, text="", font=("Arial", 12), 
                                    justify="center")
        self.setup_label.pack(pady=10)
        
        
        self.punchline_label = tk.Label(self.alexa, text="", 
                                       font=("Arial", 12, "italic"), 
                                       fg="darkgreen",
                                       wraplength=450, 
                                       justify="center")
        self.punchline_label.pack(pady=10)
        
        
        button_frame = tk.Frame(self.alexa)
        button_frame.pack(pady=20)
        
        
        self.joke_button = tk.Button(button_frame, text="Alexa tell me a Joke", 
                                    font=("Arial", 12, "bold"),
                                    bg="lightblue",
                                    command=self.get_random_joke)
        self.joke_button.grid(row=0, column=0, padx=5, pady=5)
        
        
        self.punchline_button = tk.Button(button_frame, text="Show Punchline", 
                                         font=("Arial", 12),
                                         bg="lightgreen",
                                         command=self.show_punchline)
        self.punchline_button.grid(row=0, column=1, padx=5, pady=5)
        
        
        self.next_button = tk.Button(button_frame, text="Next Joke", 
                                    font=("Arial", 12),
                                    bg="lightyellow",
                                    command=self.get_random_joke)
        self.next_button.grid(row=1, column=0, padx=5, pady=5)
        
    
    def get_random_joke(self):
        if not self.jokes:
            messagebox.showerror("Error", "No jokes available!")
            return
        
       
        random_joke = random.choice(self.jokes)
        
        
        if "?" in random_joke:
            parts = random_joke.split("?", 1)
            self.current_setup = parts[0] + "?"
            self.current_punchline = parts[1] if len(parts) > 1 else ""
        else:
            
            self.current_setup = random_joke
            self.current_punchline = "No punchline available"
        
        
        self.setup_label.config(text=self.current_setup)
        self.punchline_label.config(text="")
        
        
        self.punchline_button.config(state="normal")
    
    def show_punchline(self):
        self.punchline_label.config(text=self.current_punchline)
        
        self.punchline_button.config(state="disabled")

def main():
    alexa = tk.Tk()
    app = GoogleAssistant(alexa)
    alexa.mainloop()

if __name__ == "__main__":
    main()