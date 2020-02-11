# mpsgui.py

# Ryan Akerley
# Umass Boston Senior Design
# ryan.akerley002@umb.edu

import tkinter as tk
from tkinter.ttk import *
import mpsfunc


main_window = tk.Tk()
main_window.title('MPS')

data = tk.Frame(main_window)
data.pack(side = tk.TOP)

drive_freq = tk.StringVar() 
control = Frame(main_window)

frequency = Frame(control, width=512, height=256, padding=5)
freq_label = Label(frequency, text='Drive Frequency')
freq_label.pack(side=tk.LEFT)
freq_entry = Entry(frequency, textvariable=drive_freq)
freq_entry.pack(side=tk.RIGHT)
frequency.pack()

run_button = Button(control, command=lambda:mpsfunc.set_freq(freq_entry.get()), text='Run')
run_button.pack(side=tk.RIGHT)
control.pack()












main_window.mainloop()
