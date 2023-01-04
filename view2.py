from tkinter import *
import controller

def get_choise():
    return txt.get()

def view_message(mes):
    lb.configure(text=mes)

def get_loop():
    return window.mainloop

window = Tk()

lb = Label(window, text='')
txt = Entry(window, width=30)
btn = Button(window, text="Отправить", command=controller.controller_loop)

lb.grid(column=0, row=0)
txt.grid(column=0, row=1)
btn.grid(column=1, row=1)