# mpsfunc.py

# Copyright Ryan Akerley

# This file is part of MPS
# MPS is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# MPS is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with MPS. If not, see <https://www.gnu.org/licenses/>.



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
    try:
        ser.write(bytearray((pwr_start, pwr_end, pwr_step)))
        ser_read = [0] * 3
        ser_read = ser.read(3)
        print(ser_read)
    except NameError:
        pass

def set_serial_port(port='/dev/ttyACM0'):
    pass


