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

# Empty list to be used to append temp values to.
lstTemps = [] 

# Standalone function for the conversion that takes a intCelsius value
def celsiusToF(intCelsius):
    return (intCelsius * 9/5) + 32 # Returns the converted value to farenheit

# Function to add adjective based on the input (intCelsius from the celsiusToF function.)
def addAdjective(intCelsius):
    if intCelsius < 0: 
        return "cold" # If Celcius input is less than 0, return the word "cold"
    elif 0 <= intCelsius <= 15:
        return "cool" # Else if it's greater than or equal to 0, and less than or equal to 15, return "cool"
    elif 16 <= intCelsius <= 25:
        return "warm" # Else if it's greater than or equal to 16 and less than or equal to 25 return "warm"
    else: 
        return "hot" # Else return "hot" if all of the above conditions have not been met
    
# Function to build table 
def buildTable():
    # The textbox user inputs need to be float types
    fltMinTemp = float(txtMinTemp.get())
    fltMaxtemp = float(txtMaxTemp.get())
    fltIncrement = float(txtIncrement.get())

    # Clear the listbox before adding new values
    lboTempOutput.delete(0, tk.END)

    # For each intCelsius value in the range of values the user inputs..
    for intCelsius in range(int(fltMinTemp), int(fltMaxtemp) + 1, int(fltIncrement)):
        intfahrenheit = celsiusToF(intCelsius) # Takes intCelsius value from CelsiusToF function
        strAdjective = addAdjective(intCelsius) # Takes the intCelsius value and passses it into strAdjective variable
        lstTemps.append(f"{intCelsius}°C ({strAdjective}) = {intfahrenheit:.2f}°F") # Append the values to the empty list
        # Update the listbox, formatting with f-string and outputting as decimal, calls the strAdjective from the loop which has the adjective outputting to the conversion table
        lboTempOutput.insert(tk.END, f"{intCelsius}°C is a {strAdjective} {intfahrenheit:.2f}°F")

    # Clear text boxes
    txtMinTemp.delete(0, tk.END)
    txtMaxTemp.delete(0, tk.END)
    txtIncrement.delete(0, tk.END)    

# Add lables for text boxes.
lblMinTemp = tk.Label(frmTempConverter, text="Minimum Temperature:")
lblMinTemp.place(x=20, y=20)
lblMaxTemp = tk.Label(frmTempConverter, text="Maximum Temperature:")
lblMaxTemp.place(x=20, y=50)
lblIncrement = tk.Label(frmTempConverter, text="Increment")
lblIncrement.place(x=20, y=80)

# Add Converting button
btnBuildTable = tk.Button(frmTempConverter, text="Build Conversion Table", command=buildTable)
btnBuildTable.place(x=100, y=130)

# Add text boxes
txtMinTemp = tk.Entry(frmTempConverter, bd=5, justify="center")
txtMinTemp.place(x=200,y=20)
txtMaxTemp = tk.Entry(frmTempConverter, bd=5, justify="center")
txtMaxTemp.place(x=200,y=50)
txtIncrement = tk.Entry(frmTempConverter, bd=5, justify="center")
txtIncrement.place(x=200, y=80)

# Text box for converted temperature outputs
lboTempOutput = tk.Listbox(frmTempConverter, height=8, width=50)
lboTempOutput.place(x=20, y=160)

# loop through through main window.
frmTempConverter.mainloop()