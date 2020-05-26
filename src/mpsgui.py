# mpsgui.py

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

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mbox
from tkinter import ttk
import mpsfunc as mf
from time import sleep

import matplotlib as mpl
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from matplotlib.backend_bases import key_press_handler

import numpy as np


def run_button_pressed():
    try:
        mf.set_freq(freq_entry.get())
        pwr_start = int(st_pwr_level.get())
        pwr_end = int(end_pwr_level.get())
        pwr_step = int(pwr_step_level.get())
        mf.set_power(pwr_start, pwr_end, pwr_step)
        print(f"Running at {freq_entry.get()}kHz from {st_pwr_level.get()}% power to {end_pwr_level.get()}% in \
                {pwr_step_level.get()}% increments.")
    except ValueError:
        print('Values must be numbers')
    else:
        mf.set_power(pwr_start, pwr_end, pwr_step)
        for i in range(pwr_start, pwr_end, pwr_step):
#            mf.set_power(i)            
#            sleep(1)
            progress['value'] = 100*i/(pwr_end - pwr_start) 

        print('Done')

def export_csv():
    filename = fd.asksaveasfilename()

def open_doc():
    pass


main_window = Tk()
main_window.title('MPS')
main_window.option_add('*tearOff', FALSE)

#*****************************************************
# The data display area
#******************************************************


data = ttk.Frame(main_window)

freqs = [25000, 75000, 125000, 175000, 225000, 275000]
amps = [1, .33, .2, .14, .11, .091]
phases = [0, -5, -7, -11, -14, -20]
excite_field = []
mag = []
smpl_time = range(0,40,1)
field = [0]*40

##############################################################################
# Display a plot of the amplitudes of the harmonics
##############################################################################
freq_plot_label = ttk.Label(data, text='Frequency')
freq_plot_label.grid(column=1, row=0, sticky='ew', padx=5, pady=5)
freq_plot = Canvas(data, width=400, height=250, relief='raised', borderwidth='2')
freq_plot_fig = Figure(figsize=(4, 2.5), dpi=100)
freq_plot_fig.add_subplot(111).plot(freqs, amps)
freq_plot_canvas = FigureCanvasTkAgg(freq_plot_fig, master=freq_plot)
freq_plot_canvas.draw()
freq_plot_canvas.get_tk_widget().grid(column=0, row=0)
freq_plot.grid(column=0, columnspan=3, row=1, rowspan=3)

##############################################################################
# Display a plot of the phase shifts of the harmonics
##############################################################################
phase_plot_label = ttk.Label(data, text='Phase')
phase_plot_label.grid(column=4, row=0, sticky='ew', padx=5, pady=5)
phase_plot_fig = Figure(figsize=(4, 2.5), dpi=100)
phase_plot_fig.add_subplot(111).plot(freqs, phases)
phase_plot = Canvas(data, width=400, height=250, relief='raised', borderwidth='2')
phase_plot_canvas = FigureCanvasTkAgg(phase_plot_fig, master=phase_plot)
phase_plot_canvas.draw()
phase_plot_canvas.get_tk_widget().grid(column=0, row=0)
phase_plot.grid(column=3, columnspan=3, row=1, rowspan=3)

##############################################################################
# Display a plot of the magnetization vs excitation field
##############################################################################
mag_plot_label = ttk.Label(data, text='Magnetization')
mag_plot_label.grid(column=1, row=4, sticky='ew', padx=5, pady=5)
mag_plot_fig = Figure(figsize=(4, 2.5), dpi=100)
mag_plot_fig.add_subplot(111).plot(excite_field, mag)
mag_plot = Canvas(data, width=400, height=250, relief='raised', borderwidth='2')
mag_plot_canvas = FigureCanvasTkAgg(mag_plot_fig, master=mag_plot)
mag_plot_canvas.draw()
mag_plot_canvas.get_tk_widget().grid(column=0, row=0)
mag_plot.grid(column=0, columnspan=3, row=5, rowspan=3)

##############################################################################
# Display a plot of magnetization over time
##############################################################################
field_plot_label = ttk.Label(data, text='Excitation Field')
field_plot_label.grid(column=4, row=4, sticky='ew', padx=5, pady=5)
field_plot_fig = Figure(figsize=(4, 2.5), dpi=100)
field_plot_fig.add_subplot(111).plot(smpl_time, field)
field_plot = Canvas(data, width=400, height=250, relief='raised', borderwidth='2')
field_plot_canvas = FigureCanvasTkAgg(field_plot_fig, master=field_plot)
field_plot_canvas.draw()
field_plot_canvas.get_tk_widget().grid(column=0, row=0)
field_plot.grid(column=3, columnspan=3, row=5, rowspan=3)

