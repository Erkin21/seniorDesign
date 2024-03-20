import serial

# Configure serial communication with Raspberry Pi Pico
ser = serial.Serial('', 115200)  

# Open the .txt file on Raspberry Pi Pico for reading
ser.write(b'dataMPU6050.txt r\n')  # Adjust filename as needed

# Initialize variable to store the last line
last_line = ''

# Read and transfer the file contents line by line
while True:
    line = ser.readline().decode('utf-8').strip()
    if not line:
        break
    last_line = line  # Store the current line

# Close the serial connection
ser.close()

# Extract the last line content separated by '\t'
last_line_data = last_line.split('\t')

# Print or use the last line data as needed
print(last_line_data)
