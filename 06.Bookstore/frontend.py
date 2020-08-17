"""
A program that stores this book information 
Title, Author
Year, ISBN, 

User can:
View all records
Search an entry
Add entry
Update entry
Delete
Close
"""

from tkinter import *
import backend


#Function to get ListBox row selection
def get_selected_row(event):
    global selected_row
    index = listBox.curselection()[0]
    selected_row = listBox.get(index)
    ent_Title.delete(0,END)
    ent_Title.insert(END,selected_row[1])
    ent_Author.delete(0,END)
    ent_Author.insert(END,selected_row[2])
    ent_Year.delete(0,END)
    ent_Year.insert(END,selected_row[3])
    ent_ISBN.delete(0,END)
    ent_ISBN.insert(END,selected_row[4])


#Functions to pull data from backend
def command_view_all():
    listBox.delete(0,END)
    for row in backend.view_all():
        listBox.insert(END, row)

def command_search_entry():
    listBox.delete(0,END)
    for row in backend.search_entry(text_Title.get(),text_Author.get(),text_Year.get(),text_ISBN.get()):
        listBox.insert(END, row)

def command_add_entry():
    listBox.delete(0,END)
    backend.add_entry(text_Title.get(),text_Author.get(),text_Year.get(),text_ISBN.get())
    command_view_all()

def command_delete():
    backend.delete(selected_row[0])
    command_view_all()

def command_update():
    backend.update(selected_row[0],text_Title.get(),text_Author.get(),text_Year.get(),text_ISBN.get())
    command_view_all()

def command_close():
    window.destroy()

window = Tk()
window.wm_title("Bookstore")

#Declare & position Label components
lbl_Title = Label(window,text="Title")
lbl_Title.grid(row=0, column=0)
lbl_Year = Label(window,text="Year")
lbl_Year.grid(row=1, column=0)
lbl_Author = Label(window,text="Author")
lbl_Author.grid(row=0, column=2)
lbl_ISBN = Label(window,text="ISBN")
lbl_ISBN.grid(row=1, column=2)

#Declare & position Entry components
text_Title = StringVar()
ent_Title = Entry(window,textvariable=text_Title)
ent_Title.grid(row=0, column=1)

text_Year = StringVar()
ent_Year =Entry(window,textvariable=text_Year)
ent_Year.grid(row=1, column=1)

text_Author = StringVar()
ent_Author =Entry(window,textvariable=text_Author)
ent_Author.grid(row=0, column=3)

text_ISBN = StringVar()
ent_ISBN = Entry(window,textvariable=text_ISBN)
ent_ISBN.grid(row=1, column=3)

#Declare & position listbox
listBox = Listbox(window,height=8,width=28)
listBox.grid(row=2, column=0,rowspan=6,columnspan=2)
listBox.bind('<<ListboxSelect>>',get_selected_row)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2,column=2,rowspan=6)

listBox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listBox.yview)

#Declare & position button
but_viewall = Button(window,text="View All",width = 12,command=command_view_all)
but_viewall.grid(row=2,column=3)

but_searchentry = Button(window,text="Search Entry",width = 12,command=command_search_entry)
but_searchentry.grid(row=3,column=3)

but_addentry = Button(window,text="Add Entry",width = 12,command=command_add_entry)
but_addentry.grid(row=4,column=3)

but_update = Button(window,text="Update",width = 12,command=command_update)
but_update.grid(row=5,column=3)

but_delete = Button(window,text="Delete",width = 12,command=command_delete)
but_delete.grid(row=6,column=3)

but_close = Button(window,text="Close",width = 12,command=command_close)
but_close.grid(row=7,column=3)

##Play continuously
window.mainloop()