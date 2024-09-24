import serial
import time
import os

os.chdir('/home/ramartin/Documents/') #Change this to the desired output folder

os.getcwd()

# Setup the serial connection (adjust the port if necessary)
ser = serial.Serial('/dev/ttyACM1', 9600) #Change this to the port that the Arduino is currently in
time.sleep(2)  # Wait for the connection to establish
startTime = time.time()

with open('data.csv', 'w') as f:
    while True:
        # Read data as raw bytes instead of trying to decode it
        line = ser.readline()  # This will read bytes

        # Decode the bytes into a string
        try:
            decoded_line = line.decode('utf-8').strip()
            f.write(decoded_line + ' | Time: ' + str(startTime-time.time()) + '\n')  # Write to the file
            print("Decoded: " + decoded_line)
        except UnicodeDecodeError as e:
            print("Error decoding: " + e)
