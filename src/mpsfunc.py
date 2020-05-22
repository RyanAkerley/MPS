import serial
from serial.serialutil import SerialException

try:
    ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
except SerialException:
    print('No serial device detected')


def export_csv():
    print('The data has been exported as a CSV file')

def set_freq(drive_freq):
    print(f'The drive frequency has been set to {drive_freq}')

def set_power(pwr_start, pwr_end, pwr_step):
    ser.write(bytearray((pwr_start, pwr_end, pwr_step)))
    ser_read = [0] * 3
    ser_read = ser.read(3)
    print(ser_read)



