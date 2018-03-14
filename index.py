from tkinter import *
import tkinter as tk
from LoginChecker import tester
import AdminPanel
import UserPanel
import Register_Form

# Setting Window
root = Tk()
root.title("Welcome to CDAC, Login to continue...")
root.config(bg="#F9F9F9")
root.geometry("1000x600")

tk.img = PhotoImage(file="321.gif")


def registerfunc():
    f1.pack_forget()
    f2.pack_forget()
    f3.pack_forget()
    f4.pack_forget()
    root.destroy()
    Register_Form.One.register_form(registerfunc)

def loginfunc():
    n1 = usernamee.get()
    n2 = passworde.get()
    n3 = tester.checkerone(0, n1, n2)
    if n3 == 1:
        loginlabel.config(text="Logged in Successfully!", fg="Green")
        print("User Logged in Successfully")
        f1.pack_forget()
        f2.pack_forget()
        f3.pack_forget()
        f4.pack_forget()
        root.destroy()
        UserPanel.user_panel(n1, n2)
    elif n3 == 2:
        loginlabel.config(text="Logged in Successfully!", fg="Green")
        print("Admin Logged in Successfully")
        f1.pack_forget()
        f2.pack_forget()
        f3.pack_forget()
        f4.pack_forget()
        root.destroy()
        AdminPanel.admin_panel(n1, n2)
    else:
        loginlabel.config(text="Username and Password doesn't Match!", fg="RED")


def labels(framename, row, column, columnspan, height, width, labeltext, bg, fg):
    labelname = Label(framename, text=labeltext, bg=bg, fg=fg, height=height, width=width)
    labelname.grid(row=row, column=column, columnspan=columnspan)


def putingrid(name, row, column, columnspan, rowspan):
    name.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)


f2 = Frame(root, bd=5, relief=SUNKEN, bg="#F9F9F9")
# Logo Image Label
Label(f2, image=tk.img, height=80, width=200).grid(row=1, column=0, sticky=W)
# Label(f2, text="Hello", height=1, width=21).grid(row=1, column=0, sticky=W)
Label(f2, text="", width=100, bg="#F9F9F9").grid(row=1, column=1, sticky='we')
# Register Button
registerbutton = Button(f2, text="Register HERE!", bg="PowderBlue", command=registerfunc)
registerbutton.grid(row=1, column=2, sticky=E)
labels(f2, 1, 3, 1, 1, 10, "", "#F9F9F9", "#000000")
# Packing Frame
f2.grid_columnconfigure(1, weight=1)
f2.pack(fill=X)

f3 = Frame(root, bg="#F9F9F9")
# Spacer
labels(f3, 0, 0, 50, 10, 20, "", "#F9F9F9", "#000000")
f3.pack(fill=X)

f1 = Frame(root, bd=5, relief=RIDGE, bg="#F9F9F9")

# Spacer
labels(f1, 2, 0, 1, 1, 2, "", "#F9F9F9", "#000000")
# Username
labels(f1, 3, 1, 1, 1, 25, "Username: ", "#F9F9F9", "#000000")
usernamee = Entry(f1, width=30)
putingrid(usernamee, 3, 2, 1, 1)
# Password
labels(f1, 4, 1, 1, 1, 25, "Password: ", "#F9F9F9", "#000000")
passworde = Entry(f1, show="*", width=30)
putingrid(passworde, 4, 2, 1, 1)
# Login Buttons
loginButton = Button(f1, text="Login", command=loginfunc, width=25, bg="#8cde6b")
putingrid(loginButton, 5, 2, 1, 1)
forgotpass = Button(f1, text="Forgot Password", command="forgotpassfunc", width=25, bg="PowderBlue")
putingrid(forgotpass, 5, 1, 1, 1)
# Message label
loginlabel = Label(f1, text="", fg="RED", height=1, bg="#F9F9F9")
putingrid(loginlabel, 6, 1, 2, 1)
# Spacer
labels(f1, 2, 3, 2, 1, 2, "", "#F9F9F9", "#000000")

f1.pack()

f4 = Frame(root, bg="#F9F9F9")
# Spacer
labels(f4, 0, 0, 50, 10, 20, "", "#F9F9F9", "#000000")
f4.pack(fill=X)

root.mainloop()
