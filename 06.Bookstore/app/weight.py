from tkinter import *

def convert():
    gm = float(kgs.get())*1000.0
    t1.insert(END,gm)
    lb = float(kgs.get())*2.20462
    t2.insert(END,lb)
    oz = float(kgs.get())*35.274
    t3.insert(END,oz)

window = Tk() #initialising the window

#Initialising widgets
l1 = Label(window, text="Enter kg")
l1.grid(row=0, column=0)

kgs = StringVar()
e1 = Entry(window,textvariable=kgs)
e1.grid(row=0, column=1)

b1 = Button(window, text="Convert",command=convert)
b1.grid(row=0, column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)

t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)

window.mainloop()