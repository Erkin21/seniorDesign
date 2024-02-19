from imu import MPU6050
from time import sleep, time
from machine import Pin, I2C

class StrideDetector:
    def __init__(self):
        self.imu = MPU6050(I2C(0, sda=Pin(0), scl=Pin(1), freq=400000))
        self.threshold = 40
        self.start_time = time()
        self.total_elapsed_time = 0  # New variable to track total elapsed time
        self.run_duration = 30
        self.file_name = "dataMPU6050.txt"
        self.file = open(self.file_name, "w")
        self.file.write("No of Strides\tWalking Time\tStride Length\tStride Frequency\tStride Speed\tStride Cadence\tStride Time\tStance Time\tSwing Time")
        self.file.write("\n")

        self.distance = 40		# This is 40 meters but maybe change later
        self.num_strides = 0
        self.walk_time = 0
        self.stride_length = 0
        self.stride_freq = 0
        self.stride_speed = 0
        self.stride_cadence = 0
        self.stride_time = 0
        self.stance_time = 0
        self.swing_time = 0
        
        # Variables
        self.strike = 0
        self.time_strike = 0

    def mpu_read(self):
        ax = round(self.imu.accel.x, 2)
        ay = round(self.imu.accel.y, 2)
        az = round(self.imu.accel.z, 2)
        gx = round(self.imu.gyro.x, 2)
        gy = round(self.imu.gyro.y, 2)
        gz = round(self.imu.gyro.z, 2)
        mag = round(self.imu.gyro.magnitude, 2)		# Magnitude of gyroscope
        return ax, ay, az, gx, gy, gz, mag

    def write_file_data(self):
        data = [
            str(self.num_strides),
            str(self.walk_time),
            str(self.stride_length),
            str(self.stride_freq),
            str(self.stride_speed),
            str(self.stride_cadence),
            str(self.stride_time),
            str(self.stance_time),
            str(self.swing_time)
        ]
        self.file.write("\t".join(data) + "\n")
        self.file.flush()

    def detect_stride(self, ax, ay, gz, mag):
        if gz >= 20 and self.walk_time >= 0.4:
            if gz >= 20 and self.strike <= 0:
                self.num_strides += 1
                self.strike = 1
                if self.time_strike == 0:
                    self.time_strike = self.walk_time
                else:
                    self.time_strike = self.walk_time - self.time_strike
        elif gz < 20:
            self.strike = 0

        # Calculate stride length (assuming walking speed is relatively constant)
        self.stride_length = self.distance / self.num_strides if self.num_strides > 0 else 0

        # Calculate stride frequency, time, speed, and cadence
        self.stride_freq = self.num_strides / self.time_strike if self.time_strike > 0 else 0
        self.stride_speed = self.stride_length * self.stride_freq
        self.stride_cadence = self.num_strides / self.time_strike * 60 if self.time_strike > 0 else 0

        # Need to fix these, Time strike is only when foot off the ground
        self.stride_time = self.time_strike / self.num_strides if self.num_strides > 0 else 0
        self.stance_time = self.stride_time * 0.56
        self.swing_time = self.stride_time * 0.44

        # Increment walk time and write data to the file
        self.walk_time += 0.4
        
        print(self.strike, self.time_strike)
        self.write_file_data()


    def run_detection(self):
        while self.walk_time <= self.run_duration:
            ax, ay, az, gx, gy, gz, mag = self.mpu_read()
            
            self.detect_stride(ax, ay, gz, mag)
            print(ax, ay, az, gx, gy, gz)
            sleep(0.4)

        self.file.close()

# Run the stride detection
stride_detector = StrideDetector()
stride_detector.run_detection()

