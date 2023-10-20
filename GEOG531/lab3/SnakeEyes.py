'''
Author: Aidan Brown
GEOG 531
Snake Eyes dice rolling game
'''

# Import TKinter and Random modules
import tkinter as tk
import random

# Create the main window
frmSnakeEyes = tk.Tk()

# Create title of form
frmSnakeEyes.title("Snake Eyes Dice Roller")

# Create the dimensions of form
frmSnakeEyes.geometry("300x500")

# Function to roll the dice. 
def rollDice(): 
    intCount = 0 # Start the count at 0
    lstRolls = [] # Empty list to hold rolls
    # Clear the listbox
    lboOutput.delete(0, tk.END) 
    # While true - store random number from 1 - 6 on each die (intDie1, intDie2)
    # Iterate over the count and append each role to the list box 
    # stop program when each die is equal to int of 1
    while True:
        intDie1 = random.randint(1, 6)
        intDie2 = random.randint(1, 6)
        intCount += 1 # Iterate over the dice once (rolling the dice once)
        # strRoll variable to output the rolls in readable format using f-string
        strRoll = f"Roll {intCount}: {intDie1}, {intDie2}"
        lstRolls.append(strRoll)
         # For each value in the list, output the values into the list box.
        for rolls in lstRolls:
            lboOutput.insert(tk.END, rolls)

        if intDie1 == 1 and intDie2 == 1:
            lblRollCount.config(text=f"Number of Rolls: {intCount}") # Formatting the number of rolls it takes to get snake eyes using F-string
            break # Stop program when the conditions are met

# Create the listbox for output
lboOutput = tk.Listbox(frmSnakeEyes, width=40, height=25)
lboOutput.pack(pady=20)

# Create a button to strRoll the dice
btnRollDice = tk.Button(frmSnakeEyes, text="Roll Dice", command=rollDice)
btnRollDice.pack()

# Create a label to display the number of lstRolls
lblRollCount = tk.Label(frmSnakeEyes, text="")
lblRollCount.pack()

# Looping of main window
frmSnakeEyes.mainloop()
