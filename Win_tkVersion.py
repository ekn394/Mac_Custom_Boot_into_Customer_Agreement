# KPL - DIY Computer Use Agreement for Branch Macs
# This step is usually handled by Netloan or MyPC. 
# However, branch Macs don't use either of those programs.  
# Evan Nordquist
# October 2021
# Requires Python 3 at this stage. 


# Import modules 

import sys
from tkinter import *
from tkinter import font as tkFont
from tkinter import messagebox

# Creating tk object
window = Tk(className="This is a test")

# Window attribute
window.attributes('-fullscreen', True)
window.title("KPL_Mac_User_Agreement")
window.config(bg="#FF00FF")

# Load the image
bg = PhotoImage(file = "backsplash2.png")

# Create Canvas

canvas1 = Canvas(window)
#canvas1.attributes('-fullscreen', True)

canvas1.pack(fill =BOTH, expand = True)

# Display image

canvas1.create_image( 0, 0, image = bg, anchor ="nw")

# Functions triggered by the buttons

def showAgreeMessage():
    #messagebox.showinfo('Message', 'Enjoy')
    sys.exit()

def showDeclineMessage():
    messagebox.showinfo('Alert', 'Whoops, you pressed the "DISAGREE" button.  You are going to need to click the "AGREE" button to use this computer.  Please try again.')

# Create fonts 

default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=20)
helv24 = tkFont.Font(family='Helvetica', size=24, weight='bold')

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
button = Button(canvas1, text=" I Agree", font=helv24, command = showAgreeMessage, width= 40, height=3, bg='#0052cc', fg="#ffffff", activebackground='#0052cc', activeforeground='#aaffaa')
button2 = Button(canvas1, text="I Disagree", font=helv24, command = showDeclineMessage, width= 40, height=3, bg='#0052cc', fg="#ffffff", activebackground='#0052cc', activeforeground='#aaffaa')
button.pack(side=LEFT, expand=True )
button2.pack(side=LEFT, expand=True )

# run 

window.mainloop()


