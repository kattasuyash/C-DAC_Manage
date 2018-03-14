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


def admin_panel(u, p):

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
    listbox.insert(0, "►Manage Users")
    listbox.insert(1, "►Manage Subject")
    listbox.insert(2, "►Manage Results")
    listbox.insert(3, "►Manage Exam")
    listbox.insert(4, "►Change Password")
    listbox.grid(row=2, column=1)

    # Padding Label
    labels(f2, 2, 2, 1, 10, 5, "", "#F0F0F0", "#000000")

    # Manage user Function
    def manageuserfunc():
        # Forgetting Main Frame
        f3.grid_forget()
        # Creating New Frame
        f4 = Frame(f2)
        # Main Showcase
        tree = ttk.Treeview(f4)

        '''vsb = ttk.Scrollbar(f4, orient="horizontal", command=tree.xview)
        vsb.pack(side='bottom', fill='x')

        tree.configure(xscrollcommand=vsb.set)'''

        tree["columns"] = ("ufullname", "uusername", "upassword", "umobile", "uemail", "udob", "ugender"
                           , "ufname", "uqualification", "ucollege", "ucourses")
        # tree['show'] = 'headings'
        # tree.column("uid", width=100)
        tree.column("ufullname", width=70)
        tree.column("uusername", width=70)
        tree.column("upassword", width=70)
        tree.column("umobile", width=80)
        tree.column("uemail", width=100)
        tree.column("udob", width=80)
        tree.column("ugender", width=50)
        tree.column("ufname", width=70)
        tree.column("uqualification", width=70)
        tree.column("ucollege", width=50)
        tree.column("ucourses", width=80)

        tree.heading("#0", text='UID', anchor='center')
        tree.column("#0", anchor='w', width=30)
        tree.heading("ufullname", text='Full Name')
        tree.heading("uusername", text='Username')
        tree.heading("upassword", text='Password')
        tree.heading("umobile", text='Mobile')
        tree.heading("uemail", text='E-Mail')
        tree.heading("udob", text='Date of Birth')
        tree.heading("ugender", text='Gender')
        tree.heading("ufname", text='Fathers Name')
        tree.heading("uqualification", text='Qualification')
        tree.heading("ucollege", text='College')
        tree.heading("ucourses", text='Courses')

        sql = "SELECT * FROM userdata"

        try:
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                uid = row[0]
                ufullname = row[1]
                uusername = row[2]
                upassword = row[3]
                umobile = row[4]
                uemail = row[5]
                udob = row[6]
                ugender = row[7]
                ufname = row[8]
                uqualification = row[9]
                ucollege = row[10]
                ucourses = row[11]
                tree.insert("", uid, text=uid, values=(ufullname, uusername, upassword, umobile, uemail, udob, ugender,
                                                       ufname, uqualification, ucollege, ucourses))
        except Exception as e:
            print("ERROR :", e)
        tree.pack()

        f5 = Frame(f4)
        addbutton = Button(f5, text="Add User", command="adduser", bg="PowderBlue", width=20)
        addbutton.grid(row=1, column=1, padx=(20, 20), pady=(10, 10))
        delbutton = Button(f5, text="Delete User", command="deluser", bg="PowderBlue", width=20)
        delbutton.grid(row=1, column=2, padx=(20, 20))
        editbutton = Button(f5, text="Edit User", command="edituser", bg="PowderBlue", width=20)
        editbutton.grid(row=1, column=3, padx=(20, 20))
        makeadminbutton = Button(f5, text="Make Admin", command="adminuser", bg="PowderBlue", width=20)
        makeadminbutton.grid(row=1, column=4, padx=(20, 20))
        f5.pack(fill="x")

        # Putting F4 Frame into Grid
        f4.grid(row=2, column=3)

    # Main Frame
    f3 = Frame(f2)
    # Content for main Frame
    userlogo = PhotoImage(file="userlogo_small.png")
    doclogo = PhotoImage(file="document_logo.png")
    manageuser = Button(f3, image=userlogo, text="Manage User", height=100, width=80, compound="top", padx=5, pady=5,
                        command=manageuserfunc)
    putingrid(manageuser, 2, 1, 1, 1)
    manageuser.grid_configure(padx=(50, 50))
    manageuser.grid_configure(pady=(50, 50))
    managesubject = Button(f3, image=doclogo, text="Manage Subject", height=100, width=80, compound="top", padx=5,
                           pady=5)
    putingrid(managesubject, 2, 2, 1, 1)
    managesubject.grid_configure(padx=(50, 50))
    manageresult = Button(f3, image=userlogo, text="Manage Result", height=100, width=80, compound="top", padx=5,
                          pady=5)
    putingrid(manageresult, 2, 3, 1, 1)
    manageresult.grid_configure(padx=(50, 50))
    testconductor = Button(f3, image=userlogo, text="Test Conductor", height=100, width=80, compound="top", padx=5,
                           pady=5)
    putingrid(testconductor, 3, 1, 1, 1)
    testconductor.grid_configure(padx=(50, 50))
    managetest = Button(f3, image=userlogo, text="Manage Test", height=100, width=80, compound="top", padx=5, pady=5)
    putingrid(managetest, 3, 2, 1, 1)
    managetest.grid_configure(padx=(50, 50))
    changepassword = Button(f3, image=userlogo, text="Change Password", height=100, width=80, compound="top", padx=5,
                            pady=5, command=changepasswordfunc)
    putingrid(changepassword, 3, 3, 1, 1)
    changepassword.grid_configure(padx=(50, 50))

    # Packing Main Frame
    f3.grid(row=2, column=3)
    f2.pack(fill=X, padx=(10, 50), pady=(10, 50))
    # End of Middle Frame

    # Packing Root
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()

# admin_panel()
