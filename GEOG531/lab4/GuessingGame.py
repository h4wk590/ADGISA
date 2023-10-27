import tkinter as tk
import random

# Initialize global variables
random_number = 0
guesses = 0

# Create the main window
frmGuessGame = tk.Tk()
frmGuessGame.title("Number Guessing Game")
frmGuessGame.geometry("300x300")

# Function to start a new game
def new_game():
    global random_number, guesses
    random_number = random.randint(1, 10)
    guesses = 0
    txtOutput.delete(0, tk.END)  # Clear previous game's output
    txtUserEntry.config(state="normal")
    btnGuess.config(state="normal")
    lblResult.config(text="")
    txtUserEntry.delete(0, tk.END)

# Function to handle a guess
def guess_number():
    global guesses
    user_guess = int(txtUserEntry.get())

    if user_guess < random_number:
        result = "Too Low!"
    elif user_guess > random_number:
        result = "Too High!"
    else:
        result = "You're Right!"
        txtUserEntry.config(state="disable")
        btnGuess.config(state="disable")

    txtOutput.insert(tk.END, f"Guess {guesses + 1}: {user_guess} - {result}\n")
    guesses += 1
    lblResult.config(text=result)

# Create and pack the widgets
txtOutput = tk.Listbox(frmGuessGame, height=5, width=30)
txtOutput.pack(pady=10)

lblInstruction = tk.Label(frmGuessGame, text="Guess a number between 1 and 10:")
lblInstruction.pack()

txtUserEntry = tk.Entry(frmGuessGame)
txtUserEntry.pack()

lblResult = tk.Label(frmGuessGame, text="", font=("Arial", 12, "bold"))
lblResult.pack()

btnNewGame = tk.Button(frmGuessGame, text="Start a New Game", command=new_game)
btnNewGame.pack(pady=5)

btnGuess = tk.Button(frmGuessGame, text="Guess", command=guess_number)
btnGuess.pack(pady=5)

new_game()  # Start a new game initially

frmGuessGame.mainloop()
