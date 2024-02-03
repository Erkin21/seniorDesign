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
filepath = ""

# Run the loop for the specified duration
while time.time() - start_time < run_duration:
    # Read the sensor data
    accelerometer, gyroscope = read_sensor_data()

    # Print the sensor data
    print("Accelerometer data:", accelerometer)
    print("Gyroscope data:", gyroscope)

    # Wait for 1 second
    time.sleep(1)

    if not os.path.exists(filepath):                                                       # Check if the filepath exist if not create it in here
        workbook = openpyxl.Workbook()                                                     # Open workbook like an Excel sheet
        sheet = workbook["Sheet 2"]                                                        # workbook.active or The active here is the sheet that is seen at the bottom of excel "sheet 1, sheet 2..."
        heading = ["Accelerometer, Gyroscope"]
        sheet.append(heading)                                                              # Write the heading into the excel sheet
        workbook.save(filepath)                                                            # Save it

    # This few lines are for when you after you created the work book and want to save data
    workbook = openpyxl.load_workbook(filepath)
    if not 'Sheet 2' in workbook.sheetnames:
        workbook.create_sheet(title="Sheet 2")
    sheet = workbook["Sheet 2"]
    sheet.append([accelerometer,gyroscope])
    workbook.save(filepath)

print("===================================")
