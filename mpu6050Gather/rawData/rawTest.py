from imu import MPU6050
from time import sleep, time
from machine import Pin, I2C

def collect_data():
    imu = MPU6050(I2C(0, sda=Pin(0), scl=Pin(1), freq=400000))
    start_time = time()
    run_duration = 15
    data = []
    timestamp = 0

    while timestamp <= run_duration:
        ax, ay, az, gx, gy, gz = imu.accel.x, imu.accel.y, imu.accel.z, imu.gyro.x, imu.gyro.y, imu.gyro.z
        mag = imu.gyro.magnitude
        data.append((timestamp, ax, ay, az, gx, gy, gz, mag))
        print(ax, ay, az, gx, gy, gz, mag)
        timestamp += 0.4
        sleep(0.4)

    return data

def save_to_file(data):
    file_name = "raw/rawData.txt"
    with open(file_name, "w") as file:
        file.write("Timestamp\tAx\tAy\tAz\tGx\tGy\tGz\tMagnitude\n")
        for entry in data:
            timestamp, ax, ay, az, gx, gy, gz, mag = entry
            file.write(f"{round(timestamp, 2)}\t{ax}\t{ay}\t{az}\t{gx}\t{gy}\t{gz}\t{mag}\n")

if __name__ == "__main__":
    collected_data = collect_data()
    save_to_file(collected_data)

    print("Data saved to rawData.txt")


