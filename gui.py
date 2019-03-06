from tkinter import *
from decimal import *


root = Tk()
frame=Frame(root)
frame.grid()



# define the functions for calculation
def add():
    result = Decimal(a.get()) + Decimal(b.get())
    c.delete(0, END)
    c.insert(0,str(result))


def sub():
    result = Decimal(a.get()) - Decimal(b.get())
    c.delete(0, END)
    c.insert(0, str(result))


def div():
    result = Decimal(a.get()) / Decimal(b.get())
    c.delete(0, END)
    c.insert(0, str(result))


def mul():
    result = Decimal(a.get()) * Decimal(b.get())
    c.delete(0, END)
    c.insert(0, str(result))


label1 = Label(root, text="Number1")
label2 = Label(root, text="Number2")
label3 = Label(root, text="Result")

a  = Entry(root)
b = Entry(root)
c = Entry(root)

bottomgrid=Frame(root)
bottomgrid.grid(row=2,column=1)

button1 = Button(bottomgrid,text= "add", fg = "red", command = add)
button2 = Button(bottomgrid,text = "sub",fg="blue", command = sub)
button3 = Button(bottomgrid,text= "div", fg = "green", command = div)
button4 = Button(bottomgrid,text= "mul", fg = "purple", command = mul)


label1.grid(row=0)
label2.grid(row=1)
label3.grid(row=3)

a.grid(row=0,column=1)
b.grid(row=1,column=1)
c.grid(row=3,column=1)

button1.grid(row=2)
button2.grid(row=2,column=1)
button3.grid(row=2,column=2)
button4.grid(row=2,column=3)

def new():
    a.delete(0,END)
    b.delete(0,END)
    c.delete(0,END)

menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label = 'file',menu=filemenu)
filemenu.add_command(label='New',command=new)
filemenu.add_command(label='open')
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)
helpmenu=Menu(menu)
menu.add_cascade(label='help',menu=helpmenu)
helpmenu.add_command(label='about')


root.mainloop()
