from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import smtplib
import mysql.connector
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from twilio.rest import Client
import os
from tkinter import messagebox
import subprocess
from flask import Flask, render_template, request
import pandas as pd

class Feedback:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1293x560+230+220")

        # ===============title=====================

        lbl_title=Label(self.root,text="FEEDBACK FORM",font=("times new roman",18,"bold"),bg="black",fg="lightgrey",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Feedback",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)

        # =================logo====================

        img2=Image.open(r"enter path    \hotel_management\hotel images\llogo.webp") #enter path of your file
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)

        # -------------------Customer contact-------------------

        lbl_cust_contact=Label(labelframeleft,text="Customer Contact:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=1,column=0)

        # Validate function to check if input is valid
        validate_contact = self.root.register(self.validate_contact)

        # Entry for customer contact
        self.var_contact = StringVar()
        entry_contact = ttk.Entry(labelframeleft,textvariable=self.var_contact, font=("arial", 13), width=21, validate="key", validatecommand=(validate_contact, '%P'))
        entry_contact.grid(row=1,column=1)

        def on_enter(e):
            entry_contact.delete(0,"end")

        def on_leave(e):
            name=entry_contact.get()
            if name=="":
                entry_contact.insert(0,"Enter Customer's Contact")

        entry_contact.insert(0,"Enter Customer's Contact")
        entry_contact.bind("<FocusIn>",on_enter)
        entry_contact.bind("<FocusOut>",on_leave)

        # -------------------Send Email Button-------------------
        btnSearch=Button(labelframeleft,text="Send Email",command=self.fetch,font=("arial",11,"bold"),bg="black",fg="gold",width=10,cursor="hand2")
        btnSearch.grid(row=1,column=2)

    # =====================Search Data========================
    
    def fetch(self):
        # Send a QR to user's email that will collect the Feedback From the user
        try:
            # Connect to the database
            conn = mysql.connector.connect(host="localhost", username="root", password=" enter your database password", database="management")
            my_cursor = conn.cursor()

            # Fetch customer's email from the database
            query = "SELECT Email FROM customer WHERE Mobile = %s"  # Assuming you have a CustomerID to identify the customer
            customer_id = self.var_contact.get()  # Update with the actual customer ID or fetch it from your application
            my_cursor.execute(query, (customer_id,))
            row = my_cursor.fetchone()

            if row:
                customer_email = row[0]  # Extract the email from the fetched row
                # Set up the SMTP server
                smtp_server = "enter your smtp server name "  # Update with your SMTP server details
                port = 587  # Update with your SMTP server port (587 is commonly used for TLS)
                sender_email = " enter your email address"  # Update with your email address
                sender_password = " enter your password"  # Update with your email password

                # Create a secure SSL context
                smtp = smtplib.SMTP(smtp_server, port)
                smtp.starttls()
                smtp.login(sender_email, sender_password)

                # Construct the message
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = customer_email  # Use the customer's email
                msg['Subject'] = "Feedback"

                # Compose the message body
                message = f"""
                Dear Customer,

                Please give your valuable feedback by scaning the QR code given below.
                Your feedback will help us to improve our services.
                
                Thank you for choosing our hotel!

                Regards,
                Feedback Team
                """

                msg.attach(MIMEText(message, 'plain'))

                # Attach the image to the email
                image_path = r'enter path'  # Update with the correct path to your image file
                with open(image_path, 'rb') as img:
                    img_data = img.read()
                    image = MIMEImage(img_data, name=os.path.basename(image_path))
                    msg.attach(image)

                # Send the email
                smtp.send_message(msg)
                smtp.quit()

                messagebox.showinfo("Email Sent", "Feedback requesr sent to customer's email successfully.",parent=self.root)
            else:
                messagebox.showerror("Email Error", "Customer email not found.",parent=self.root)
        except Exception as e:
            messagebox.showerror("Email Error", f"Failed to send email: {str(e)}",parent=self.root)
        finally:
            # Close the database connection
            my_cursor.close()
            conn.close()


    # =========================Condition Check==================

    def validate_contact(self, new_value):
        # Check if the new value is empty
        if not new_value:
            return True
        
        if new_value == "Enter Customer's Contact":
            return True

        # Check if the new value contains non-digit characters
        if not new_value.isdigit():
            messagebox.showerror("Error", "Please enter only numbers in the contact field.",parent=self.root)
            return False

        # Check if the length is more than 10 digits
        if len(new_value) > 10:
            messagebox.showerror("Error", "Please enter up to 10 digits in the contact field.",parent=self.root)
            return False

        return True


if __name__ == '__main__':
    root=Tk()
    obj=Feedback(root)
    root.mainloop()