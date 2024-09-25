import serial
import time
import os
import keyboard

# Change to the desired output folder
os.chdir('/home/ramartin/Documents/') 
os.getcwd()

# Setup the serial connection (adjust the port if necessary)
ser = serial.Serial('/dev/ttyACM1', 9600)  # Adjust to your port
time.sleep(2)  # Wait for the connection to establish

startTime = time.time()
current_note = ""

# Function to update note based on keypress
def add_note(event):
    global current_note
    current_note += event.name  # Append the pressed key to the current note

# Hook to capture keystrokes
keyboard.on_press(add_note)

with open('data.csv', 'w') as f:
    while True:
        # Read data from Arduino
        line = ser.readline()

        try:
            decoded_line = line.decode('utf-8').strip()
            # Write the decoded line, note, and timestamp to the file
            f.write(f"{decoded_line} | Note: {current_note} | Time: {time.time()-startTime}\n")
            print(f"Decoded: {decoded_line} | Note: {current_note}")
            current_note = ""  # Clear the note after writing
        except UnicodeDecodeError as e:
            print(f"Error decoding: {e}")
