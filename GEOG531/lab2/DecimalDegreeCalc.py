'''
Author: Aidan Brown
Date: Oct 06 2023
ADGISAGEOG 531 
'''

# Import Tkinter module
import tkinter as tk

# Import messagebox
from tkinter import messagebox

# Create main window
frmDDCalculator  = tk.Tk()

# Define tile of window
frmDDCalculator.title("Decimal Degree Calculator")

# Define size of window
frmDDCalculator.geometry("500x300")

# Creating labels for text boxes
lblDegrees = tk.Label(frmDDCalculator, text="Degrees")
lblDegrees.place(x=10, y=15)
lblMinutes = tk.Label(frmDDCalculator, text="Minutes")
lblMinutes.place(x=180, y=15)
lblSeconds = tk.Label(frmDDCalculator, text="Seconds")
lblSeconds.place(x=350, y=15)
lblDecimalDegrees = tk.Label(frmDDCalculator, text="Decimal Degrees")
lblDecimalDegrees.place(x=150, y=200)

# Create and place Text boxes for converting, clearing, and decimal degrees
txtDegrees = tk.Entry(frmDDCalculator, bd=5, justify="center")
txtDegrees.place(x=10, y=40) 
txtMinutes = tk.Entry(frmDDCalculator, bd=5, justify="center")
txtMinutes.place(x=180, y=40)
txtSeconds = tk.Entry(frmDDCalculator, bd=5, justify="center")
txtSeconds.place(x=350, y=40)
txtDD = tk.Entry(frmDDCalculator, bd=5, justify="center")
txtDD.place(x=150, y=250)

# Function to clear the text boxes, and set focus back to Degrees text box
def clearText():
    txtDegrees.delete(0, tk.END)
    txtMinutes.delete(0, tk.END)
    txtSeconds.delete(0, tk.END)
    txtDD.delete(0, tk.END)
    txtDegrees.focus()

# Function to convert DMS to DD
# presents error message when not using int values in text boxes
# uses float values to add all text boxes together with formula to convert from DMS to DD
def convert():
    if not txtDegrees.get().isdigit():
        messagebox.showerror("Error", "Please use interger values to input data, not strings.")
    elif not txtMinutes.get().isdigit():
        messagebox.showerror("Error", "Please use interger values to input data, not strings.")
    elif not txtSeconds.get().isdigit():
        messagebox.showerror("Error", "Please use interger values to input data, not strings.")
    else:
        fltDD = float(txtDegrees.get()) + float(txtMinutes.get()) / 60 + float(txtSeconds.get()) / 3600
        txtDD.insert(0, fltDD)
        
# Button to clear call clearText function to clear all text boxes
btnClear = tk.Button(frmDDCalculator, text="Clear", command=clearText)
btnClear.place(x=300, y=120)

# Button to call convert function
btnConvert = tk.Button(frmDDCalculator, text="Convert", command=convert)
btnConvert.place(x=100, y=120)

# Main loop to run program
frmDDCalculator.mainloop()