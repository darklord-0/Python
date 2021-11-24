import random
import string
import clipboard
from tkinter import *


#initialize window
my_window = Tk()
my_window.geometry("650x650")
my_window.resizable(True,True)
my_window.title(" PASSWORD GENERATOR")
 

#heading
Label(my_window, text = ' RANDOM PASSWORD GENERATOR ' , font ='arial 15 bold underline').pack(padx=10,pady=10)
Label(my_window, text =' Made By - HARSHIT ', font ='algerian 10 bold italic').pack(side = BOTTOM , padx=10,pady=10)


#select password length
pass_label = Label(my_window, text = ' PASSWORD LENGTH ', font = 'arial 10 ').pack(padx=10,pady=10)
pass_len = IntVar()
length = Spinbox(my_window, from_ = 5, to_ = 25 , textvariable = pass_len , width = 15).pack(padx=10,pady=10)


#define function

pass_str = StringVar()

def Generator_Pwd():
   
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    symbols= string.punctuation
    num = string.digits

    all = upper + lower + symbols + num

    pwd = "".join(random.choices(all ,k = pass_len.get())) 
    print(pwd)

    pass_str.set(pwd)


#button
Button(my_window, text = "GENERATE PASSWORD" , command = Generator_Pwd , width=20).pack(padx=10,pady=10)

Entry(my_window , textvariable = pass_str , width=30).pack(padx=10,pady=10)


#function to copy

def Copy_password():
    clipboard.copy(pass_str.get())

Button(my_window, text = 'COPY ', command = Copy_password).pack(padx=10,pady=10)


# loop to run program
my_window.mainloop()



