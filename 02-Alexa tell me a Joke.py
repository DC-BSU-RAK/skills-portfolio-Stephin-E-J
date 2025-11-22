import tkinter as tk
from tkinter import messagebox
import random

class GoogleAssistant:
    def __init__(self, alexa):
        self.alexa = alexa
        self.alexa.title("Alexa tell me a Joke")
        self.alexa.geometry("500x300")       
        self.jokes = self.random_joke()
        self.buttons()
    
    def random_joke(self):
        with open('randomJokes.txt','r') as file:
            jokes = file.readlines()
        return [joke.strip() for joke in jokes if joke.strip()]

    def buttons(self):
        
        title_label = tk.Label(self.alexa, text="Alexa", font=("Arial",25))
        title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

        
        self.text_joke = tk.Label(self.alexa, text="", font=("Arial", 12), 
                                    justify="center")
        self.text_joke.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")
        
        
        self.punchline = tk.Label(self.alexa, text="", 
                                       font=("italic", 12), fg= "green",justify="center")
        self.punchline.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")
        
        button_frame = tk.Frame(self.alexa)
        button_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        self.joke_button = tk.Button(button_frame, text="Alexa tell me a Joke", font=("Arial", 12, "bold"),
                                    bg="maroon", command=self.get_random_joke)
        self.joke_button.grid(row=0, column=0, padx=5, pady=5)
        
        
        self.punchline_button = tk.Button(button_frame, text="Show Punchline", font=("Arial", 12),
                                         bg="lightgreen",
                                         command=self.show_punchline)
        self.punchline_button.grid(row=0, column=1, padx=5, pady=5)
        
        
        self.next_joke = tk.Button(button_frame, text="Next Joke", font=("Arial", 12),
                                    bg="lightyellow",
                                    command=self.get_random_joke)
        self.next_joke.grid(row=1, column=0, padx=5, pady=5)

        self.quit = tk.Button(button_frame, text="Quit", font=("Arial", 12),
                              bg="red", command=self.quit_tab)
        self.quit.grid(row=1, column=1, padx=5, pady=5)
        
    
    def get_random_joke(self):
        if not self.jokes:
            messagebox.showerror("Error", "No jokes available!")
            return
        
        random_joke = random.choice(self.jokes)
        
        if "?" in random_joke:
            parts = random_joke.split("?", 1)
            self.current_setup = parts[0] + "?"
            self.joke_punchline = parts[1] if len(parts) > 1 else ""
        else:            
            self.current_setup = random_joke
            self.joke_punchline = "No punchline available"
        
        
        self.text_joke.config(text=self.current_setup)
        self.punchline.config(text="")
        
        self.punchline_button.config(state="normal")
    
    def show_punchline(self):
        self.punchline.config(text=self.joke_punchline)
        
        self.punchline_button.config(state="disabled")

    def quit_tab(self):
        if messagebox.askokcancel("Quit","Do you want to quit the app?"):
            self.alexa.destroy()

def main():
    alexa = tk.Tk()
    app = GoogleAssistant(alexa)
    alexa.mainloop()

if __name__ == "__main__":
    main()