import serial
import pandas as pd

# Configure serial communication with Raspberry Pi Pico
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # Adjust baud rate as needed

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

# Write the last line data to Excel file
df = pd.DataFrame([last_line_data], columns=['Column1', 'Column2', 'Column3'])  # Adjust column names as needed
with pd.ExcelWriter('data.xlsx', engine='openpyxl', mode='a') as writer:  # Append mode to add data to existing sheet
    df.to_excel(writer, sheet_name='Sheet1', index=False, header=False)

print("Data written to Excel file successfully.")
