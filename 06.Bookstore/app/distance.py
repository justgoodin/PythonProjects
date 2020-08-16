from tkinter import *

def miles_to_km():
    print(miles.get())
    result = float(miles.get())*1.6
    t1.insert(END,result)

window = Tk() #initialising the window

#Initialising widgets
b1 = Button(window, text="Calculate",command=miles_to_km)
b1.grid(row=0, column=0)

miles = StringVar()
e1 = Entry(window, textvariable=miles)
e1.grid(row=0, column=1)

t1 = Text(window,height=1,width=20)
t1.grid(row=0, column=2)

window.mainloop()