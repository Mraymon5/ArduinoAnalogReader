This repository contains code to allow an Arduino to be used to read in an analog signal, and report it to a python code to be saved.

This program requires python, and the modules `time`, `os`, and `pySerial`.

Your machine may not allow users to access the COM ports, and thus the arduino, without admin access. This is problematic for two reasons: it can interfere with flashing the arduino with the program initially, and also with accessing the serial port in python to allow recording from the arduino.

To grant access to the COM ports, run the following code from the bash terminal:

```sudo usermod -aG dialout $USER```


This accomplished, flash an Arduino with the `AnalogRecord.ino` program. The easiest way to do this is usually via the Arduino IDE, downloadable here: https://www.arduino.cc/en/software/OldSoftwareReleases.
I recommend version `1/8/13`; after that release, they made some changes to the program that make the serial monitor much less useful. Not critical here, but having a functional serial monitor can be helpful for debugging.

To set up the python program, several lines will have to be edited.

Line 5: `os.chdir('/home/ramartin/Documents/') #Change this to the desired output folder` establishes the path to the desired folder for saving the data. Data will be saved as a CSV.

Line 10: `ser = serial.Serial('/dev/ttyACM1', 9600) #Change this to the port that the Arduino is currently in` establishes the connection with the arduino. 

If you don't know the address of the arduino, you can use the IDE to identify it: `Tools -> Port` should list the ports that currently host an Arduino. Alternatively, on linux, you can open a terminal and run:

```ls /dev/tty*```

The arduino should be listed here, likely something like `/dev/ttyUSB0` or `/dev/ttyACM0`.

Once the arduino has been flashed and the python program and its dependencies downloaded, open a terminal and run:

```python /path/to/AnalogArduinoRead.py```
