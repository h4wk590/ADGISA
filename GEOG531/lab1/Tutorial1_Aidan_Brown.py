"""
Author: Aidan Brown
GEOG 531 - Fall 2023
Assignment 01, Tutorial 1
"""

# Import the GUI package
import tkinter as tk

# Create the GUI application main window
frmTextColours = tk.Tk()

# Define the title of the window.
frmTextColours.title("Text color demonstration")

# Define the size of the window
frmTextColours.geometry("200x200")

# Create and place the textbox for user entered text on the parent window
txtColouredText = tk.Entry(frmTextColours, bd=5, justify="center")
txtColouredText.pack(side="top", pady=10)

# Create and place the labels for Text Color and Background Color
lblTC = tk.Label(frmTextColours, text = "Text Color")
lblTC.place(x=10, y=50)
lblBC = tk.Label()
lblBC = tk.Label(frmTextColours, text = "Background Color")
lblBC.place(x=85, y=50)

# Function to change textbox foreground property
def btnBlueTxt_Click():
    txtColouredText.config(fg="Blue")

# Create and place the buttons to change text to blue
btnBlueTxt = tk.Button(frmTextColours, text="Blue Text", command=btnBlueTxt_Click)
btnBlueTxt.place(x=10, y=90)

# Function to change textbox foreground property.
def btnYellowBg_Click():
    txtColouredText.config(bg="Yellow")

# Create and place the buttons to change background to yellow
btnYellowBG = tk.Button(frmTextColours, text="Yellow Background", command=btnYellowBg_Click)
btnYellowBG.place(x=80, y=90)

def btnRedTxt_Click():
    txtColouredText.config(fg="Red")

# Create and place the buttons to change text to red
btnRedTxt = tk.Button(frmTextColours, text="Red Text", command=btnRedTxt_Click)
btnRedTxt.place(x=10, y=150)

def btnGreenBg_Click():
    txtColouredText.config(bg="Green")

# Create and place the buttons to change background to green
btnGreenBG = tk.Button(frmTextColours, text="Green Background", command=btnGreenBg_Click)
btnGreenBG.place(x=80, y=150)

# Infinite loop of main window
frmTextColours.mainloop()