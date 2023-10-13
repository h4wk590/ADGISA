'''
Author: Aidan Brown
Date: Oct 9 2023
'''

# Import Tkinter module
import tkinter as tk

# Import messagebox
from tkinter import messagebox

# Create main window
frmTrainTickets  = tk.Tk()

# Define tile of window
frmTrainTickets.title("Train Tickets")

# Define size of window
frmTrainTickets.geometry("300x400")

# Empty var to hold cost for each radio button.
intCost = tk.IntVar()

# Empty var for discount checkbox
intDiscount = tk.IntVar()

# Create and place labels for radio buttons and text boxes
lblDestination = tk.Label(frmTrainTickets, text="Destination:")
lblDestination.place(x=15, y=15)
lblSeats = tk.Label(frmTrainTickets, text="Number of Seats:")
lblSeats.place(x=15, y=180)
lblCost = tk.Label(frmTrainTickets, text="Total Cost:")
lblCost.place(x=50, y=350)

# Create text boxes, justified center
txtSeats = tk.Entry(frmTrainTickets, bd=5, justify="center")
txtSeats.place(x=125, y=180)
txtCost = tk.Entry(frmTrainTickets, bd=5, justify="center")
txtCost.place(x=125, y=350)

# Create and place radio buttons for user to choose a destination.
optLadysmith = tk.Radiobutton(frmTrainTickets, text="Ladysmith ($15.00)", variable=intCost, value=1) # Unique value for intCost var
optLadysmith.place(x=50, y=40) 
optDuncan = tk.Radiobutton(frmTrainTickets, text="Duncan ($27.00)", variable=intCost, value=2) # Unique value for intCost var
optDuncan.place(x=50, y=80)
optVictoria = tk.Radiobutton(frmTrainTickets, text="Victoria ($39.00)", variable=intCost, value=3) # Unique value for intCost var
optVictoria.place(x=50, y=120)

# Function to clear the form and de-select all buttons
def ClearForm():
    optLadysmith.select() # Have to have this as select as we want Ladysmith as the starting option
    optDuncan.deselect() # De-select radio button
    optVictoria.deselect() 
    txtSeats.delete(0, tk.END) # Clean text box
    txtCost.delete(0, tk.END) 
    intDiscount.set(0) # Reset the senior discount checkbox

# Function to calculate the cost based on number of seats user chooses    
def CalculateCost():
    if not txtSeats.get().isdigit():
        messagebox.showerror("Error.", "Unaccepted. use number values only.") # Error message if user enters anything but int values
    else:
        intSeats = int(txtSeats.get()) # new int variable witihn loop to hold user entered number
        # Specified from radio button values using intCost variable, creating new float variables in loop
        if intCost.get() == 1: 
            fltCost = 15.00
        elif intCost.get() == 2: 
            fltCost = 27.00
        elif intCost.get() == 3: 
            fltCost = 39.00
        else:
            return # For any other criteria that doesn't match above stop program.
        totalCost = intSeats * fltCost
        # Apply discount within the loop
        if intDiscount.get() == 1: # if checkbox is checked [1=true]
            totalCost = totalCost * 0.85 # Apply discount - expressed as 85/100 for the 15% off the totalCost.
            messagebox.showinfo("Confirmation", "Discount Enabled.") 
        txtCost.delete(0, tk.END) # Remove any numbers in the Total Cost text box. This is just cleaner so it doesn't keep adding more values incase of multiple clicks..
        txtCost.insert(0, totalCost) # Insert total cost into the text box

# Create buttons for calculating cost and clearing the form
btnCalculate = tk.Button(frmTrainTickets, text="Calculate Cost", command=CalculateCost)
btnCalculate.place(x=50, y=295)
btnClear = tk.Button(frmTrainTickets, text="Clear Form", command=ClearForm)
btnClear.place(x=190, y=295)

# Create variable to hold senior discount value
intDiscount = tk.IntVar()
# Create and place checkbox for senior discount
ckbDiscount = tk.Checkbutton(frmTrainTickets, text="Seniors Discount (%15)", variable=intDiscount)
ckbDiscount.place(x=75, y=250)

# Focus on the opLadysmith button
optLadysmith.select()
# Main loop to run program
frmTrainTickets.mainloop()