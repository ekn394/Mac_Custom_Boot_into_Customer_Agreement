# Library Mac computers - Boot to Custom User Agreement Page 

## Installing

Place the contents of this repository somewhere on the Mac in question. 

Navigate to that folder using the Terminal, and run 

<code>
bash installer.sh
</code><br><br>


This will install the necessary dependencies (at this time consists of the Pygame library).  The installer.sh also makes sure that the launcher.sh file has "executable" permissions.

## Making the program run at each login.

Go to System Preferences, then Users & Groups.

Select the user that customers will use, add the launcher.sh file to the "Login Items" tab using the + (plus) button at the bottom of that window.  

If you log out and back in (as that user) you should be prompted with the Mac User Agreement program.  

## To disable the message

Remove the launcher.sh from the login items for the user.  

## To modify the text 

Edit the Mac_MUA.py  file. 

