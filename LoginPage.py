import os
import time
import tkinter
from tkinter import *
from tkinter import ttk
import pyttsx3

root = Tk()
root.title("Gas Detector")
root.minsize(height=500, width=800)
root.maxsize(height=500, width=800)
root.config(background="#f2c311")

photo = PhotoImage(file=r"Untitled.png")
im1 = Label(root, image=photo)
im1.place(x=300, y=100)

l0 = Label(root, background="#f2c311")
L0 = tkinter.StringVar()
l0.config(text="", font=("tajawel", 30, "bold"), justify="center")
l0.place(x=220, y=30)


def texting(letter, time, lab):
    global lst
    root.after(time, lambda: lst[lab].config(text=lst[lab].cget("text") + letter))


# We can now save the name of all labels and choose one every time when we call the function of texting with interval
def text(words,time1, lab):
    x = time1
    global lst
    for letter in words:
        texting(letter, x, lab)
        x += time1


text("Gas Detector Program",100, 0)

f1 = Frame(root, width=800, height=100, background="#0B2F3A")
f1.place(x=0, y=400)

l_name = Label(f1, text="UserName :", font=("tajawel", 16, "bold"), fg="gold", bg="#0B2F3A")
l_name.place(x=30, y=12)

name = tkinter.StringVar()
e1 = Entry(f1, font=("tajawel", 14, "bold"), width=15, textvariable=name)
e1.place(x=150, y=14)

l_pass = Label(f1, text="Password :", font=("tajawel", 16, "bold"), fg="gold", bg="#0B2F3A")
l_pass.place(x=30, y=50)

password = tkinter.StringVar()
e2 = Entry(f1, font=("tajawel", 14, "bold"), width=15, textvariable=password, show="•")
e2.place(x=150, y=50)

text = tkinter.StringVar() #it is real text
l3 = Label(f1, text="Please login to use the program", textvariable=text, font=("tajawel", 13, "bold"), fg="gold",
           bg="#0B2F3A")
l3.place(x=420, y=25)
lst = [l0, l3]

def disable():
    B2["state"] = DISABLED
    e1["state"] = DISABLED
    e2["state"] = DISABLED
    root.unbind("<Return>")


def log():
    if e1.get() == "" or e2.get() == "":
        text.set("Please fill the required info")
        #root.after(200,lambda :text("Please fill the required info",50,1))
    elif e1.get() == "Admin" and e2.get() == "123123":
        disable()
        root.after(200, lambda: text.set("Logging in please wait..."))
        # root.after(1000, lambda: pyttsx3.speak("Logging in...please wait..."))
        root.after(2000, lambda: os.startfile("practice2.py"))
        root.after(3000, lambda: root.destroy())
    else:
        root.after(200, lambda: text.set("Username or password incorrect \nTry again"))


B2 = Button(f1, text="Login", fg="black", bg="gold", font=("tajawel", 14, "bold"), height=2, command=log)
root.bind("<Return>", lambda event: log())
B2.place(x=330, y=17)

root.bind("<Escape>", lambda event: root.destroy())
root.mainloop()
