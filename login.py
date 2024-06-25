from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from hotel import HotelManagementSystem
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
        

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        
        self.bg=ImageTk.PhotoImage(file=r" enter your path    \hotel_management\hotel images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg ")# enter path of your file
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
        
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r" enter your path    \hotel_management\hotel images\LoginIconAppl.png")# enter path of your file
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="Get Started",font=("time new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)
        
        # -------------------label-------------------

        username=lbl=Label(frame,text="Username",font=("time new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)
        
        self.txtuser=ttk.Entry(frame,font=("time new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
       
        password=lbl=Label(frame,text="Password",font=("time new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)
        
        self.txtpass=ttk.Entry(frame,font=("time new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
        
        # =======================Icon Images================

        img2=Image.open(r" enter your path    \hotel_management\hotel images\LoginIconAppl.png")# enter path of your file
        img2=img2.resize((25,25),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)

        img3=Image.open(r" enter your path    \hotel_management\hotel images\lock-512.png")# enter path of your file
        img3=img3.resize((25,25),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg2=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=395,width=25,height=25)
        
        # -------------------LoginButton-------------------

        loginbtn=Button(frame,text="Login",command=self.login,font=("time new roman",15,"bold"),cursor="hand2",bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red") 
        loginbtn.place(x=110,y=300,width=120,height=35)
        
        # -------------------RegisterButton-------------------

        registerbtn=Button(frame,text="New User Register",command=self.rigister_window,font=("time new roman",10,"bold"),cursor="hand2",borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black") 
        registerbtn.place(x=15,y=350,width=160)
        
        # -------------------ForgetPasswordBtn-------------------

        registerbtn=Button(frame,text="Forget Password",command=self.forgot_password_window,font=("time new roman",10,"bold"),cursor="hand2",borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black") 
        registerbtn.place(x=10,y=370,width=160)
        
    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
        
        
    def login(self):
        if self.txtuser.get()==""or self.txtpass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to the System",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="enter your database password",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where fname=%s and password=%s",(
                                                                                    self.txtuser.get(), 
                                                                                    self.txtpass.get()
                                                                                 ))
        
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin",parent=self.root)
                if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # ========================Send Login details====================

            # Send login details to the user's email
            try:
                # Connect to the database
                conn = mysql.connector.connect(host="localhost", username="root", password="enter your database password", database="mydata")
                my_cursor = conn.cursor()

                # Fetch user's email from the database
                query = "SELECT email FROM register WHERE fname = %s"  # Assuming you have a UserID to identify the user
                user_id = self.txtuser.get()  # Update with the actual user ID or fetch it from your application
                my_cursor.execute(query, (user_id,))
                row = my_cursor.fetchone()

                if row:
                    user_email = row[0]  # Extract the email from the fetched row
                    # Set up the SMTP server
                    smtp_server = "smtp.gmail.com"  # Update with your SMTP server details
                    port = 587  # Update with your SMTP server port (587 is commonly used for TLS)
                    sender_email = "aryanamipara3@gmail.com"  # Update with your email address
                    sender_password = "bagtsanieskqprmk"  # Update with your email password

                    # Create a secure SSL context
                    smtp = smtplib.SMTP(smtp_server, port)
                    smtp.starttls()
                    smtp.login(sender_email, sender_password)

                    # Construct the message
                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = user_email  # Use the user's email
                    msg['Subject'] = "Your Login Details"

                    # Compose the message body
                    message = f"""
                    Dear User,

                    Your Login is successfull.
                    Here are your login details:
                    
                    Your UserID: {self.txtuser.get()}
                    Your Password: ***

                    Regards,
                    Hotel Management Team
                    """

                    msg.attach(MIMEText(message, 'plain'))

                    # Send the email
                    smtp.send_message(msg)
                    smtp.quit()
                else:
                    messagebox.showerror("Email Error", "User email not found.",parent=self.root)
            except Exception as e:
                messagebox.showerror("Email Error", f"Failed to send email: {str(e)}",parent=self.root)
            finally:
                # Close the database connection
                my_cursor.close()
                conn.close()


    # ================================reset password==================================

    def reset_pass(self):
        if self.combo_security_Q.get()=="":
            messagebox.showerror("Error","Select the security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="enter your database password",database="mydata")
            my_cursor=conn.cursor()
            qury=("select * from register where fname=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get())
            my_cursor.execute(qury,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where fname=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, please login with the new password",parent=self.root2)
                self.root2.destroy()

    

    # ===============================forgot password window============================

    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please write the Email address to reset the password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="enter your database password",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where fname=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","Please enter the valid user name",parent=self.root)

            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("time new roman",20,"bold"),fg="red")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),fg="black")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Your Birth Place","Your Friend Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)

                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset", command=self.reset_pass,font=("times new roman",15),fg="white",bg="green")
                btn.place(x=135,y=290)



class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ===================variables=======================

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        # ==========================bg image=======================

        self.bg=ImageTk.PhotoImage(file=r" enter your path    \hotel_management\hotel images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")# enter path of your file

        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # ==========================left image======================
        
        self.bg1=ImageTk.PhotoImage(file=r" enter your path    \hotel_management\hotel images\thought-good-morning-messages-LoveSove.jpg")# enter path of your file

        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        # ======================main frame==========================

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="Register here",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)

        # ===================label and entry========================

        # -------------------row1-------------------

        fname=Label(frame,text="Frist Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        # -------------------row2-------------------

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white",fg="black")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        # -------------------row3-------------------

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Your Birth Place","Your Friend Name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=270,width=250)

        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        # -------------------row4-------------------

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        # ===================chech button======================

        self.var_check=IntVar()
        Checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms and Conditions",font=("times new roman",12,"bold"),cursor="hand2",onvalue=1,offvalue=0)
        Checkbtn.place(x=50,y=380)

        # ==================buttons============================

        img=Image.open(r"enter your path    \hotel_management\hotel images\register-now-button1.jpg")# enter path of your file
        img=img.resize((200,50),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"enter your  path   \hotel_management\hotel images\loginpng.png")# enter path of your file
        img1=img1.resize((200,50),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)

    # ====================Function declaration================
    
    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="" or self.var_SecurityA.get()=="" or self.var_pass.get()=="" or self.var_confpass.get=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Both Password and Confirm Password must be same",parent=self.root)

        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree our Terms and Conditions",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist, Please try another email",parent=self.root)

            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_fname.get(),
                                                                                    self.var_lname.get(),
                                                                                    self.var_contact.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_securityQ.get(),
                                                                                    self.var_SecurityA.get(),
                                                                                    self.var_pass.get()
                                                                                    
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Welcome to the System",parent=self.root)            
            
    def return_login(self):
        self.root.destroy()

        
if __name__=="__main__":
    main()