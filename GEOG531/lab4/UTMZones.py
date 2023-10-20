'''
Author: Aidan Brown
GOEG 531 Fall 2023
This program shows the longitude range for a given UTM zone.
'''

# Import modules
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk

# Create the form
frmUTMZones = tk.Tk()

# Create form title
frmUTMZones.title("About UTM Zones")

# Define the size of the window
frmUTMZones.geometry("350x350")

# Function to calculate the longitude range based on the UTM zone
def calculateLongitude():
    intUTMZone = intZone.get()
    if 1 <= intUTMZone <= 30:
        longitude = (intUTMZone * 6) - 180
    elif 31 <= intUTMZone <= 60:
        longitude = 180 - (intUTMZone * 6)
    else:
        showinfo("Invalid UTM Zone", "Please select a valid UTM zone (1-60).")
        return

    showinfo("Longitude Range", f"Longitude Range: {longitude}° to {longitude + 6}°")

# Create an int control variable for the combobox property textvariable
intZone = tk.IntVar()
intZoneChoice = ttk.Combobox(frmUTMZones, width=15, textvariable=intZone)
intZoneChoice['values'] = list(range(1, 61))  # UTM zones 1 to 60
intZoneChoice.set(0)  # Default selection
intZoneChoice.pack(pady=10)

# Create a button to calculate the longitude range
calculate_button = tk.Button(frmUTMZones, text="Show Longitude Range", command=calculateLongitude)
calculate_button.pack()

# Create a button to show the "About UTM Zones" window
about_button = tk.Button(frmUTMZones, text="About UTM Zones") # Needs a command to show the about window still
about_button.pack()

# Create combobox
intZoneChoice = ttk.Combobox(frmUTMZones, width=15, textvariable=intZone)

# Initialize the form
frmUTMZones.mainloop()