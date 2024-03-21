# This file make sure only on Pico it will keep running in background so you can run mpuToExcel.py to store data
# the last line in 'dataMPU6050.txt' to the excel sheet where the machine learning will read it
import machine
import time

# Define the serial port pins (UART)
uart = machine.UART(0, baudrate=9600)

# Read the last line from the text file
with open('dataMPU6050.txt', 'r') as file:
    lines = file.readlines()
    last_line = lines[-1]

# Send the last line over the serial connection
while True:
    print(last_line)
    # Wait for the data to be sent
    time.sleep(1)  # Adjust delay as needed

# Close the serial connection (optional)
uart.deinit()
