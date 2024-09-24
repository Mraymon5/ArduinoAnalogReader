This repository contains code to allow an Arduino to be used to read in an analog signal, and report it to a python code to be saved.

This program requires python, and the modules `time`, `os`, and `pySerial`.

Your machine may not allow users to access the COM ports, and thus the arduino, without admin access. This is problematic for two reasons: it can interfere with flashing the arduino with the program initially, and also with accessing the serial port in python to allow recording from the arduino.

To grant access to the COM ports, run:
`sudo usermod -aG dialout $USER`


To use this code, flash an Arduino with the `.ino` program.
