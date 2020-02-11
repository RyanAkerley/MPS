# mpsgui.py

# Ryan Akerley
# Umass Boston Senior Design
# ryan.akerley002@umb.edu

import tkinter as tk
from tkinter.ttk import *
import mpsfunc as mf

def run_button_pressed():
    mf.set_freq(freq_entry.get())
    mf.set_power(pwr_level.get())
    print(f"Running at {freq_entry.get()}Hz with {pwr_level.get()}% power for {run_time_var.get()} sec.")

main_window = tk.Tk()
main_window.title('MPS')

#*****************************************************
# The data display area
#******************************************************
data = tk.Frame(main_window)
freq_plot = tk.Canvas(data, width=400, height=400, relief='raised', borderwidth='2')
freq_plot.grid(column=0, row=0)
phase_plot = tk.Canvas(data, width=400, height=400, relief='raised', borderwidth='2')
phase_plot.grid(column=1, row=0)
data.pack(side = tk.TOP)

#*******************************************************
# Control Area
# ******************************************************

control = Frame(main_window)

drive_freq = tk.StringVar()
frequency = Frame(control, width=512, height=256, padding=5)
freq_label = Label(frequency, text='Drive Frequency')
freq_label.grid(column=0, row=0)
freq_entry = Entry(frequency, textvariable=drive_freq)
freq_entry.grid(column=1, row=0)
frequency.grid(column=0, row=0)

pwr_level = tk.StringVar()
power = Frame(control, width=512, height=256, padding=5)
pwr_lbl = Label(power, text='Drive Power')
pwr_lbl.grid(column=0, row=0)
pwr_entry = Entry(power, textvariable=pwr_level)
pwr_entry.grid(column=1, row=0)
power.grid(column=0, row=1)

run_time_var = tk.StringVar()
runtime = Frame(control, padding=5)
runtime_lbl = Label(runtime, text='Run Time')
runtime_lbl.grid(column=0, row=0)
runtime_entry = Entry(runtime, textvariable=run_time_var)
runtime_entry.grid(column=1, row=0)
runtime.grid(column=0, row=2)

run_button = Button(control, command=run_button_pressed, text='Run')
run_button.grid(column=1, row=1)
control.pack()












main_window.mainloop()
