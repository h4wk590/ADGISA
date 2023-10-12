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

# Empty var for radio buttons
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

# Create text boxes
txtSeats = tk.Entry(frmTrainTickets, bd=5, justify="center")
txtSeats.place(x=125, y=180)
txtCost = tk.Entry(frmTrainTickets, bd=5, justify="center")
txtCost.place(x=125, y=350)

# Function to clear the form and de-select all buttons
def ClearForm():
    optLadysmith.deselect(0, tk.END)
    optDuncan.deselect(0, tk.END)
    optVictoria.deselect(0, tk.END)

# Create buttons for calculating cost and clearing the form
# Need to add command when have function
btnCalculate = tk.Button(frmTrainTickets, text="Calculate Cost")
btnCalculate.place(x=50, y=295)
btnClear = tk.Button(frmTrainTickets, text="Clear Form", command=ClearForm)
btnClear.place(x=190, y=295)

# Create and place radio buttons for user to choose a destination.
optLadysmith = tk.Radiobutton(frmTrainTickets, text="Ladysmith ($15.00)", variable=intCost, value=1) # Unique value for intCost var
optLadysmith.place(x=50, y=40) 
optDuncan = tk.Radiobutton(frmTrainTickets, text="Duncan ($27.00)", variable=intCost, value=2) # Unique value for intCost var
optDuncan.place(x=50, y=80)
optVictoria = tk.Radiobutton(frmTrainTickets, text="Victoria ($39.00)", variable=intCost, value=3) # Unique value for intCost var
optVictoria.place(x=50, y=120)

# Create and place checkbox for senior discount
ckbDiscount = tk.Checkbutton(frmTrainTickets, text="Seniors Discount (%15)", variable=intDiscount)
ckbDiscount.place(x=75, y=250)




# Focus on the opLadysmith button
optLadysmith.select()
# Main loop to run program
frmTrainTickets.mainloop()