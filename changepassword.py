import pymysql
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Frame
from tkinter import messagebox


def change_password(oldusername, oldpassword):
    root = Tk()
    root.title("Change Password")
    root.resizable(False, False)

    def submit2(new_password, checkpassword):

        def goback():
            # messagebox.showinfo("Success!", "Password Changed Successfully!")
            f1.grid_forget()
            root.destroy()
            import index

        # Connecting to Database
        db = pymysql.connect("localhost", "root", "", "CDAC")
        cursor = db.cursor()

        changer = "update USERDATA set upassword='%s' Where UUSERNAME='%s' and UPASSWORD='%s'" % (new_password, oldusername, checkpassword)
        changer1 = "update adminuser set password='%s' Where username='%s' and password='%s'" % (new_password, oldusername, checkpassword)
        n3 = 0

        try:
            r = cursor.execute(changer1)
            if r > 0:
                n3 = 2
                messagebox.showinfo("Success!", "AdminUser's Password Changed!")
                goback()
            else:
                messagebox.showinfo("Not adminuser", "no records in AdminUser")
            db.commit()

        except Exception as e:
            db.rollback()
            print("Connection Error", e)
        if n3 == 0:
            try:
                r = cursor.execute(changer)
                if r > 0:
                    cursor.execute(changer)
                    n3 = 1
                    messagebox.showinfo("Success!", "User's Password Changed!")
                    goback()
                else:
                    messagebox.showinfo("Not userdata", "no records in UserData")
                db.commit()
            except Exception as e:
                db.rollback()
                print("Connection Error", e)
        return n3

    def cancel():
        messagebox.showinfo("Cancel", "Changes Cancelled, Going back")
        f1.grid_forget()
        root.destroy()
        import index

    def submit1():
        submit2(str(npe.get()), str(ope.get()))

    f1 = Frame(root)

    Label(f1, text="Change Password", anchor='center').grid(row=1, column=0, columnspan=3, pady=(10, 10))

    Label(f1, text="Old Password: ", anchor="w").grid(row=2, column=1)
    ope = Entry(f1)
    ope.grid(row=2, column=2)

    Label(f1, text="New Password: ", anchor="w").grid(row=3, column=1)
    npe = Entry(f1)
    npe.grid(row=3, column=2)

    Label(f1, text="Re-Type New Password: ", anchor="w").grid(row=4, column=1)
    rpe = Entry(f1)
    rpe.grid(row=4, column=2)

    submit = Button(f1, text="Submit", command=submit1, bg="Green", width=15)
    submit.grid(row=5, column=2)

    cancel = Button(f1, text="Cancel", command=cancel, bg="#ff5555", width=15)
    cancel.grid(row=5, column=1, pady=(10, 10))

    f1.grid(row=1, column=1, padx=(20, 20), pady=(10, 20))
    root.mainloop()

# change_password("admin", "password")
