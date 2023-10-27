import tkinter as tk
import random

# Setting guesses and the random number to 0 as variables
intRandomNum = 0
intGuesses = 0

# Create the form
frmGuessGame = tk.Tk()
frmGuessGame.title("Number Guessing Game")
frmGuessGame.geometry("300x400")

# Function to start a new game
def new_game():
    global intRandomNum, intGuesses # Referencethe two global variables
    intRandomNum = random.randint(1, 10) # Set random number range
    intGuesses = 0 # Start the guess count at 0
    lboOutput.delete(0, tk.END)  # Clear previous game's output
    txtUserGuess.config(state="normal") 
    btnGuess.config(state="normal")
    lblResult.config(text="")
    txtUserGuess.delete(0, tk.END)

# Function to handle a guess
def Guess_Click():
    global intGuesses
    intUserGuess = int(txtUserGuess.get())

    if intUserGuess < intRandomNum:
        result = "Too Low!"
    elif intUserGuess > intRandomNum:
        result = "Too High!"
    else:
        result = "You're Right!"
        txtUserGuess.config(state="disable")
        btnGuess.config(state="disable")

    lboOutput.insert(tk.END, f"Guess {intGuesses + 1}: {intUserGuess} - {result}\n")
    intGuesses += 1
    lblResult.config(text=result)

# Create labels and textboxes
lboOutput = tk.Listbox(frmGuessGame, height=15, width=40)
lboOutput.pack(pady=10)

lblUserGuess = tk.Label(frmGuessGame, text="Your Guess:")
lblUserGuess.place(x=25, y=300)

txtUserGuess = tk.Entry(frmGuessGame)
txtUserGuess.place(x=140, y=300)

lblResult = tk.Label(frmGuessGame, text=lboOutput)
lblResult.pack()

btnNewGame = tk.Button(frmGuessGame, text="Start a New Game", command=new_game)
btnNewGame.place(x=140,y=350)

btnGuess = tk.Button(frmGuessGame, text="Guess", command=Guess_Click, justify="center")
btnGuess.place(x=25,y=350)

new_game()  # Start a new game initially

frmGuessGame.mainloop()
