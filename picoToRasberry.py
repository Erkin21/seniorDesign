import serial
import openpyxl

# Define the serial port and file path
serial_port = "/dev/ttyACM0"
file_path = "dataMPU6050.txt"

# Initialize serial communication
ser = serial.Serial(serial_port)

# Read the last line from the text file on Raspberry Pi Pico
with open(file_path, "r") as file:
    last_line = file.readlines()[-1]

# Split the last line into a list of numbers
numbers = last_line.strip().split()

# Create a new Excel workbook
wb = openpyxl.Workbook()
sheet = wb.active

# Write the numbers to Excel cells
for i, num in enumerate(numbers, start=1):
    sheet.cell(row=1, column=i).value = float(num)  # Assuming the numbers are floats

# Save the Excel workbook
wb.save("output.xlsx")
