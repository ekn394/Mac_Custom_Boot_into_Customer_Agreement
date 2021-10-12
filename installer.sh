#!/usr/bin/bash

clear;
ECHO "#############################";
ECHO "Installing PyGame Library";
pip3 install pygame --disable-pip-version-check;


ECHO "#############################";
ECHO "Making launcher.sh an executable file";
chmod +x launcher.sh;
ECHO "Finished making the launcher executable.";

ECHO "#############################";
ECHO "You will want to go to Terminal>Preferences";
ECHO "Select the 'Shell' tab";
ECHO "Select 'Close if the shell exited cleanly' from drop-down menu";


