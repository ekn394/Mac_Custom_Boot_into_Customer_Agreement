#!/usr/bin/bash

clear;
ECHO "Installing Mac Compatible TKinter library -tkmacosx";
pip3 install tkmacosx --disable-pip-version-check;

ECHO "#############################";
ECHO "Installing pyautogui Library - for mouse/keyboard inputs";
pip3 install pyautogui --disable-pip-version-check;


ECHO "#############################";
ECHO "Making launcher.sh an executable file";
chmod +x launcher.sh;
ECHO "Finished making the launcher executable.";

ECHO "#############################";
ECHO "You will want to go to Terminal>Preferences";
ECHO "Select the 'Shell' tab";
ECHO "Select 'Close if the shell exited cleanly' from drop-down menu";


