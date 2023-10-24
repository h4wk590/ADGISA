'''
Author: Aidan Brown
GOEG 531 Fall 2023
This program shows the intlongitude range for a given UTM zone.
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

# Function to calculate the intlongitude range based on the UTM zone
def calculateLongitude():
    intUTMZone = intZone.get()
    if 1 <= intUTMZone <= 30:
        intlongitude = (intUTMZone * 6) - 180
    elif 31 <= intUTMZone <= 60:
        intlongitude = 180 - (intUTMZone * 6)
    else:
        showinfo("Invalid UTM Zone", "Please select a valid UTM zone (1-60).")
        return

    showinfo("Longitude Range", f"Longitude Range: {intlongitude}° to {intlongitude + 6}°")

# Function to show the About UTM Zones window
def AboutZones():
    wdwAbout = tk.Toplevel()
    wdwAbout.title("About UTM Zones")
    wdwAbout.geometry("300x200")
    
    lblAbout = tk.Label(wdwAbout, text="Universal Transverse Mercator (UTM) zones are a system of geospatial latitude-intlongitude grids.")
    lblAbout.pack(pady=20)
    
    close_button = tk.Button(wdwAbout, text="Close", command=wdwAbout.destroy)
    close_button.pack()

# Create an int control variable for the combobox property textvariable
intZone = tk.IntVar()
intZoneChoice = ttk.Combobox(frmUTMZones, width=15, textvariable=intZone)
intZoneChoice['values'] = list(range(1, 61))  # UTM zones 1 to 60
intZoneChoice.set(0)  # Default selection
intZoneChoice.pack(pady=10)

# Create a button to calculate the intlongitude range
btnCalculateRange = tk.Button(frmUTMZones, text="Show Longitude Range", command=calculateLongitude)
btnCalculateRange.pack()

# Create a button to show the "About UTM Zones" window
btnAbout = tk.Button(frmUTMZones, text="About UTM Zones", command=AboutZones) # Needs a command to show the about window still
btnAbout.pack()

# Create combobox
intZoneChoice = ttk.Combobox(frmUTMZones, width=15, textvariable=intZone)

# Initialize the form
frmUTMZones.mainloop()