import machine
import utime
from mpu6050 import MPU6050

# Initialize MPU6050
mpu = MPU6050()

# Set up UART for serial communication
uart = machine.UART(0, baudrate=115200, tx=0, rx=1) 

# Run the loop indefinitely
while True:
    # Read the sensor data
    accelerometer_data = mpu.acceleration
    gyroscope_data = mpu.gyroscope

    # Format the data as a CSV string
    data_string = f"{accelerometer_data[0]},{accelerometer_data[1]},{accelerometer_data[2]},"
    data_string += f"{gyroscope_data[0]},{gyroscope_data[1]},{gyroscope_data[2]}\n"

    # Send the data over serial
    uart.write(data_string)

    # Wait for a short duration (adjust as needed)
    utime.sleep_ms(1000)
