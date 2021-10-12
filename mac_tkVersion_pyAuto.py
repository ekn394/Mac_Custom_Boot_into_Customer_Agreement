# KPL - DIY Computer Use Agreement for Branch Macs
# This step is usually handled by Netloan or MyPC. 
# However, branch Macs don't use either of those programs.  
# Evan Nordquist
# October 2021
# Requires Python 3 at this stage.
# Macs don't natively let you change the look of a button object, even in python.  Baffling.
# In order to customize the buttons we needed another library tkmacosx
# Which you can get with pip3 install tkmacosx


# Import modules

#!/Library/Frameworks/Python.framework/Versions/3.10/bin/python3

import sys

from tkinter import *
from tkinter import font as tkFont
from tkinter import messagebox
from tkmacosx import Button
import pyautogui as mouse
from time import sleep




# Creating tk object
window = Tk(className="Loading...")

# Window attribute
window.attributes('-fullscreen', True)
window.title("KPL_Mac_User_Agreement")
window.config(bg="#FF00FF", menu="")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

print("Screen Height", screen_height)
print("Screen Width", screen_width)


# Load the image
bg = PhotoImage(file = "./backsplash2.png")


# Create Canvas

canvas1 = Canvas(window)
#canvas1.attribute('-fullscreen', True)

canvas1.pack(fill =BOTH, expand = True)

# Display image

canvas1.create_image( 500,0, image = bg)

# Mouse setup

mouse.FAILSAFE = False #Prevents mouse in top corner from stopping the program

# Functions triggered by the buttons

def showAgreeMessage():
    global window
    #messagebox.showinfo('Message', 'Enjoy')
    #sys.exit()  #This is the exit for Windows Computer
    window.destroy()  # This is the exit for a Mac
    

def showDeclineMessage():
    messagebox.showinfo('Alert', 'Whoops, you pressed the "DISAGREE" button.  You are going to need to click the "AGREE" button to use this computer.  Please try again.')

# Create fonts 

default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=20)
helv24 = tkFont.Font(family='Helvetica', size=24)

# Create textbox

message ='''
    Computer Use Policy:

        No funny business
        Keep pirating to a minimum

    Thanks,
    The Nerds '''

text_box = Text(canvas1, height=10, width=50, font=default_font)
text_box.pack(expand=True)
text_box.insert('end', message)
text_box.config(state='disabled')

# create buttons
button = Button(canvas1, text=" I Agree", font=helv24, command = showAgreeMessage, bg='#0052cc', fg="#ffffff", height=100, borderless=1, width=500)
button2 = Button(canvas1, text="I Disagree", font=helv24, command = showDeclineMessage, height=100,borderless=1, width=500, bg='#0052cc', fg="#FFF")

button.pack(side=LEFT, expand=True )
button2.pack(side=LEFT, expand=True )

# Run 

#window.mainloop()

def pacManUniverseMouse():
    x,y = mouse.position()
    if y < 100:
        mouse.moveTo(x,screen_height - 50)


while True:
    window.mainloop()
    time.sleep(.1)
    pacManUniverseMouse()
    time.sleep(.1)