##############################################################################
# Display the current from the current sensor
##############################################################################
amps = IntVar()
amp_label = ttk.Label(data, text=(('current: '+str(amps.get())+' Amps')))
amp_label.grid(column = 0, row=8, padx=5, pady=5, sticky='e')
ex_field = IntVar()
field_label = ttk.Label(data, text=(('excitation field: '+str(ex_field.get())+' mT')))
field_label.grid(column = 3, row=8, padx=5, pady=5, sticky='e')
data.grid(column=0, row=0)


#*******************************************************
# Control Area
# ******************************************************

control = ttk.Frame(main_window, relief='groove', borderwidth=2)
widget_width = 32
label_width = 24

# The frequency entry
drive_freq = StringVar(value='25')
freq_label = ttk.Label(control, text='Drive Frequency', width=label_width)
freq_label.grid(column=0, row=0, sticky='w', padx=5, pady=2)
freq_entry = ttk.Entry(control, textvariable=drive_freq, width=widget_width, justify='right')
freq_entry.grid(column=1, row=0, sticky='w', padx=5, pady=2)
freq_incr = ttk.Label(control, text='kHz')
freq_incr.grid(column=2, row=0, sticky='w', padx=5, pady=2)

# start power entry
st_pwr_level = StringVar(value='10')
st_pwr_lbl = ttk.Label(control, text='Start Power', width=label_width)
st_pwr_lbl.grid(column=0, row=1, sticky='w', padx=5, pady=2)
st_pwr_entry = ttk.Entry(control, textvariable=st_pwr_level, width=widget_width, justify='right')
st_pwr_entry.grid(column=1, row=1, sticky='w', padx=5, pady=2)
st_pwr_incr = ttk.Label(control, text='%')
st_pwr_incr.grid(column=2, row=1, sticky='w', padx=5, pady=2)

# end power entry
end_pwr_level = StringVar(value='100')
end_pwr_lbl = ttk.Label(control, text='End Power', width=label_width)
end_pwr_lbl.grid(column=0, row=2, sticky='w', padx=5, pady=2)
end_pwr_entry = ttk.Entry(control, textvariable=end_pwr_level, width=widget_width, justify='right')
end_pwr_entry.grid(column=1, row=2, sticky='w', padx=5, pady=2)
end_pwr_incr = ttk.Label(control, text='%')
end_pwr_incr.grid(column=2, row=2, sticky='w', padx=5, pady=2)

# power step entry
pwr_step_level = StringVar(value='10')
pwr_step_lbl = ttk.Label(control, text='Power Step', width=label_width)
pwr_step_lbl.grid(column=0, row=3, sticky='w', padx=5, pady=2)
pwr_step_entry = ttk.Entry(control, textvariable=pwr_step_level, width=widget_width, justify='right')
pwr_step_entry.grid(column=1, row=3, sticky='w', padx=5, pady=2)
pwr_step_incr = ttk.Label(control, text='%')
pwr_step_incr.grid(column=2, row=3, sticky='w', padx=5, pady=2)


# the run button
run_button = Button(control, command=run_button_pressed, text='Run', width=widget_width)
run_button.grid(column=3, row=1, padx=5, pady=2, sticky='ew')

progress = ttk.Progressbar(control, orient=HORIZONTAL, mode='determinate', length=400)
progress.grid(column=0, row=4, padx=5, pady=2, columnspan=4, sticky='ew')

control.grid(column=0, row=1, sticky='nsew')

#*******************************************************************************************
# The menubar
#*******************************************************************************************

menubar = Menu(main_window)
main_window['menu'] = menubar

# The File Menu
file_menu = Menu(menubar)
menubar.add_cascade(menu=file_menu, label='File')
file_menu.add_command(label='Export as CSV', command=export_csv)
file_menu.add_command(label='Quit', command=main_window.destroy)

# The help menu
help_menu = Menu(menubar, name='help')
menubar.add_cascade(menu=help_menu, label='Help')
help_menu.add_command(label='Documentation', command=open_doc)

# Context menu
context_menu = Menu(main_window)
context_menu.add_command(label = 'Export to CSV', command=export_csv)
if(main_window.tk.call('tk', 'windowingsystem')=='aqua'):
    main_window.bind('<2>', lambda e: context_menu.post(e.x_root, e.y_root))
    main_window.bind('<Control-1>', lambda e: context_menu.post(e.x_root, e.y_root))
else:
    main_window.bind('<3>', lambda e: context_menu.post(e.x_root, e.y_root))



main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=0)






main_window.mainloop()
