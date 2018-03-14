import pymysql
class tester:
    def checkerone(self, n1, n2):
        # Connecting to Database
        db = pymysql.connect("localhost", "root", "", "CDAC")
        cursor = db.cursor()

        user = "SELECT * FROM USERDATA WHERE UUSERNAME='%s' and UPASSWORD='%s'" % (n1, n2)
        admin = "select * from adminuser where username='%s' and password='%s'" % (n1, n2)
        n3 = 0


        try:
            cursor.execute(admin)
            rows = cursor.fetchall()
            # print(rows)
            for row in rows:
                username = row[1]
                password = row[2]
                n3 = 2
        except Exception as e:
            print("Connection Error", e)
        if n3 == 0:
            try:
                cursor.execute(user)
                rows = cursor.fetchall()
                # print(rows)
                for row in rows:
                    UID = row[0]
                    UUSERNAME = row[2]
                    UPASSWORD = row[3]
                    # print(UID, "\t", UUSERNAME, "\t", UPASSWORD)
                    n3 = 1
            except Exception as e:
                print("Connection Error", e)
        return n3
