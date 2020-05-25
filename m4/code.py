# code.py

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




from wavegen import Wavegen
import supervisor
import time

def run():
    wave = Wavegen()
    freq = 440
    pwr_start = 50
    pwr_end = 50
    pwr_step = 10
    print("running")

    while True:
        if supervisor.runtime.serial_bytes_available:
            val = input()
            pwr_start = val[0]
            pwr_end = val[1]
            pwr_step = val[2]
            print(val[0], val[1], val[2])

        power = pwr_start
        while power <= pwr_end:
            wave.update(freq, power)
            power = power + pwr_step
            time.sleep(0.2)

run()
