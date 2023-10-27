'''
Author: Aidan Brown
GEOG 531 Fall 2023
'''

# Import TKinter and Random modules
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
def New_Game():
    global intRandomNum, intGuesses # Referencethe two global variables
    intRandomNum = random.randint(1, 10) # Set random number range
    intGuesses = 0 # Start the guess count at 0
    lboOutput.delete(0, tk.END)  # Clear previous game's output
    txtUserGuess.config(state="normal") 
    btnGuess.config(state="normal") # Game state when user clicks on the guess button
    txtUserGuess.delete(0, tk.END) # Clear the text box 

# Function to guess the number
def Guess_Click():
    global intGuesses # Use the guesses global variable
    intUserGuess = int(txtUserGuess.get()) # Read user input as int

    if intUserGuess < intRandomNum: # If the number is less than the random number 
        txtresult = "Too low!" # Return text "Too Low!"
    elif intUserGuess > intRandomNum: # Else if the users guess is greater than the random numver
        txtresult = "Too high!" # Return text "Too High!"
    else:
        txtresult = "You're Right!" # Return the txtresult when number is correct
        # Turn the game state off when user guesses the right number
        txtUserGuess.config(state="disable") 
        btnGuess.config(state="disable")

    lboOutput.insert(tk.END, f"Guess {intGuesses + 1}: {intUserGuess} - {txtresult}\n") # F-string to output the 
    intGuesses += 1 # Iterate over the the guesses

# Create labels, text boxes, and buttons
lboOutput = tk.Listbox(frmGuessGame, height=15, width=40)
lboOutput.pack(pady=10)

lblUserGuess = tk.Label(frmGuessGame, text="Your Guess:")
lblUserGuess.place(x=25, y=300)

txtUserGuess = tk.Entry(frmGuessGame)
txtUserGuess.place(x=140, y=300)

# New game button
btnNewGame = tk.Button(frmGuessGame, text="Start a New Game", command=New_Game)
btnNewGame.place(x=140,y=350)

# Guess button
btnGuess = tk.Button(frmGuessGame, text="Guess", command=Guess_Click, justify="center")
btnGuess.place(x=25,y=350)

# Setup new game
New_Game()

# Loop through main window
frmGuessGame.mainloop()
