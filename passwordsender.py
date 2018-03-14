import smtplib
from smtplib import *
import random
from win10toast import ToastNotifier
import time


class passwordsender:
    def send(self, to):

        one = str(random.randint(100000, 999999))

        print("Password is: ", one)

        # Windows Toast Notification-------------------------------
        toaster = ToastNotifier()
        toaster.show_toast("Password for Registration is:",
                           one,
                           duration=10)
        # Wait for threaded notification to finish
        # while toaster.notification_active():
        #   time.sleep(2)

        # Sending to Email-----------------------------------------
        '''try:
            # to = input("Enter Email Address for To User: ")
            gmail_user = "Your G-Mail ID"
            gmail_pwd = "Your Gmail Password"

            header = 'To: '+to+'\n'+'From: '+gmail_user+'\n'+'Subject: Password for Registration \n'
            msg = header + '\n Below is your Auto-Generated Password for Registration: \n'+one+'\n'
            try:
                    smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
                    smtpObj.ehlo()
                    smtpObj.starttls()
                    smtpObj.login(gmail_user, gmail_pwd)
                    smtpObj.sendmail(gmail_user, to, msg)
                    print("Successfully Sent Email.")
            except SMTPException as e:
                print("Un-abel to send Email.", e)
                smtpObj.close()
        except Exception as e:
            print("Error: ", e)'''
        return one
# passwordsender.send(passwordsender, 1)
