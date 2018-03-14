from tkinter import *
from tkinter import ttk
import pymysql

db = pymysql.connect("localhost", "root", "", "CDAC")
cursor = db.cursor()


def labels(framename, row, column, columnspan, height, width, labeltext, bg, fg):
    labelname = Label(framename, text=labeltext, bg=bg, fg=fg, height=height, width=width)
    labelname.grid(row=row, column=column, columnspan=columnspan)


def putingrid(name, row, column, columnspan, rowspan):
    name.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan)


def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: "%s"' % (index, value))


def user_panel(u, p):

    def backtoindex():
        f1.pack_forget()
        f2.pack_forget()
        f3.pack_forget()
        root.destroy()
        import index
        # index()

    def changepasswordfunc():
        f1.pack_forget()
        f2.pack_forget()
        f3.pack_forget()
        root.destroy()
        import changepassword
        changepassword.change_password(u, p)

    root = Tk()
    root.title("Registration Form!")
    # root.geometry("1000x600")
    root.resizable(False, False)

    # Header Frame
    f1 = Frame(root, bd=1, relief=RAISED)
    # Padding Label
    labels(f1, 1, 0, 1, 1, 5, "", "#f0f0f0", "#000000")
    # Image Label
    img = PhotoImage(file="321.gif")
    l1 = Label(f1, image=img, height=80, width=200, bd=2, relief=SUNKEN)
    # l1 = Label(f1, text="Hello", height=1, width=21, bd=2, relief=SUNKEN)
    putingrid(l1, 1, 1, 1, 1)
    l1.grid_configure(sticky=W)
    # Filler Label
    labels(f1, 1, 2, 1, 1, 1, "", "#f0f0f0", "#000000")
    # Login Button
    logoutbutton = Button(f1, text="Logout", command=backtoindex, width=15, bg="PowderBlue")
    logoutbutton.grid(row=1, column=3)
    # Padding Label
    labels(f1, 1, 4, 1, 1, 15, "", "#f0f0f0", "#000000")
    # Packing
    f1.grid_columnconfigure(1, weight=1)
    f1.pack(fill=X)
    # End of Header Frame

    # Middle Frame
    f2 = Frame(root, bg="#F0F0F0")
    # Padding Label
    labels(f2, 1, 0, 1, 1, 1, "", "#F0F0F0", "#000000")
    labels(f2, 2, 0, 1, 1, 5, "", "#F0F0F0", "#000000")
    listbox = Listbox(f2, selectmode="single", selectbackground="Green", relief=FLAT, bg="#F0F0F0",
                      font=5, highlightthickness=0)
    listbox.bind('<<ListboxSelect>>', onselect)
    listbox.insert(0, "►Give Test")
    listbox.insert(1, "►Check Result")
    listbox.insert(2, "►Manage Profile")
    listbox.insert(3, "►Change Password")
    listbox.grid(row=2, column=1)

    # Padding Label
    labels(f2, 2, 2, 1, 10, 5, "", "#F0F0F0", "#000000")

    # Main Frame
    f3 = Frame(f2)
    # Content for main Frame
    userlogo = PhotoImage(file="userlogo_small.png")
    doclogo = PhotoImage(file="document_logo.png")
    givetest = Button(f3, image=doclogo, text="Give Test", height=100, width=80, compound="top", padx=5, pady=5,
                        command="", bg="RED")
    putingrid(givetest, 2, 1, 1, 1)
    givetest.grid_configure(padx=(50, 50))
    givetest.grid_configure(pady=(50, 50))
    checkresult = Button(f3, image=doclogo, text="Check Result", height=100, width=80, compound="top", padx=5,
                           pady=5, bg="Yellow")
    putingrid(checkresult, 2, 2, 1, 1)
    checkresult.grid_configure(padx=(50, 50))
    manageprofile = Button(f3, image=userlogo, text="Manage Profile", height=100, width=80, compound="top", padx=5,
                          pady=5, bg="Green")
    putingrid(manageprofile, 2, 3, 1, 1)
    manageprofile.grid_configure(padx=(50, 50))
    changepassword = Button(f3, text="Change Password", height=2, width=80, compound="top", padx=5,
                            pady=5, bg="Orange", command=changepasswordfunc)
    putingrid(changepassword, 3, 1, 1, 1)
    changepassword.grid_configure(padx=(50, 50), columnspan=3)

    # Packing Main Frame
    f3.grid(row=2, column=3)
    f2.pack(fill=X, padx=(10, 50), pady=(10, 50))
    # End of Middle Frame

    # Packing Root
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()

# user_panel()
