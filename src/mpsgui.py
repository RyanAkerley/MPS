# mpsgui.py

# Ryan Akerley
# Umass Boston Senior Design
# ryan.akerley002@umb.edu

from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mbox
from tkinter import ttk
import mpsfunc as mf
from time import sleep

def run_button_pressed():
    mf.set_freq(freq_entry.get())
    mf.set_power(pwr_level.get())
    print(f"Running at {freq_entry.get()}kHz with {pwr_level.get()}% power for {run_time_var.get()} sec.")
    try:
        rt = int(run_time_var.get())
    except ValueError:
        mbox.showinfo(message='Time value must be a number')
    else:
        progress['value'] = 25
        sleep(rt/4)
        progress['value'] = 50 
        sleep(rt/4)
        progress['value'] = 75
        sleep(rt/4)
        progress['value'] = 100
        sleep(rt/4)

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
freq_plot = Canvas(data, width=400, height=400, relief='raised', borderwidth='2')
freq_plot.grid(column=0, columnspan=3, row=0, rowspan=3)
phase_plot = Canvas(data, width=400, height=400, relief='raised', borderwidth='2')
phase_plot.grid(column=3, columnspan=3, row=0, rowspan=3)

amps = IntVar()
amp_label = ttk.Label(data, text=(('current: '+str(amps.get())+' Amps')))
amp_label.grid(column = 0, row=3, sticky='e')
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

# power entry
pwr_level = StringVar(value='50')
pwr_lbl = ttk.Label(control, text='Drive Power', width=label_width)
pwr_lbl.grid(column=0, row=1, sticky='w', padx=5, pady=2)
pwr_entry = ttk.Entry(control, textvariable=pwr_level, width=widget_width, justify='right')
pwr_entry.grid(column=1, row=1, sticky='w', padx=5, pady=2)
pwr_incr = ttk.Label(control, text='%')
pwr_incr.grid(column=2, row=1, sticky='w', padx=5, pady=2)

# run time entry
run_time_var = StringVar(value='5')
runtime_lbl = ttk.Label(control, text='Run Time', width=label_width)
runtime_lbl.grid(column=0, row=2, sticky='w', padx=5, pady=2)
runtime_entry = ttk.Entry(control, textvariable=run_time_var, width=widget_width, justify='right')
runtime_entry.grid(column=1, row=2, sticky='w', padx=5, pady=2)
runtime_incr = ttk.Label(control, text='sec')
runtime_incr.grid(column=2, row=2, sticky='w', padx=5, pady=2)

# the run button
run_button = Button(control, command=run_button_pressed, text='Run', width=widget_width)
run_button.grid(column=3, row=1, padx=5, pady=2, sticky='ew')

progress = ttk.Progressbar(control, orient=HORIZONTAL, mode='determinate', length=400)
progress.grid(column=0, row=3, padx=5, pady=2, columnspan=4, sticky='ew')

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
