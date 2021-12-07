
from tkinter import *

main = Tk()
main.geometry('800x700')


def add(arg=None):
    if entry.get() != '' :
        res = entry.get()
        text.insert( END ,"\n *  " + res)
        entry.delete(0,END)

def clear():
    text.delete(1.0 , END)

label = Label(main , text=" My ToDo List " , font=40 , bd=4 , fg='#000066').pack()

entry = Entry(main , width=40,bd=4 ,font=5 )
entry.focus()
entry.bind("<Return>",add)
entry.pack(padx=5, pady=8)

btn = Button(main , text="ADD" ,width=7,height=2, command=add)
btn.pack( padx=10, pady=10)

btn1 = Button(main , text="CLEAR" ,width=7,height=2, command=clear)
btn1.pack( padx=5, pady=5)


text = Text(main , bg='#e6e6ff' ,font=6)
text.pack( padx=5, pady=5)

label1 = Label(main , text="")
label1.pack( padx=5, pady=5)


main.mainloop()


