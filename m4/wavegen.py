# wavegen.py

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




import array
import audioio
import board
import math

samp_rate = 64000
default_freq = 25000
default_power = 50

class Wavegen:
    def __init__(self):
        self.out = audioio.AudioOut(board.A0)
        self.freq = default_freq
        self.power = default_power

    def update(self, freq, pwr):
        self.power = pwr
        self.freq = freq
        sample_buffer = array.array('h', [0] * int(samp_rate/self.freq))
        buff_length = len(sample_buffer)
        for i in range(buff_length):
            sample_buffer[i] = min(2 ** 15 - 1, int((self.power/100) * math.sin(2 * math.pi * i/buff_length)))

        self.out.stop()
        self.out.play(audioio.RawSample(sample_buffer, sample_rate=samp_rate), loop=True)
