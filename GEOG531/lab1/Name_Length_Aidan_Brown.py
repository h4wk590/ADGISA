"""
Author: Aidan Brown
GEOG 531 - Fall 2023
Assignment 1 - Question 7   
"""

# Import tkinter module and messagebox
import tkinter as tk
from tkinter import messagebox

# Create main window using tk
FrmNameLength = tk.Tk()

# Define the title of the window.
FrmNameLength.title("Name Length")

# Set the window size
FrmNameLength.geometry("250x100")

# Add Label for name
lblName = tk.Label(FrmNameLength, text = "Your Name:")
lblName.place(x=10, y=25)

# Text box for Commission title
txtName = tk.Entry(FrmNameLength, bd=5, justify="center")
txtName.place(x=110, y=25)

# Function takes txtName and uses len function to output string characters
# Executed on click
def calculate_Click():
    intLenght = len(txtName.get()) # Get len() from assigned the name entered.
    messagebox.showinfo("Length of Name", f"{txtName.get()} is {intLenght} characters long.") # Popup message box to display output using f-string.
    txtName.delete(0, tk.END) # Delete characters in txt field when done.

# Calculate button to call calculate function
btnCalculate = tk.Button(FrmNameLength, text="CALCULATE", command=calculate_Click)
btnCalculate .place(x=85, y=70)

# Main loop of program
FrmNameLength.mainloop()

