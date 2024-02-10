import mpu6050
import time
import os
import openpyxl

# Create a new MPU6050 object
mpu = mpu6050.mpu6050(0x68)

# Define a function to read the sensor data
def read_sensor_data():
    # Read the accelerometer values
    accelerometer = mpu.get_accel_data()

    # Read the gyroscope values
    gyroscope = mpu.get_gyro_data()

    return accelerometer, gyroscope

# Get the current time
start_time = time.time()

# Set the duration for the program to run (in seconds)
run_duration = 30

# Filepath
filepath = "\data.xlsx"

# Check if the file exists, and create it if not
if not os.path.exists(filepath):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    heading = ["Accelerometer", "Gyroscope"]
    sheet.append(heading)
    workbook.save(filepath)

# Initialize workbook outside the loop
workbook = openpyxl.load_workbook(filepath)
sheet = workbook["Sheet 2"]

# Run the loop for the specified duration
while time.time() - start_time < run_duration:
    # Read the sensor data
    accelerometer, gyroscope = read_sensor_data()

    # Print the sensor data
    print("Accelerometer data:", accelerometer)
    print("Gyroscope data:", gyroscope)

    # Append data to the Excel sheet
    sheet.append([accelerometer["x"], accelerometer["y"], accelerometer["z"],
                  gyroscope["x"], gyroscope["y"], gyroscope["z"]])

    # Wait for 1 second
    time.sleep(1)

# Save workbook after the loop
workbook.save(filepath)

print("===================================")
