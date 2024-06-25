from tkinter import*
from tkcalendar import*
from PIL import Image,ImageTk
from tkinter import ttk
from datetime import datetime
import mysql.connector
from tkinter import messagebox
from tkcalendar import Calendar
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
from twilio.rest import Client

class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1293x560+230+220")

        # ===============variables=================

        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomNo=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_subtotal=StringVar()
        self.var_total=StringVar()

        # ===============title=====================

        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="lightgrey",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # =================logo====================

        img2=Image.open(r"enter your path    \hotel_management\hotel images\llogo.webp")# enter path of your file
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)

        # ====================lableFrame=====================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking Details",font=("arial",12,"bold"),padx=2,pady=6)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # ====================lables and entry==============

        # -------------------Customer contact-------------------

        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        # Validate function to check if input is valid
        validate_contact = self.root.register(self.validate_contact)

        # Entry widget for customer contact with a default placeholder text
        placeholder_text = "Enter Customer Contact"
        self.var_contact = StringVar()
        self.var_contact.set(placeholder_text)
        entry_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, font=("arial", 13), width=21, validate="key", validatecommand=(validate_contact, '%P'))
        entry_contact.grid(row=0,column=1,sticky=W)

        # Function to handle the placeholder text and user input
        def on_entry_click(event):
            if self.var_contact.get() == placeholder_text:
                entry_contact.delete(0, END)  # Clear the placeholder text
                entry_contact.config(foreground='black')  # Change text color to black

        # Bind the function to the entry widget
        entry_contact.bind('<FocusIn>', on_entry_click)

        # Function to handle the case when focus is lost without input
        def on_entry_focusout(event):
            if not self.var_contact.get():
                entry_contact.insert(0, placeholder_text)  # Restore placeholder text
                entry_contact.config(foreground='gray')  # Change text color to gray

        # Bind the function to handle focus out event
        entry_contact.bind('<FocusOut>', on_entry_focusout)

        # -------------------Fetch Data Button-------------------

        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",9,"bold"),bg="black",fg="pink",width=8,cursor="hand2")
        btnFetchData.place(x=347,y=4)

        # -------------------Check_in Date-------------------

        check_in_date=Label(labelframeleft,font=("arial",12,"bold"),text="Check_in Date:",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)

        # Entry widget for customer contact with a default placeholder text
        placeholder_text1 = "Select Check-in Date"
        self.var_checkin = StringVar()
        self.var_checkin.set(placeholder_text1)
        txt_check_in_date=Entry(labelframeleft,textvariable=self.var_checkin,font=("arial",13),width=21,state="readonly")
        txt_check_in_date.grid(row=1,column=1,sticky=W)

        # Function to handle the placeholder text and user input
        def on_entry_click(event):
            if self.var_checkin.get() == placeholder_text1:
                txt_check_in_date.delete(0, END)  # Clear the placeholder text
                txt_check_in_date.config(foreground='black')  # Change text color to black

        # Bind the function to the entry widget
        txt_check_in_date.bind('<FocusIn>', on_entry_click)

        # Function to handle the case when focus is lost without input
        def on_entry_focusout(event):
            if not self.var_checkin.get():
                txt_check_in_date.insert(0, placeholder_text1)  # Restore placeholder text
                txt_check_in_date.config(foreground='gray')  # Change text color to gray

        # Bind the function to handle focus out event
        txt_check_in_date.bind('<FocusOut>', on_entry_focusout)

        # -------------------Check_in Date Button-------------------

        btn_checkin_calendar = Button(self.root, text="Select Date",bg="black",fg="orange", command=self.open_checkin_calendar,cursor="hand2")
        btn_checkin_calendar.pack()
        btn_checkin_calendar.place(x=357,y=116)

        # -------------------Check_out Date-------------------

        lbl_Check_out=Label(labelframeleft,font=("arial",12,"bold"),text="Check_Out Date:",padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)

        # Entry widget for customer contact with a default placeholder text
        placeholder_text2 = "Select Check-out Date"
        self.var_checkout = StringVar()
        self.var_checkout.set(placeholder_text2)
        txt_Check_out=Entry(labelframeleft,textvariable=self.var_checkout,font=("arial",13),width=21,state="readonly")
        txt_Check_out.grid(row=2,column=1,sticky=W)

        # Function to handle the placeholder text and user input
        def on_entry_click(event):
            if self.var_checkout.get() == placeholder_text2:
                txt_Check_out.delete(0, END)  # Clear the placeholder text
                txt_Check_out.config(foreground='black')  # Change text color to black

        # Bind the function to the entry widget
        txt_Check_out.bind('<FocusIn>', on_entry_click)

        # Function to handle the case when focus is lost without input
        def on_entry_focusout(event):
            if not self.var_checkout.get():
                txt_Check_out.insert(0, placeholder_text2)  # Restore placeholder text
                txt_Check_out.config(foreground='gray')  # Change text color to gray

        # Bind the function to handle focus out event
        txt_Check_out.bind('<FocusOut>', on_entry_focusout)

        # -------------------Check_out Date Button-------------------

        btn_checkout_calendar = Button(self.root, text="Select Date",bg="black",fg="orange", command=self.open_checkout_calendar,cursor="hand2")
        btn_checkout_calendar.pack()
        btn_checkout_calendar.place(x=357,y=151)

        # -------------------Room Type-------------------

        label_RoomType=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12),width=27,state="readonly")
        # Add a placeholder value to the Combobox
        combo_RoomType.set("Select Room Type")
        combo_RoomType["value"]=("Single","Double","Laxary")

        # Function to handle Combobox selection changes
        def on_room_type_select(event):
            selected_room_type = combo_RoomType.get()
            if selected_room_type == "Select Room Type":
                # Handle placeholder selection
                combo_RoomType.delete(0, END)  # Clear the entry
            else:
                # Handle actual room type selection
                combo_RoomType.delete(0, END)  # Clear the entry
                combo_RoomType.insert(0, selected_room_type)  # Insert the selected room type

        # Bind the function to the Combobox selection event
        combo_RoomType.bind("<<ComboboxSelected>>", on_room_type_select)

        # Place the Combobox on the grid
        combo_RoomType.grid(row=3,column=1)

        # -------------------Room No-------------------

        lblRoom_no=Label(labelframeleft,font=("arial",12,"bold"),text="Rooms No:",padx=2,pady=6)
        lblRoom_no.grid(row=4,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows=my_cursor.fetchall()

        combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_roomNo,font=("arial",12),width=27,state="readonly")
        # Add a placeholder value to the Combobox
        combo_RoomNo.set("Select Room No")
        combo_RoomNo["value"]=rows

        # Function to handle Combobox selection changes
        def on_select(event):
            selected_room = combo_RoomNo.get()
            if selected_room == "Select Room No":
                # Handle placeholder selection
                combo_RoomNo.delete(0, END)  # Clear the entry
            else:
                # Handle actual room selection
                combo_RoomNo.delete(0, END)  # Clear the entry
                combo_RoomNo.insert(0, selected_room)  # Insert the selected room number

        # Bind the function to the Combobox selection event
        combo_RoomNo.bind("<<ComboboxSelected>>", on_select)

        # Place the Combobox on the grid
        combo_RoomNo.grid(row=4,column=1)

        # -------------------Meal-------------------

        lblMeal=Label(labelframeleft,font=("arial",12,"bold"),text="Meal:",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)

        combo_meal=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("arial",12),width=27,state="readonly")
        # Add a placeholder value to the Combobox
        combo_meal.set("Select Meal")
        combo_meal["value"]=("Breakfast","Lunch","Dinner","All")

        # Function to handle Combobox selection changes
        def on_meal_select(event):
            selected_room_type = combo_RoomType.get()
            if selected_room_type == "Select Meal":
                # Handle placeholder selection
                combo_RoomType.delete(0, END)  # Clear the entry
            else:
                # Handle actual meal selection
                combo_RoomType.delete(0, END)  # Clear the entry
                combo_RoomType.insert(0, selected_room_type)  # Insert the selected meal

        # Bind the function to the Combobox selection event
        combo_RoomType.bind("<<ComboboxSelected>>", on_meal_select)

        # Place the Combobox on the grid
        combo_meal.grid(row=5,column=1)

        # -------------------No Of Days-------------------

        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="No of Days:",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)

        txtNoOfDays=Entry(labelframeleft,textvariable=self.var_noofdays,font=("arial",13,"bold"),width=29,state="readonly")
        txtNoOfDays.grid(row=6,column=1)

        # -------------------Paid Tax-------------------

        lblpaid_tax=Label(labelframeleft,font=("arial",12,"bold"),text="Paid Tax:",padx=2,pady=6)
        lblpaid_tax.grid(row=7,column=0,sticky=W)

        txtpaid_tax=Entry(labelframeleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29,state="readonly")
        txtpaid_tax.grid(row=7,column=1)

        # -------------------Sub Total-------------------

        lblsub_total=Label(labelframeleft,font=("arial",12,"bold"),text="Sub Total:",padx=2,pady=6)
        lblsub_total.grid(row=8,column=0,sticky=W)

        txtsub_total=Entry(labelframeleft,textvariable=self.var_subtotal,font=("arial",13,"bold"),width=29,state="readonly")
        txtsub_total.grid(row=8,column=1)

        # -------------------Total Cost-------------------

        lbltotal_cost=Label(labelframeleft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
        lbltotal_cost.grid(row=9,column=0,sticky=W)

        txttotal_cost=Entry(labelframeleft,textvariable=self.var_total,font=("arial",13,"bold"),width=29,state="readonly")
        txttotal_cost.grid(row=9,column=1)

        #===============Bill Button==================

        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="darkgreen",width=10,cursor="hand2")
        btnBill.grid(row=10,column=0,padx=1,sticky=W)

        #===============Print Button=================

        btnPrint=Button(labelframeleft,text="Print Bill",font=("arial",11,"bold"),bg="black",fg="darkgreen",width=10,cursor="hand2")
        btnPrint.grid(row=10,column=1,padx=1,sticky=W)

        #===============Send Button==================

        btnSend=Button(labelframeleft,text="Send Bill",command=self.send,font=("arial",11,"bold"),bg="black",fg="darkgreen",width=10,cursor="hand2")
        btnSend.place(x=295,y=350)

        # =================btns=====================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="orange",fg="black",width=10,cursor="hand2")
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="green",fg="gold",width=10,cursor="hand2")
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",11,"bold"),bg="red",fg="white",width=10,cursor="hand2")
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10,cursor="hand2")
        btnReset.grid(row=0,column=3,padx=1)

        # ==================Right Side Image======================

        img3=Image.open(r"enter your path    \hotel_management\hotel images\room1.jpg")# enter path of your file
        img3=img3.resize((500,300),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lbling=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lbling.place(x=790,y=55,width=500,height=200)

        # ===============Table frame search system================

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2,)
        Table_Frame.place(x=435,y=280,width=860,height=260)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12),width=24,state="readonly")
        # Add a placeholder value to the Combobox
        combo_Search.set("Select Search Option")
        combo_Search["value"]=("Contact","RoomNo","RoomType")
        
        # Function to handle Combobox selection changes
        def on_search_option_select(event):
            selected_search_type = combo_Search.get()
            if selected_search_type == "Select Search Option":
                # Handle placeholder selection
                combo_Search.delete(0, END)  # Clear the entry
            else:
                # Handle actual search option selection
                combo_Search.delete(0, END)  # Clear the entry
                combo_Search.insert(0, selected_search_type)  # Insert the selected search option

        # Bind the function to the Combobox selection event
        combo_Search.bind("<<ComboboxSelected>>", on_search_option_select)

        # Place the Combobox on the grid
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",11,"bold"),bg="darkblue",fg="pink",width=10,cursor="hand2")
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="darkblue",fg="pink",width=10,cursor="hand2")
        btnShowAll.grid(row=0,column=4,padx=1)

        # ===========Show Data Table=================

        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL,cursor="hand2")
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL,cursor="hand2")

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomNo","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check_out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomNo",text="Room No")
        self.room_table.heading("meal",text="Meal")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomNo",width=100)
        self.room_table.column("meal",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)

        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    # -------------------Add Data-------------------
        
    def add_data(self):
        if self.var_contact.get()=="" or self.var_contact.get()=="Enter Customer Contact" or self.var_checkin.get()=="" or self.var_checkin.get()=="Select Check-in Date" or self.var_checkout.get()=="" or self.var_checkout.get()=="Select Check-out Date" or self.var_roomtype.get()=="" or self.var_roomtype.get()=="Select Room Type" or self.var_roomNo.get()=="" or self.var_roomNo.get()=="Select Room No" or self.var_meal.get()=="" or self.var_meal.get()=="Select Meal":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_contact.get(),
                                                                                    self.var_checkin.get(),
                                                                                    self.var_checkout.get(),
                                                                                    self.var_roomtype.get(),
                                                                                    self.var_roomNo.get(),
                                                                                    self.var_meal.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room has been Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

        self.var_contact.set("Enter Customer Contact")
        self.var_checkin.set("Select Check-in Date")
        self.var_checkout.set("Select Check-out Date")
        self.var_roomtype.set("Select Room Type")
        self.var_roomNo.set("Select Room No")
        self.var_meal.set("Select Meal")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_subtotal.set("")
        self.var_total.set("")

    # -------------------Fetch Data-------------------

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # -------------------Get Cursor-------------------
        
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomNo.set(row[4])
        self.var_meal.set(row[5])

    # -------------------Update Data-------------------
        
    def update(self):
        if self.var_contact.get()=="" or self.var_contact.get()=="Enter Customer Contact" or self.var_checkin.get()=="" or self.var_checkin.get()=="Select Check-in Date" or self.var_checkout.get()=="" or self.var_checkout.get()=="Select Check-out Date" or self.var_roomtype.get()=="" or self.var_roomtype.get()=="Select Room Type" or self.var_roomNo.get()=="" or self.var_roomNo.get()=="Select Room No" or self.var_meal.get()=="" or self.var_meal.get()=="Select Meal":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("Update room set check_in=%s,check_out=%s,roomtype=%s,Contact=%s,meal=%s where roomNo=%s",(

                                                                                                                                        self.var_checkin.get(),
                                                                                                                                        self.var_checkout.get(),
                                                                                                                                        self.var_roomtype.get(),
                                                                                                                                        self.var_contact.get(),
                                                                                                                                        self.var_meal.get(),
                                                                                                                                        self.var_roomNo.get()
                                            
                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details has been updated Successfully",parent=self.root)
        
        self.var_contact.set("Enter Customer Contact")
        self.var_checkin.set("Select Check-in Date")
        self.var_checkout.set("Select Check-out Date")
        self.var_roomtype.set("Select Room Type")
        self.var_roomNo.set("Select Room No")
        self.var_meal.set("Select Meal")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_subtotal.set("")
        self.var_total.set("")

    # -------------------Delete Data-------------------
            
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this Room",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
            my_cursor=conn.cursor()
            query="delete from room where roomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete","Customer Details has been deleted Successfully",parent=self.root)

        self.var_contact.set("Enter Customer Contact")
        self.var_checkin.set("Select Check-in Date")
        self.var_checkout.set("Select Check-out Date")
        self.var_roomtype.set("Select Room Type")
        self.var_roomNo.set("Select Room No")
        self.var_meal.set("Select Meal")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_subtotal.set("")
        self.var_total.set("")

    # -------------------Reset Data-------------------
        
    def reset(self):
        self.var_contact.set("Enter Customer Contact")
        self.var_checkin.set("Select Check-in Date")
        self.var_checkout.set("Select Check-out Date")
        self.var_roomtype.set("Select Room Type")
        self.var_roomNo.set("Select Room No")
        self.var_meal.set("Select Meal")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_subtotal.set("")
        self.var_total.set("")

    # ===================All Data Fetch=====================

    def Fetch_contact(self):
        if self.var_contact.get()=="" or self.var_contact.get()=="Enter Customer Contact":
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number is not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=430,y=55,width=358,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                # =============Gender=================

                conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                # =============Email=================

                conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)

                # =============Nationality=================

                conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblnationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblnationality.place(x=0,y=90)

                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)

                # =============Address=================

                conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lbladdress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lbladdress.place(x=0,y=120)

                lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)

    # ============Search System===========================
                
    def search(self):
        if self.search_var.get()=="Select Search option":
            messagebox.showerror("Error","Please select search option",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
            my_cursor=conn.cursor()

            my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    self.room_table.insert("",END,values=i)
                conn.commit()
            conn.close()

    
    # ======================Bill===========================
                
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days+1)

        if (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Laxary"):
            q1=float(300)
            q2=float(800)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Laxary"):
            q1=float(500)
            q2=float(800)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(500)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(500)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Laxary"):
            q1=float(800)
            q2=float(800)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(800)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(800)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="All" and self.var_roomtype.get()=="Laxary"):
            q1=float(1600)
            q2=float(800)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="All" and self.var_roomtype.get()=="Single"):
            q1=float(1600)
            q2=float(600)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="All" and self.var_roomtype.get()=="Double"):
            q1=float(1600)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.var_paidtax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

    # ========================Send Bill====================

    def send(self):
        # Send bill to the user's email
        try:
            # Connect to the database
            conn = mysql.connector.connect(host="localhost", username="root", password="enter your database password", database="management")
            my_cursor = conn.cursor()

            # Fetch customer's email from the database
            query = "SELECT Email FROM customer WHERE Mobile = %s"  # Assuming you have a CustomerID to identify the customer
            customer_id = self.var_contact.get()  # Update with the actual customer ID or fetch it from your application
            my_cursor.execute(query, (customer_id,))
            row = my_cursor.fetchone()

            if row:
                customer_email = row[0]  # Extract the email from the fetched row
                # Set up the SMTP server
                smtp_server = " enter your smtp  server name "  # Update with your SMTP server details
                port = 587  # Update with your SMTP server port (587 is commonly used for TLS)
                sender_email = "  enter your  email address"  # Update with your email address
                sender_password = "enter your  password "  # Update with your email password

                # Create a secure SSL context
                smtp = smtplib.SMTP(smtp_server, port)
                smtp.starttls()
                smtp.login(sender_email, sender_password)

                # Construct the message
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = customer_email  # Use the customer's email
                msg['Subject'] = "Your Bill Details"

                # Compose the message body
                message = f"""
                Dear Customer,

                Here are your bill details:

                
                Sub Total: {self.var_subtotal.get()}
                Paid Tax: {self.var_paidtax.get()}
                Total Cost: {self.var_total.get()}

                Thank you for choosing our hotel!

                Regards,
                Hotel Management Team
                """

                msg.attach(MIMEText(message, 'plain'))

                # Attach the image to the email
                image_path = r'enter your path    \hotel_management\Qr.jpg'  # Update with the correct path to your image file  # enter path of your file
                with open(image_path, 'rb') as img:
                    img_data = img.read()
                    image = MIMEImage(img_data, name=os.path.basename(image_path))
                    msg.attach(image)

                # Send the email
                smtp.send_message(msg)
                smtp.quit()

                messagebox.showinfo("Email Sent", "Bill details sent to customer's email successfully.",parent=self.root)
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

    # =====================Calendar============================

    def open_checkin_calendar(self):
        self.calendar_window = Toplevel(self.root)
        self.calendar_window.title("Check-in Date")

        # Set the geometry of the calendar window to position it at (x, y)
        x = 386  # Specify the x-coordinate
        y = 393  # Specify the y-coordinate
        self.calendar_window.geometry(f"+{x}+{y}")

        cal = Calendar(self.calendar_window, selectmode='day', year=2024, month=4, day=1)
        cal.pack()

        btn_ok = Button(self.calendar_window, text="OK", command=lambda: self.set_checkin_date(cal.get_date()))
        btn_ok.pack()

    def set_checkin_date(self, date):
        # Convert the string to datetime format
        date1 = datetime.strptime(date, "%m/%d/%y")
        formatted_date = date1.strftime("%d/%m/%Y")
        current_contact = self.var_contact.get()  # Get the current contact value
        self.var_checkin.set(formatted_date)
        self.calendar_window.destroy()
        self.var_contact.set(current_contact)  # Restore the contact field value

    def open_checkout_calendar(self):
        self.calendar_window = Toplevel(self.root)
        self.calendar_window.title("Check-out Date")

        # Set the geometry of the calendar window to position it at (x, y)
        x = 386  # Specify the x-coordinate
        y = 427  # Specify the y-coordinate
        self.calendar_window.geometry(f"+{x}+{y}")

        cal = Calendar(self.calendar_window, selectmode='day', year=2024, month=4, day=1)
        cal.pack()

        btn_ok = Button(self.calendar_window, text="OK", command=lambda: self.set_checkout_date(cal.get_date()))
        btn_ok.pack()

    def set_checkout_date(self, date):
        # Convert the string to datetime format
        date1 = datetime.strptime(date, "%m/%d/%y")
        formatted_date = date1.strftime("%d/%m/%Y")
        current_contact = self.var_contact.get()  # Get the current contact value
        self.var_checkout.set(formatted_date)
        self.calendar_window.destroy()
        self.var_contact.set(current_contact)  # Restore the contact field value


        

if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()