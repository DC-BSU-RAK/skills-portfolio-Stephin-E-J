import tkinter as tk
from tkinter import messagebox
import random

class GoogleAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Alexa")
        self.root.geometry("500x300")        
        
        self.jokes = self.load_jokes()
                
        self.current_setup = ""
        self.current_punchline = ""
        
        self.create_widgets()
        
        self.get_random_joke()
    
    def joke(self):
        with open('randomJokes.txt','r') as file:
            jokes = file.read
            print(jokes)

    def create_widgets(self):
        
        title_label = tk.Label(self.root, text="Alexa", 
                              font=("Arial", 16, "bold"), fg="blue")
        title_label.pack(pady=10)
        
        
        self.setup_label = tk.Label(self.root, text="", 
                                   font=("Arial", 12), 
                                   wraplength=450, 
                                   justify="center")
        self.setup_label.pack(pady=10)
        
        
        self.punchline_label = tk.Label(self.root, text="", 
                                       font=("Arial", 12, "italic"), 
                                       fg="darkgreen",
                                       wraplength=450, 
                                       justify="center")
        self.punchline_label.pack(pady=10)
        
        
        button_frame = tk.Frame(self.root)
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
    
    def quit_application(self):
        if messagebox.askokcancel("Quit", "Do you want to quit the application?"):
            self.root.destroy()

def main():
    root = tk.Tk()
    app = GoogleAssistant(root)
    root.mainloop()

if __name__ == "__main__":
    main()