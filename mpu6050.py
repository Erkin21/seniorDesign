from micropython import const
import ustruct

MPU6050_I2CADDR_DEFAULT = const(0x68)

MPU6050_REG_ACCEL_XOUT_H = const(0x3B)
MPU6050_REG_TEMP_OUT_H = const(0x41)
MPU6050_REG_GYRO_XOUT_H = const(0x43)


class MPU6050:
    def __init__(self, i2c, address=MPU6050_I2CADDR_DEFAULT):
        self.i2c = i2c
        self.address = address
        self.buf = bytearray(6)

    def _read_bytes(self, register, buf):
        self.i2c.readfrom_mem_into(self.address, register, buf)

    def _read_word(self, register):
        self._read_bytes(register, self.buf)
        return ustruct.unpack(">h", self.buf)[0]

    @property
    def temperature(self):
        raw_temp = self._read_word(MPU6050_REG_TEMP_OUT_H)
        return raw_temp / 340.0 + 36.53

    @property
    def accel(self):
        raw_accel_x = self._read_word(MPU6050_REG_ACCEL_XOUT_H)
        return raw_accel_x / 16384.0

    @property
    def gyro(self):
        raw_gyro_x = self._read_word(MPU6050_REG_GYRO_XOUT_H)
        return raw_gyro_x / 131.0
