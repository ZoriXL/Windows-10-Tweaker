from tkinter import *
import os
import shutil
from tkinter import ttk
from tkinter.ttk import Progressbar

# main setup
root = Tk()
root.title("Windows 10 Tweak")
root.geometry("299x250")

#text-warning
label = Label(text="Secret Apps")
label.place(y=0, x=115)

# default in-app
def scrsaver(): 
     os.system("control desk.cpl,,@screensaver")

btn = Button(text="Open\nscreen\nsaver", command=scrsaver, width=7, height=3)
btn.place(y=25, x=0) #Screen Saver

#default in-app
def slideoff(): 
     os.system("SlideToShutDown")

btn = Button(text="Slide To\nshutdown", command=slideoff, width=7, height=3)
btn.place(x=60, y=25) #Slide to shutdown

#default in-app
def oldwall(): 
     os.system("explorer.exe shell:::{ED834ED6-4B5A-4bfe-8F11-A626DCB6A921} -Microsoft.Personalization\pageWallpaper ")

btn = Button(text="Change\nwallpaper\nold menu", command=oldwall, width=7, height=3)
btn.place(x=120, y=25) #old change wallpaper

#default an-app
def oldcolor(): 
     os.system("explorer.exe shell:::{ED834ED6-4B5A-4bfe-8F11-A626DCB6A921} -Microsoft.Personalization\pageColorization ")

btn = Button(text="Change\ncolor old\n menu", command=oldcolor, width=7, height=3)
btn.place(x=180, y=25) #old change color

#default an-app
def oldtheme(): 
     os.system("explorer.exe shell:::{ED834ED6-4B5A-4bfe-8F11-A626DCB6A921}")

btn = Button(text="Change\ntheme old\n menu", command=oldtheme, width=7, height=3)
btn.place(x=240, y=25) #old change wallpaper

#entry.get() -- command to paste entry value
#app-install
def installcustom():
   pathvar = str("powershell add-appxpackage -path ") + str(entry.get())
   os.system(pathvar)

btn = Button(text="Install custom appx", command=installcustom, width=16, height=1)
btn.place(x=140, y=140)

entry = Entry()
entry.place(x=140, y=112)

#text-warning
label = Label(text="Appx manager")
label.place(x=105, y=85)

#app-install
def installms():
   os.system("powershell wsreset -i")

btn = Button(text="Install\nMS Store", command=installms, width=7, height=3)
btn.place(x=0, y=110)

#app-install
def installcam():
   os.system("powershell Add-AppxPackage -path C:/Users/ZoriXL/Documents/N-Staller/appx/cam.appx")

btn = Button(text="Install\ncamera", command=installcam, width=7, height=3)
btn.place(x=60, y=110)

root.mainloop()