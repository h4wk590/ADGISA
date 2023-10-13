'''
Author: Aidan Brown
GEOG 531 Fall 2023
Purpose: This program converts
farenheit to celcius, and outputs to form
using the tkinter module.
'''

# Import tkinter module
import tkinter as tk
from tkinter.messagebox import showinfo

# Create the main window
frmTempConverter = tk.Tk()

# Define the title of the window
frmTempConverter.title("Celcius to Fahrenheit Converter")

# Define the size of the window
frmTempConverter.geometry("350x320")

# Add empty list to add temp values to.
lstTemps = []

# Add lables for text boxes.
lblMinTemp = tk.Label(frmTempConverter, text="Minimum Temperature:")
lblMinTemp.place(x=20, y=20)
lblMaxTemp = tk.Label(frmTempConverter, text="Maximum Temperature:")
lblMaxTemp.place(x=20, y=50)
lblIncrement = tk.Label(frmTempConverter, text="Increment")
lblIncrement.place(x=20, y=80)

# Add Converting button
btnBuildTable = tk.Button(frmTempConverter, text="Build Conversion Table")
btnBuildTable.place(x=100, y=120)

# Add text boxes
txtMinTemp = tk.Entry(frmTempConverter, bd=5, justify="center")
txtMinTemp.place(x=200,y=20)
txtMaxTemp = tk.Entry(frmTempConverter, bd=5, justify="center")
txtMaxTemp.place(x=200,y=50)
txtIncrement = tk.Entry(frmTempConverter, bd=5, justify="center")
txtIncrement.place(x=200, y=80)

# Text box for converted temperature outputs
lboTempOutput = tk.Listbox(frmTempConverter, height=3, width=50, listvariable=lstTemps)

# loop through through main window.
frmTempConverter.mainloop()