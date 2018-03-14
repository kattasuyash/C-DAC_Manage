from tkinter import *
from tkinter import ttk
import pymysql
db = pymysql.connect("localhost", "root", "", "CDAC")
cursor = db.cursor()


class One:

    def register_form(self):
        # Assigning Tk()
        root = Tk()
        root.title("Registration Form")
        root.geometry("1000x600")

        # First Frame F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
        f1 = Frame(root)

        # Top Label
        l1 = Label(f1, text="Registration Form", anchor=CENTER)
        l1.grid(row=2, column=1, sticky=NSEW)
        f1.grid_columnconfigure(1, weight=1)

        # Frame for Labels and Entries F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
        f2 = Frame(f1)

        fullnamelabel = Label(f2, text="Full Name: ", anchor=W)
        fullnamelabel.grid(row=2, column=0, sticky=W)
        fullnameentry = Entry(f2, width=50)
        fullnameentry.grid(row=2, column=1, sticky=W, pady=(10, 10))

        fnamelabel = Label(f2, text="Father's Name: ", anchor=W)
        fnamelabel.grid(row=3, column=0, sticky=W)
        fnameentry = Entry(f2, width=50)
        fnameentry.grid(row=3, column=1, sticky=W, pady=(10, 10))

        usernamelabel = Label(f2, text="UserName: ", anchor=W)
        usernamelabel.grid(row=4, column=0, sticky=W)
        usernameentry = Entry(f2, width=50)
        usernameentry.grid(row=4, column=1, sticky=W, pady=(10, 10))

        '''passwordlabel = Label(f2, text="Password: ", anchor=W)
        passwordlabel.grid(row=5, column=0, sticky=W)
        passwordentry = Entry(f2, width=50, show="*")
        passwordentry.grid(row=5, column=1, sticky=W, pady=(10, 10))

        repasslabel = Label(f2, text="ReType Password: ", anchor=W)
        repasslabel.grid(row=6, column=0, sticky=W)
        repassentry = Entry(f2, width=50, show="*")
        repassentry.grid(row=6, column=1, sticky=W, pady=(10, 10))'''

        mobilelabel = Label(f2, text="Mobile: ", anchor=W)
        mobilelabel.grid(row=7, column=0, sticky=W)
        mobileentry = Entry(f2, width=50)
        mobileentry.grid(row=7, column=1, sticky=W, pady=(10, 10))

        emaillabel = Label(f2, text="Email: ", anchor=W)
        emaillabel.grid(row=8, column=0, sticky=W)
        emailentry = Entry(f2, width=50)
        emailentry.grid(row=8, column=1, sticky=W, pady=(10, 10))

        doblabel = Label(f2, text="Date of Birth", anchor=W)
        doblabel.grid(row=9, column=0, sticky=W)

        # Creating Lists for Date of Birth ComboBoxes
        # Date List
        date2 = []
        for date1 in range(1, 32):
            date2.append(date1)
        # Year List
        year2 = []
        for year1 in range(2018, 1899, -1):
            year2.append(year1)
        # Month List
        month2 = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October"
                    ,"November", "December"]

        # Frame for Date of Birth ComboBoxes F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
        f4 = Frame(f2)
        # Date Combobox
        date = StringVar()
        date3 = ttk.Combobox(f4, textvariable=date, width=11)
        # courses['values'] = ("Date", date2)
        date3['values'] = date2
        date3.grid(row=1, column=1, padx=(1, 10), sticky=W)
        date3.current(0)
        # Month ComboBox
        month = StringVar()
        month3 = ttk.Combobox(f4, textvariable=month, width=11)
        month3['values'] = month2
        month3.grid(row=1, column=2, padx=(10, 10), sticky=W)
        month3.current(0)
        # Year ComboBox
        year = StringVar()
        year3 = ttk.Combobox(f4, textvariable=year, width=11)
        year3['values'] = year2
        year3.grid(row=1, column=3, padx=(10, 10), sticky=W)
        year3.current(0)
        # Packing f4 Frame F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
        f4.grid(row=9, column=1, pady=(10, 10), sticky=W)

        # Frame for Ratio Buttons F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
        f3 = Frame(f2)

        # Radio Buttons
        var = StringVar(root, value="0")
        genderlabel = Label(f3, text="Gender: ")
        genderlabel.grid(row=1, column=0, sticky=W)
        Radiobutton(f3, variable=var, value="male", text="Male").grid(row=1, column=2, padx=(0, 20), sticky=W)
        Radiobutton(f3, variable=var, value="female", text="Female").grid(row=1, column=3, padx=(20, 20), sticky=W)
        Radiobutton(f3, variable=var, value="third", text="Third").grid(row=1, column=4, padx=(20, 0), sticky=W)

        # ComboBox For Courses
        courselabel = Label(f3, text="Choose Course: ")
        courselabel.grid(row=2, column=0, pady=(10, 10))
        var1 = StringVar()
        courses = ttk.Combobox(f3, width=20, textvariable=var1)
        courses['values'] = ("--Select Course", "Core Python", "Advance Python", "Core Java", "Advance Java",
                             "Core Android", "Advance Android")
        courses.grid(row=2, column=2, padx=(10, 0), columnspan=3, sticky=W)
        courses.current(0)

        # ComboBox for College
        collegelabel = Label(f3, text="Choose College: ")
        collegelabel.grid(row=3, column=0, pady=(10, 10))
        var2 = StringVar()
        college = ttk.Combobox(f3, textvariable=var2)
        college['values'] = ("--Select College", "MASMS", "JECRC", "Rajasthan University", "Subodh College")
        college.grid(row=3, column=2, padx=(10, 0), columnspan=3, sticky=W)
        college.current(0)

        # ComboBox for Qualification
        quallabel = Label(f3, text="Qualification: ")
        quallabel.grid(row=4, column=0, pady=(10, 10))
        var3 = StringVar()
        qual = ttk.Combobox(f3, textvariable=var3)
        qual['values'] = ("--Qualification", "BCA", "MCA", "B.Tech", "M.Tech")
        qual.grid(row=4, column=2, padx=(10, 0), columnspan=3, sticky=W)
        qual.current(0)
        # Packing 3rd Frame F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
        f3.grid(row=10, column=0, sticky=W, pady=(10, 10), columnspan=3)

        # Function to Go Back
        def gobackfunc():
            f1.pack_forget()
            f2.grid_forget()
            f3.grid_forget()
            f4.grid_forget()
            root.destroy()
            import index
            # index()

        def error():
            errorlabel.config(text="Fields with Error are Marked in Red, Please Re-Check and Try Again.", fg="RED")

        def checkall():
            if (len(fullnameentry.get()) < 3 or len(fnameentry.get()) < 3 or len(usernameentry.get()) < 3
                    or len(mobileentry.get()) < 10 or len(emailentry.get()) < 6)\
                    or var.get() == "0" or var1.get() == "--Select College" or var2.get() == "--Select College" \
                    or var3.get() == "--Qualification":
                if len(fullnameentry.get()) < 3:
                    fullnamelabel.config(bg="RED", fg="White")
                if len(fnameentry.get()) < 3:
                    fnamelabel.config(bg="RED", fg="White")
                if len(usernameentry.get()) < 3:
                    usernamelabel.config(bg="RED", fg="White")
                '''if len(passwordentry.get()) < 6:
                    passwordlabel.config(bg="RED", fg="White")
                if len(repassentry.get()) < 6:
                    repasslabel.config(bg="RED", fg="White")'''
                if len(mobileentry.get()) < 10:
                    mobilelabel.config(bg="RED", fg="White")
                if len(emailentry.get()) < 6:
                    emaillabel.config(bg="RED", fg="White")
                if var.get() == "0":
                    genderlabel.config(bg="RED", fg="White")
                if courses.current() == 0:
                    courselabel.config(bg="RED", fg="White")
                if college.current() == 0:
                    collegelabel.config(bg="RED", fg="White")
                if qual.current() == 0:
                    quallabel.config(bg="RED", fg="White")
                error()

                return 0
            else:
                return 1

        def usertodb(password):
            fdate = (str(date3.get())+"-"+str(month3.get())+"-"+str(year3.get()))
            sql = "INSERT INTO userdata(ufullname," \
                  "uusername," \
                  "upassword," \
                  "umobile," \
                  "uemail," \
                  "udob," \
                  "ugender," \
                  "ufname," \
                  "uqualification," \
                  "ucollege," \
                  "ucourses)" \
                  "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
                  % (fullnameentry.get(),
                     usernameentry.get(),
                     password,
                     mobileentry.get(),
                     emailentry.get(),
                     fdate,
                     var.get(),
                     fnameentry.get(),
                     qual.get(),
                     college.get(),
                     courses.get())
            try:
                r = cursor.execute(sql)
                if r == 1:
                    print("Successfully Registered!")
                    db.commit()
                else:
                    print("Error in Registration!, Try Again!")
                    db.rollback()
            except Exception as e:
                print("Connection Error", e)
            finally:
                db.close()

        def submitfunc():
            n1 = checkall()
            if n1 == 0:
                print("ERROR!")
            if n1 == 1:
                import passwordsender
                password = passwordsender.passwordsender.send(passwordsender, emailentry.get())
                usertodb(password)
                gobackfunc()

        def autofill():
            if fullnameentry.get() == "":
                fullnameentry.insert(0, "Tester")
                fnameentry.insert(0, "Tester")
                usernameentry.insert(0, "Tester")
                mobileentry.insert(0, "9351590509")
                emailentry.insert(0, "kattasuyash@yahoo.com")
                var.set("male")
                courses.current(1)
                college.current(1)
                qual.current(1)

        errorlabel = Label(f2, width=50)
        errorlabel.grid(row=11, column=0, columnspan=3)

        cancelbutton = Button(f2, text="Cancel, Go Back!", command=gobackfunc, bg="RED", fg="#ffffff")
        cancelbutton.grid(row=12, column=0, pady=(10, 10), columnspan=1)

        submitbutton = Button(f2, text="Submit", width=40,  command=submitfunc, bg="GREEN", fg="#ffffff")
        submitbutton.grid(row=12, column=1, pady=(10, 10), columnspan=2)

        autofill = Button(f2, text="Auto-Fill", width=56,  command=autofill, bg="Purple", fg="#ffffff")
        autofill.grid(row=13, column=0, pady=(10, 10), columnspan=3, sticky=W)

        # Packing 2nd Frame F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
        f2.grid(row=3, column=1, columnspan=3)

        # Packing First Frame F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F  F
        f1.pack(fill=X)

        # Initializing tkinter Loop
        root.mainloop()


# One.register_form(One)
