'''
Author: Aidan Brown
GOEG 531 Fall 2023
This program shows the intlongitude range for a given UTM zone.
'''

# Import modules
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import ttk
from PIL import Image, ImageTk # Import PIL for images, needed to install 'Pillow' via pip

# Create the form
frmUTMZones = tk.Tk()

# Create form title
frmUTMZones.title("About UTM Zones")

# Define the size of the window
frmUTMZones.geometry("350x200")

# Function to calculate the intlongitude range based on the UTM zone
def calculateLongitude():
    intUTMZone = intZone.get() # Get the users input from the combobox
    if 1 <= intUTMZone <= 30:
        intlongitude = (intUTMZone * 6) - 180
    elif 31 <= intUTMZone <= 60:
        intlongitude = 180 - (intUTMZone * 6)
    else:
        showinfo("Please select a valid UTM zone (1-60).")
        return
    showinfo("Longitude Range", f"Zone {cboZones.get()} Longitude Range: {intlongitude}° to {intlongitude + 6}°") # Display output of long and lat using f-string

# Function to show the About UTM Zones window
def AboutZones():
    infoAbout = tk.Toplevel() # Create the info box 
    infoAbout.title("UTM Zone List") # Add title
    infoAbout.geometry("400x300") # Set resolution of the info box
    
    lblAbout = tk.Label(infoAbout, text="Universal Transverse Mercator (UTM) is a grid system that uses zones to identify coordinates on the Earth.", wraplength=200)
    lblAbout.pack(pady=20) # Using .pack method to place the label

    # Display an imgFile
    imgFile = Image.open('C:/Users/aidan/Nextcloud/Documents/school/School/VIU/ADGISA/GEOG531/lab4/utmzones.png')  # Had to hard code the path in, you will have to change this path to the photo dir.
    photo = ImageTk.PhotoImage(imgFile) # Using PhotoImage method to read the file
    lblImage = tk.Label(infoAbout, image=photo) # Add read file to infoAbout info box
    lblImage.photo = photo
    lblImage.pack() # Pack the photo into the info box

    # Creating button to close the 'About UTM Zones'
    btnCloseAbout = tk.Button(infoAbout, text="Ok", command=infoAbout.destroy) # Remove from memory after close
    btnCloseAbout.pack() # Pack the button to the bottom of the info box

# Create label for zones
lblZones = tk.Label(frmUTMZones, text="Zone:")
lblZones.place(x=70, y=25) # Place at same y position as combo box

# Create an intZone variable to hold integer values
intZone = tk.IntVar()

cboZones = ttk.Combobox(frmUTMZones, width=15, textvariable=intZone) # Create the combo box usig intZone variable
cboZones['values'] = list(range(1, 61))  # UTM zones 1 to 60
cboZones.set(1)  # Default selection set to 1
cboZones.place(x=120, y=25)

# Create a button to calculate the intlongitude range
btnCalculateRange = tk.Button(frmUTMZones, text="Show Longitude Range", command=calculateLongitude)
btnCalculateRange.place(x=30, y=70)

# Create a button to show the "About UTM Zones" window
btnAbout = tk.Button(frmUTMZones, text="About UTM Zones", command=AboutZones) # Needs a command to show the about window still
btnAbout.place(x=180, y=70)

# Create combo box
cboZones = ttk.Combobox(frmUTMZones, width=15, textvariable=intZone)

# Initialize the form
frmUTMZones.mainloop()