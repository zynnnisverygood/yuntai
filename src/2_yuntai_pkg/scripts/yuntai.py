import serial
import struct
from time import sleep


def crc16(buffer):
    c, treat, bcrc, wcrc = 0, 0, 0, 0
    for c in buffer:
        for j in range(8):
            treat = c & 0x80
            c <<= 1
            bcrc = (wcrc >> 8) & 0x80
            wcrc <<= 1
            wcrc %= (0xffff + 1)
            if treat != bcrc:
                wcrc ^= 0x1021
    return wcrc % 256, int(wcrc / 256)


def int2uint(num):
    num=int(num)
    if num >= 0:
        return num
    return 256 + num


def setspeed(TTL, x=0, y=0):
    result = [0x55, 0x66, 1, 2, 0, 0, 0, 0x07]
    result += (int2uint(x), int2uint(y))
    result += (crc16(result))
    TTL.write(result)


def setpose(TTL, yaw=0, pitch=0):
    yaw *= 10
    pitch *= 10
    result = [0x55, 0x66, 1, 4, 0, 0, 0, 0x0e]
    result += (
    struct.pack('<h', yaw)[0], struct.pack('<h', yaw)[1], struct.pack('<h', pitch)[0], struct.pack('<h', pitch)[1])
    result += (crc16(result))
    TTL.write(result)
    sleep(0.04)
    TTL.read_all()


def setback(TTL):
    result = [0x55, 0x66, 0x01, 0x01, 0x00, 0x00, 0x00, 0x08, 0x01, 0xd1, 0x12]
    TTL.write(result)
    sleep(0.04)
    TTL.read_all()


def getpose(TTL):
    result = [0x55, 0x66, 0x01, 0x00, 0x00, 0x00, 0x00, 0x0d]
    result += (crc16(result))
    # resultbyt = bytes(result)
    TTL.write(result)
    sleep(0.04)
    respond_data = TTL.read_all()[8:-2]
    yaw, pitch, roll, yaw_velocity, pitch_velocity, roll_velocity = [
        (struct.unpack('<h', bytes([respond_data[i * 2], respond_data[i * 2 + 1]])))[0] / 10 for i in range(6)]
    return yaw, pitch, roll, yaw_velocity, pitch_velocity, roll_velocity 

# if __name__ == '__main__':
TTL = serial.Serial('/dev/ttyUSB0', 115200)
print(type(TTL))
    # setspeed(TTL, -50, -50)
    # setback(TTL)
    # setpose(TTL,7s0,25)
    # setback(TTL)
    # getpose(TTL)
    # result = [0x55, 0x66, 0x01, 0x01, 0x00, 0x00, 0x00, 0x08, 0x01, 0xd1, 0x12]
    # TTL.write(result)
    # print(TTL.readable())
    # TTL.close()
    # exit(0)
