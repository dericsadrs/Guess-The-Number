import tkinter as tk
from tkinter import messagebox
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

class NumberGuessingGameGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Number Guessing Game")
        self.create_widgets()
        self.answer = 0
        self.turns = 0

    def create_widgets(self):
        self.logo_label = tk.Label(self.window, text=logo, font=("Courier", 12, "bold"))
        self.instruction_label = tk.Label(self.window, text="Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nGuess the number.", font=("Helvetica", 10))
        self.difficulty_label = tk.Label(self.window, text="Choose a difficulty:")
        self.difficulty_var = tk.StringVar(value="easy")
        self.difficulty_radio_easy = tk.Radiobutton(self.window, text="Easy", variable=self.difficulty_var, value="easy")
        self.difficulty_radio_hard = tk.Radiobutton(self.window, text="Hard", variable=self.difficulty_var, value="hard")
        self.start_button = tk.Button(self.window, text="Start", command=self.start_game)
        self.guess_label = tk.Label(self.window, text="Enter your guess:")
        self.guess_entry = tk.Entry(self.window)
        self.guess_button = tk.Button(self.window, text="Guess", command=self.check_guess)
        self.result_label = tk.Label(self.window, text="", font=("Helvetica", 10, "bold"))
        self.trademark_label = tk.Label(self.window, text="Created by Deric C. San Andres", font=("Helvetica", 8, "italic"))

        self.logo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.instruction_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        self.difficulty_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)
        self.difficulty_radio_easy.grid(row=3, column=0, padx=5, pady=5)
        self.difficulty_radio_hard.grid(row=3, column=1, padx=5, pady=5)
        self.start_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.guess_label.grid(row=5, column=0, padx=5, pady=5)
        self.guess_entry.grid(row=5, column=1, padx=5, pady=5)
        self.guess_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        self.result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
        self.trademark_label.grid(row=8, column=0, columnspan=2, padx=10, pady=5)


    def start_game(self):
        self.result_label.config(text="")
        self.answer = randint(1, 100)
        self.turns = EASY_LEVEL_TURNS if self.difficulty_var.get() == "easy" else HARD_LEVEL_TURNS
        self.guess_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)

    def check_guess(self):
        guess = self.guess_entry.get()
        if not guess.isdigit():
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
            return

        guess = int(guess)
        if guess < 1 or guess > 100:
            messagebox.showerror("Error", "Invalid input. Please enter a number between 1 and 100.")
            return

        self.turns -= 1
        if guess == self.answer:
            self.result_label.config(text=f"Congratulations! You've guessed the number {self.answer}.")
            self.guess_button.config(state=tk.DISABLED)
            self.start_button.config(state=tk.NORMAL)
        elif self.turns == 0:
            self.result_label.config(text=f"You've run out of guesses. The correct number was {self.answer}.")
            self.guess_button.config(state=tk.DISABLED)
            self.start_button.config(state=tk.NORMAL)
        else:
            self.result_label.config(text=f"Too {'low' if guess < self.answer else 'high'}. {self.turns} attempts remaining.")

# Create an instance of the NumberGuessingGameGUI class
if __name__ == "__main__":
    game = NumberGuessingGameGUI()
    game.window.mainloop()
