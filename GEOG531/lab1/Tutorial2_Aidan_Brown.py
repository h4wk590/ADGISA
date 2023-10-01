"""
Author: Aidan Brown
GEOG 531 - Fall 2023
Assignment 1, Tutorial 2
"""

# Import tkinter module
import tkinter as tk

# Create main window using tk
FrmCalcCommission = tk.Tk()

# Define title
FrmCalcCommission.title("Calculate Commission")

# Set the window size
FrmCalcCommission.geometry("250x100")

# Place labels within window.
lblSales = tk.Label(FrmCalcCommission, text = "SALES:")
lblSales.place(x=10, y=10)
lblCommission = tk.Label(FrmCalcCommission, text = "COMMISSION:")
lblCommission.place(x=10, y=35)

# Text box for Sales title
txtSales = tk.Entry(FrmCalcCommission, bd=5, justify="center")
txtSales.place(x=110, y=10)

# Text box for Commission title
txtCommission = tk.Entry(FrmCalcCommission, bd=5, justify="center")
txtCommission.place(x=110, y=35)

# Function to calculate on click
# Takes input as text number and multiplies the input
# by 0.15 to get 15% of the input number as commission
def calculate_Click():

    fltCommission = float(txtSales.get()) * 0.15
    txtCommission.delete(0, tk.END)
    txtCommission.insert(0, fltCommission)

# Calculate button to call calculate function
btnCalculate = tk.Button(FrmCalcCommission, text="CALCULATE", command=calculate_Click)
btnCalculate .place(x=85, y=68)

# Place tab focus on the sales button
txtSales.focus()

# Main loop of program
FrmCalcCommission.mainloop()