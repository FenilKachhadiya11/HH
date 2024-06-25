from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1293x560+230+220")

        # ===============title=====================

        lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="lightgrey",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # =================logo====================

        img2=Image.open(r"enter your path    \hotel_management\hotel images\llogo.webp") #enter path of your file

        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lbling=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=40)

        # ====================lableFrame=====================

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=540,height=350)

        # ===================Floor============================.

        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W,padx=20)

        # Validate function to check if input is valid
        validate_floor = self.root.register(self.validate_floor)

        # Entry widget for customer contact with a default placeholder text
        placeholder_text = "Enter Floor No."
        self.var_floor=StringVar()
        self.var_floor.set(placeholder_text)
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("arial",13),width=20, validate="key", validatecommand=(validate_floor, '%P'))
        entry_floor.grid(row=0,column=1,sticky=W)
        
        # Function to handle the placeholder text and user input
        def on_entry_click(event):
            if self.var_floor.get() == placeholder_text:
                entry_floor.delete(0, END)  # Clear the placeholder text
                entry_floor.config(foreground='black')  # Change text color to black

        # Bind the function to the entry widget
        entry_floor.bind('<FocusIn>', on_entry_click)

        # Function to handle the case when focus is lost without input
        def on_entry_focusout(event):
            if not self.var_floor.get():
                entry_floor.insert(0, placeholder_text)  # Restore placeholder text
                entry_floor.config(foreground='gray')  # Change text color to gray

        # Bind the function to handle focus out event
        entry_floor.bind('<FocusOut>', on_entry_focusout)

        # =========================Room No==================================

        lbl_RoomNo=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W,padx=20)

        # Validate function to check if input is valid
        validate_room_no = self.root.register(self.validate_room_no)

        # Entry widget for customer contact with a default placeholder text
        placeholder_text1 = "Enter Room No."
        self.var_roomNo=StringVar()
        self.var_roomNo.set(placeholder_text1)
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,font=("arial",13),width=20, validate="key", validatecommand=(validate_room_no, '%P'))
        entry_RoomNo.grid(row=1,column=1,sticky=W)

        # Function to handle the placeholder text and user input
        def on_entry_click(event):
            if self.var_roomNo.get() == placeholder_text1:
                entry_RoomNo.delete(0, END)  # Clear the placeholder text
                entry_RoomNo.config(foreground='black')  # Change text color to black

        # Bind the function to the entry widget
        entry_RoomNo.bind('<FocusIn>', on_entry_click)

        # Function to handle the case when focus is lost without input
        def on_entry_focusout(event):
            if not self.var_roomNo.get():
                entry_RoomNo.insert(0, placeholder_text1)  # Restore placeholder text
                entry_RoomNo.config(foreground='gray')  # Change text color to gray

        # Bind the function to handle focus out event
        entry_RoomNo.bind('<FocusOut>', on_entry_focusout)

        # ========================Room Type====================================

        lbl_RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W,padx=20)

        self.var_roomType=StringVar()
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomType,font=("arial",13),width=18,state="readonly")
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
        combo_RoomType.grid(row=2,column=1)

        # =================btns=====================

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="orange",fg="black",width=10,cursor="hand2")
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="green",fg="gold",width=10,cursor="hand2")
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",11,"bold"),bg="red",fg="white",width=10,cursor="hand2")
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=10,cursor="hand2")
        btnReset.grid(row=0,column=3,padx=1)

        # ===============Table frame of Room Details================

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=600,y=55,width=600,height=350)

        scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL,cursor="hand2")
        scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL,cursor="hand2")

        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomNo","roomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomNo",text="Room No")
        self.room_table.heading("roomType",text="Room Type")

        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomNo",width=100)
        self.room_table.column("roomType",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    # -------------------Check Room-------------------

    def check_room_exists(self, room_number):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="enter your database password", database="management"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT COUNT(*) FROM details WHERE roomNo = %s", (room_number,))
        count = my_cursor.fetchone()[0]
        conn.close()
        return count > 0

    # -------------------Add Details-------------------
        
    def add_data(self):
        if self.var_floor.get()=="" or self.var_floor.get()=="Enter Floor No." or self.var_roomNo.get()=="" or self.var_roomNo.get()=="Enter Room No." or self.var_roomType.get()=="" or self.var_roomType.get()=="Select Room Type":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
                my_cursor=conn.cursor()

                # Check if the room number already exists in the 'details' table
                my_cursor.execute("SELECT COUNT(*) FROM details WHERE roomNo = %s", (self.var_roomNo.get(),))
                count = my_cursor.fetchone()[0]

                if count > 0:
                    messagebox.showerror("Error", "Room number already exists", parent=self.root)
                else:
                    # Insert the new room details if it doesn't already exist
                    my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                            self.var_floor.get(),
                                                                            self.var_roomNo.get(),
                                                                            self.var_roomType.get()
                                                                        ))
                    conn.commit()
                    self.fetch_data()
                    messagebox.showinfo("Success","New Room has been Added Successfully",parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)
        self.var_floor.set("Enter Floor No.")
        self.var_roomNo.set("Enter Room No.")
        self.var_roomType.set("Select Room Type")

    # -------------------Fetch Data-------------------

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
        my_cursor=conn.cursor()
        # Fetch all room numbers from the 'room' table
        my_cursor.execute("SELECT roomNo FROM room")
        room_numbers = [row[0] for row in my_cursor.fetchall()]

        # Fetch details excluding rooms present in the 'room' table
        my_cursor.execute("SELECT * FROM details WHERE roomNo NOT IN ({})".format(','.join(['%s'] * len(room_numbers))), room_numbers)
        rows = my_cursor.fetchall()
        #my_cursor.execute("select * from details")
        #rows=my_cursor.fetchall()
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

        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_roomType.set(row[2])

    # -------------------Update Data-------------------
        
    def update(self):
        if self.var_floor.get()=="" or self.var_floor.get()=="Enter Floor No." or self.var_roomNo.get()=="" or self.var_roomNo.get()=="Enter Room No." or self.var_roomType.get()=="" or self.var_roomType.get()=="Select Room Type":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("Update details set Floor=%s,RoomType=%s where RoomNo=%s",(

                                                                                        self.var_floor.get(),
                                                                                        self.var_roomType.get(),
                                                                                        self.var_roomNo.get()
                                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room Details has been updated Successfully",parent=self.root)
        self.var_floor.set("Enter Floor No.")
        self.var_roomNo.set("Enter Room No.")
        self.var_roomType.set("Select Room Type")

    # -------------------Delete Data-------------------
            
    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this Room Details",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="enter your database password",database="management")
            my_cursor=conn.cursor()
            query="delete from details where RoomNo=%s"
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete","Room Details has been deleted Successfully",parent=self.root)
        self.var_floor.set("Enter Floor No.")
        self.var_roomNo.set("Enter Room No.")
        self.var_roomType.set("Select Room Type")

    # -------------------Reset Data-------------------
        
    def reset(self):
        self.var_floor.set("Enter Floor No.")
        self.var_roomNo.set("Enter Room No.")
        self.var_roomType.set("Select Room Type")

    # =========================Condition Check for Floor No==================

    def validate_floor(self, new_value):
        # Check if the new value is empty
        if not new_value:
            return True
        
        if new_value == "Enter Floor No.":
            return True

        # Check if the new value contains non-digit characters
        if not new_value.isdigit():
            messagebox.showerror("Error", "Please enter only numbers in floor number.",parent=self.root)
            return False
        
        return True

    # =========================Condition Check for Room No==================

    def validate_room_no(self, new_value):
        # Check if the new value is empty
        if not new_value:
            return True
        
        if new_value == "Enter Room No.":
            return True

        # Check if the new value contains non-digit characters
        if not new_value.isdigit():
            messagebox.showerror("Error", "Please enter only numbers in room no.",parent=self.root)
            return False

        # Check if the length is more than 4 digits
        if len(new_value) > 4:
            messagebox.showerror("Error", "Please enter 4 digit in room no.",parent=self.root)
            return False

        return True


if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()