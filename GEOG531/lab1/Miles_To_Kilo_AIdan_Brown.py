"""
Author: Aidan Brown
GEOG 531 - Fall 2023
Assignment 1 - Question 8
"""

# Import tkinter module and messagebox
import tkinter as tk
from tkinter import messagebox

# Create main window using TK
FrmConvertKm = tk.Tk()

# Set the window size
FrmConvertKm.geometry("250x250")

# Define Title
FrmConvertKm.title("Calculate Commission")


# Add Label for Kilometers and Miles
lblKm = tk.Label(FrmConvertKm, text = "Kilometers:")
lblKm.place(x=10, y=100)
lblMiles = tk.Label(FrmConvertKm, text = "Miles:")
lblMiles.place(x=10, y=25)


# Enter number in miles
txtMiles = tk.Entry(FrmConvertKm, bd=5, justify="center")
txtMiles.place(x=110, y=25)

# Output for KM
txtKm = tk.Entry(FrmConvertKm, bd=5, justify="center")
txtKm.place(x=100, y=100)


# Define function to convert input (miles) to output (KM)
def calculate_Click():
    fltKm = float(txtMiles.get()) * 1.6
    txtKm.delete(0, tk.END)
    txtKm.insert(0, fltKm)


# Calculate button to call calculate_Click function
btnCalculate = tk.Button(FrmConvertKm, text="CALCULATE", command=calculate_Click)
btnCalculate .place(x=85, y=68)


# Focus on Kilometer textbox
txtMiles.focus()
# Main loop of program
FrmConvertKm.mainloop()