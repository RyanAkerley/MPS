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
    try:
        mf.set_freq(freq_entry.get())
        mf.set_power(st_pwr_level.get())
        pwr_start = int(st_pwr_level.get())
        pwr_end = int(end_pwr_level.get())
        pwr_step = int(pwr_step_level.get())
        print(f"Running at {freq_entry.get()}kHz from {st_pwr_level.get()}% power to {end_pwr_level.get()}% in \
                {pwr_step_level.get()}% increments.")
    except ValueError:
        print('Values must be numbers')
    else:
        for i in range(pwr_start, pwr_end, pwr_step):
            mf.set_power(i)            
            sleep(1)
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

freq_plot_label = ttk.Label(data, text='Frequency')
freq_plot_label.grid(column=1, row=0, sticky='ew', padx=5, pady=5)
freq_plot = Canvas(data, width=400, height=250, relief='raised', borderwidth='2')
freq_plot.grid(column=0, columnspan=3, row=1, rowspan=3)
freq_img = PhotoImage(file='freq.png')
freq_plot.create_image(20, 20, anchor=NW, image=freq_img)

phase_plot_label = ttk.Label(data, text='Phase')
phase_plot_label.grid(column=4, row=0, sticky='ew', padx=5, pady=5)
phase_plot = Canvas(data, width=400, height=250, relief='raised', borderwidth='2')
phase_plot.grid(column=3, columnspan=3, row=1, rowspan=3)
phase_img = PhotoImage(file='phase.png')
phase_plot.create_image(20, 20, anchor=NW, image=phase_img)

mag_plot_label = ttk.Label(data, text='Magnetization')
mag_plot_label.grid(column=1, row=4, sticky='ew', padx=5, pady=5)
mag_plot = Canvas(data, width=400, height=250, relief='raised', borderwidth='2')
mag_plot.grid(column=0, columnspan=3, row=5, rowspan=3)
mag_img = PhotoImage(file='magnetization.png')
mag_plot.create_image(20, 20, anchor=NW, image=mag_img)

field_plot_label = ttk.Label(data, text='Excitation Field')
field_plot_label.grid(column=4, row=4, sticky='ew', padx=5, pady=5)
field_plot = Canvas(data, width=400, height=250, relief='raised', borderwidth='2')
field_plot.grid(column=3, columnspan=3, row=5, rowspan=3)
field_img = PhotoImage(file='excitation_field.png')
field_plot.create_image(20, 20, anchor=NW, image=field_img)

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
