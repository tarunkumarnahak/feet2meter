# import tkinter
from tkinter import Tk, Button, Label, DoubleVar, Entry

# creating interface
window = Tk()
window.title("Feet to Meter Conversion App")
window.configure(background="light green")
window.geometry("320x220")
window.resizable(width=False, height=False)

# function


def convert():
    value = float(ft_entry.get())
    meter = value * 0.3048
    mt_value.set("%.4f" % meter)


def clear():
    ft_value.set("")
    mt_value.set("")


# adding labels
ft_lb1 = Label(window, text="Feet", bg='purple', fg='white', width=14)
ft_lb1.grid(column=0, row=0, padx=15, pady=15)

ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(column=1, row=0)
ft_entry.delete(0, 'end')  # delete to end

# adding label 2
mt_lb1 = Label(window, text='Meter', bg='brown', fg='white', width=14)
mt_lb1.grid(column=0, row=1)

mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=14)
mt_entry.grid(column=1, row=1, pady=30)
mt_entry.delete(0, 'end')
# convert button
convert_btn = Button(window, text='Convert', bg='blue',
                     fg='white', width=14, command=convert)
convert_btn.grid(column=0, row=3, padx=15)

clear_btn = Button(window, text='Clear', bg="black",
                   fg='white', width=14, command=clear)
clear_btn.grid(column=1, row=3, padx=15)
window.mainloop()
