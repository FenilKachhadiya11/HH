from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1293x560+230+220")


        # ==============variables================

        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_father=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()

        # ===============title=====================

        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="lightgrey",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # =================logo====================

        img2=Image.open(r"enter path    \hotel_management\hotel images\llogo.webp")  # enter path of your file
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)

        # ====================lableFrame=====================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("arial",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        # ====================lables and entry==============

        # -------------------custRef-------------------

        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("arial",13,"bold"),width=29,state="readonly")
        entry_ref.grid(row=0,column=1)

        # -------------------cust name-------------------

        cname=Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)

        # Validate function to check if input is valid
        validate_cust_name = self.root.register(self.validate_cust_name)

        # Entry for customer name
        self.var_cust_name = StringVar()

        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial",13),width=29, validate="key", validatecommand=(validate_cust_name, '%P'))
        txtcname.grid(row=1,column=1)

        def on_enter(e):
            txtcname.delete(0,"end")

        def on_leave(e):
            name=txtcname.get()
            if name=="":
                txtcname.insert(0,"Enter Customer name")

        txtcname.insert(0,"Enter Customer name")
        txtcname.bind("<FocusIn>",on_enter)
        txtcname.bind("<FocusOut>",on_leave)

        #Frame(labelframeleft,width=264,height=2,bg="black").place(x=138,y=67)

        # -------------------Father name-------------------

        lblmname=Label(labelframeleft,font=("arial",12,"bold"),text="Father Name:",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)

        txtfname=Entry(labelframeleft,textvariable=self.var_father,font=("arial",13),width=29)
        txtfname.grid(row=2,column=1)
        
        def on_enter(e):
            txtfname.delete(0,"end")

        def on_leave(e):
            name=txtfname.get()
            if name=="":
                txtfname.insert(0,"Enter Customer's Father name")

        txtfname.insert(0,"Enter Customer's Father name")
        txtfname.bind("<FocusIn>",on_enter)
        txtfname.bind("<FocusOut>",on_leave)

        # -------------------gender combobox-------------------

        label_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender:",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12),width=27,state="readonly")
        combo_gender["value"]=("Enter Gender","Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        # -------------------postcode-------------------

        lblpostcode=Label(labelframeleft,font=("arial",12,"bold"),text="PostCode:",padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)
        
        # Validate function to check if input is valid
        validate_postcode = self.root.register(self.validate_postcode)

        # Entry for customer postcode
        self.var_post = StringVar()
        txtpostcode=Entry(labelframeleft,textvariable=self.var_post,font=("arial",13),width=29, validate="key", validatecommand=(validate_postcode, '%P'))
        txtpostcode.grid(row=4,column=1)

        def on_enter(e):
            txtpostcode.delete(0,"end")

        def on_leave(e):
            name=txtpostcode.get()
            if name=="":
                txtpostcode.insert(0,"Enter Postcode")

        txtpostcode.insert(0,"Enter Postcode")
        txtpostcode.bind("<FocusIn>",on_enter)
        txtpostcode.bind("<FocusOut>",on_leave)

        # -------------------mobilenumber-------------------
        lblMobile=Label(labelframeleft,font=("arial",12,"bold"),text="Mobile:",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)

        # Validate function to check if input is valid
        validate_mobilenumber = self.root.register(self.validate_mobilenumber)

        # Entry for customer contact
        self.var_contact = StringVar()
        txtMobile=Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",13),width=29, validate="key", validatecommand=(validate_mobilenumber, '%P'))
        txtMobile.grid(row=5,column=1)

        def on_enter(e):
            txtMobile.delete(0,"end")

        def on_leave(e):
            name=txtMobile.get()
            if name=="":
                txtMobile.insert(0,"Enter Mobile number")

        txtMobile.insert(0,"Enter Mobile number")
        txtMobile.bind("<FocusIn>",on_enter)
        txtMobile.bind("<FocusOut>",on_leave)

        # -------------------email-------------------

        lblEmail=Label(labelframeleft,font=("arial",12,"bold"),text="Email:",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)

        txtEmail=Entry(labelframeleft,textvariable=self.var_email,font=("arial",13),width=29)
        txtEmail.grid(row=6,column=1)

        def on_enter(e):
            txtEmail.delete(0,"end")

        def on_leave(e):
            name=txtEmail.get()
            if name=="":
                txtEmail.insert(0,"Enter Email")

        txtEmail.insert(0,"Enter Email")
        txtEmail.bind("<FocusIn>",on_enter)
        txtEmail.bind("<FocusOut>",on_leave)

        # -------------------nationality-------------------

        lblNationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality:",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12),width=27,state="readonly")
        combo_Nationality["value"]=("Enter Customer's Nationality","Indian","American","Britist")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)

        # -------------------idproof type combobox-------------------

        lblIdProof=Label(labelframeleft,font=("arial",12,"bold"),text="Id Proof Type:",padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12),width=27,state="readonly")
        combo_id["value"]=("Enter Id Proof Type","AadharCard","DrivingLicence","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        # -------------------id number-------------------

        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Id Number:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)

        txtIdNumber=Entry(labelframeleft,textvariable=self.var_id_number,font=("arial",13),width=29)
        txtIdNumber.grid(row=9,column=1)

        def on_enter(e):
            txtIdNumber.delete(0,"end")

        def on_leave(e):
            name=txtIdNumber.get()
            if name=="":
                txtIdNumber.insert(0,"Enter Id number")

        txtIdNumber.insert(0,"Enter Id number")
        txtIdNumber.bind("<FocusIn>",on_enter)
        txtIdNumber.bind("<FocusOut>",on_leave)

        # -------------------address-------------------

        lblAddress=Label(labelframeleft,font=("arial",12,"bold"),text="Address:",padx=2,pady=6)
        lblAddress.grid(row=10,column=0,sticky=W)

        txtAddress=Entry(labelframeleft,textvariable=self.var_address,font=("arial",13),width=29)
        txtAddress.grid(row=10,column=1)

        def on_enter(e):
            txtAddress.delete(0,"end")

        def on_leave(e):
            name=txtAddress.get()
            if name=="":
                txtAddress.insert(0,"Enter Address")

        txtAddress.insert(0,"Enter Address")
        txtAddress.bind("<FocusIn>",on_enter)
        txtAddress.bind("<FocusOut>",on_leave)

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

        # ===============Table frame search system================

        Table_Frame=LabelFrame(root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2,)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12),width=24,state="readonly")
        # Add a placeholder value to the Combobox
        combo_Search.set("Select Search Option")
        combo_Search["value"]=("Ref","Name")

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
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL,cursor="hand2")
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL,cursor="hand2")

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","father","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("father",text="Father Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("father",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    # -------------------Add Data-------------------

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mobile.get()=="Enter Mobile number" or self.var_father.get()=="" or self.var_father.get()=="Enter Customer's Father name" or self.var_cust_name.get()=="" or self.var_cust_name.get()=="Enter Customer name" or self.var_gender.get()=="" or self.var_gender.get()=="Enter Gender" or self.var_post.get()=="" or self.var_post.get()=="Enter Postcode" or self.var_email.get()=="" or self.var_email.get()=="Enter Email" or self.var_id_number.get()=="" or self.var_id_number.get()=="Enter Id number" or self.var_address.get()=="" or self.var_address.get()=="Enter Address" or self.var_id_proof.get()=="" or self.var_id_proof.get()=="Enter Id Proof Type" or self.var_nationality.get()=="" or self.var_nationality.get()=="Enter Customer's Nationality":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="  enter your database password",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.var_ref.get(),
                                                                                    self.var_cust_name.get(),
                                                                                    self.var_father.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_post.get(),
                                                                                    self.var_mobile.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_nationality.get(),
                                                                                    self.var_id_proof.get(),
                                                                                    self.var_id_number.get(),
                                                                                    self.var_address.get()
                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
        
        self.var_cust_name.set("Enter Customer name"),
        self.var_father.set("Enter Customer's Father name"),
        self.var_gender.set("Enter Gender"),
        self.var_post.set("Enter Postcode"),
        self.var_mobile.set("Enter Mobile number"),
        self.var_email.set("Enter Email"),
        self.var_nationality.set("Enter Customer's Nationality"),
        self.var_id_proof.set("Enter Id Proof Type"),
        self.var_id_number.set("Enter Id number"),
        self.var_address.set("Enter Address")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    # -------------------Fetch Data-------------------

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="  enter your database password",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # -------------------Get Cursor-------------------

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_father.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    # -------------------Update Data-------------------

    def update(self):
        if self.var_mobile.get()=="" or self.var_mobile.get()=="Enter Mobile number" or self.var_father.get()=="" or self.var_father.get()=="Enter Customer's Father name" or self.var_cust_name.get()=="" or self.var_cust_name.get()=="Enter Customer name" or self.var_gender.get()=="" or self.var_gender.get()=="Enter Gender" or self.var_post.get()=="" or self.var_post.get()=="Enter Postcode" or self.var_email.get()=="" or self.var_email.get()=="Enter Email" or self.var_id_number.get()=="" or self.var_id_number.get()=="Enter Id number" or self.var_address.get()=="" or self.var_address.get()=="Enter Address" or self.var_id_proof.get()=="" or self.var_id_proof.get()=="Enter Id Proof Type" or self.var_nationality.get()=="" or self.var_nationality.get()=="Enter Customer's Nationality":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="  enter your database password",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("Update Customer set Name=%s,father=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,idproof=%s,idnumber=%s,Address=%s where Ref=%s",(

                                                                                                                                                                        self.var_cust_name.get(),
                                                                                                                                                                        self.var_father.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_post.get(),
                                                                                                                                                                        self.var_mobile.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_nationality.get(),
                                                                                                                                                                        self.var_id_proof.get(),
                                                                                                                                                                        self.var_id_number.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_ref.get()
                                                                                                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details has been updated Successfully",parent=self.root)

        self.var_cust_name.set("Enter Customer name"),
        self.var_father.set("Enter Customer's Father name"),
        self.var_gender.set("Enter Gender"),
        self.var_post.set("Enter Postcode"),
        self.var_mobile.set("Enter Mobile number"),
        self.var_email.set("Enter Email"),
        self.var_nationality.set("Enter Customer's Nationality"),
        self.var_id_proof.set("Enter Id Proof Type"),
        self.var_id_number.set("Enter Id number"),
        self.var_address.set("Enter Address")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    # -------------------Delete Data-------------------

    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this customer",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="  enter your database password",database="management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete","Customer Details has been deleted Successfully",parent=self.root)

        self.var_cust_name.set("Enter Customer name"),
        self.var_father.set("Enter Customer's Father name"),
        self.var_gender.set("Enter Gender"),
        self.var_post.set("Enter Postcode"),
        self.var_mobile.set("Enter Mobile number"),
        self.var_email.set("Enter Email"),
        self.var_nationality.set("Enter Customer's Nationality"),
        self.var_id_proof.set("Enter Id Proof Type"),
        self.var_id_number.set("Enter Id number"),
        self.var_address.set("Enter Address")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
    
    # -------------------Reset Data-------------------

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set("Enter Customer name"),
        self.var_father.set("Enter Customer's Father name"),
        self.var_gender.set("Enter Gender"),
        self.var_post.set("Enter Postcode"),
        self.var_mobile.set("Enter Mobile number"),
        self.var_email.set("Enter Email"),
        self.var_nationality.set("Enter Customer's Nationality"),
        self.var_id_proof.set("Enter Id Proof Type"),
        self.var_id_number.set("Enter Id number"),
        self.var_address.set("Enter Address")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    # ============Search System=====================

    def search(self):
        if self.search_var.get()=="Select Search Option":
            messagebox.showerror("Error","Please Select Search Option",parent=self.root)

        elif self.txt_search.get()=="":
            messagebox.showerror("Error","Please Enter the value to search the result",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="  enter your database password",database="management")
            my_cursor=conn.cursor()

            my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
            rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # =========================Condition Check for Mobile Number==================

    def validate_mobilenumber(self, new_value):
        # Check if the new value is empty
        if not new_value:
            return True
        
        if new_value == "Enter Mobile number":
            return True

        # Check if the new value contains non-digit characters
        if not new_value.isdigit():
            messagebox.showerror("Error", "Please enter only numbers in mobile number.",parent=self.root)
            return False

        # Check if the length is more than 10 digits
        if len(new_value) > 10:
            messagebox.showerror("Error", "Please enter up to 10 digits in mobile number.",parent=self.root)
            return False

        return True

    #def fetch_data(self):
        # Your fetch data logic goes here
        pass

    # =========================Condition Check for PostCode==================

    def validate_postcode(self, new_value):
        # Check if the new value is empty
        if not new_value:
            return True
        
        if new_value == "Enter Postcode":
            return True

        # Check if the new value contains non-digit characters
        if not new_value.isdigit():
            messagebox.showerror("Error", "Please enter only numbers in postcode.",parent=self.root)
            return False

        # Check if the length is more than 6 digits
        if len(new_value) > 6:
            messagebox.showerror("Error", "Please enter up to 6 digits in postcode.",parent=self.root)
            return False

        return True

    #def fetch_data(self):
        # Your fetch data logic goes here
        pass

    # =================Condition Check for Customer Name=====================

    def validate_cust_name(self, new_value):
        # Check if the new value is empty
        if not new_value:
            return True
        
        if new_value == "Enter Customer name":
            return True

        # Check if the new value contains digit characters
        if any(char.isdigit() for char in new_value):
            messagebox.showerror("Error", "Please enter only characters in Customer name.",parent=self.root)
            return False

        return True


if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()
