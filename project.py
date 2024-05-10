from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk #pip install pillow

import mysql.connector
from tkinter import messagebox



class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")
    
        #variable
        self.var_branch = StringVar()
        self.var_department=StringVar()
        self.var_year=StringVar()
        self.var_course=StringVar()
        self.var_semester=StringVar()
        self.var_student_id=StringVar()
        self.var_student_name=StringVar()
        self.var_gender=StringVar()
        self.var_date_of_birth=StringVar()
        self.var_branch_section=StringVar()
        self.var_phone_number=StringVar()
        self.var_address=StringVar()
        self.var_e_mail=StringVar()
        
        #label tittle 
        lbl_tittle=Label(self.root,text="Student Management System",font=("times new roman",40,"bold"),bg="black",fg="white")
        lbl_tittle.place(x=5,y=5,width=1525,height=70)
        
        #main frame
        main_frame=Frame(self.root,bd=5,bg="white",relief=RIDGE)
        main_frame.place(x=5,y=85,width=1525,height=690)        
        
        
        #left frame
        data_left=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"),fg="black")
        data_left.place(x=5,y=0,widt=350,height=670)
        
        #current course information in left frame
        cc_left=LabelFrame(data_left,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",14,"bold"),fg="black")
        cc_left.place(x=5,y=0,width=330,height=210)
        
        # branch details label
        lbl_branch=Label(cc_left,text="Branch:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl_branch.grid(row=0,column=0,padx=10,sticky=W)
        combo_branch=ttk.Combobox(cc_left,textvariable=self.var_branch,font=("times new roman",13,"bold"),state="readonly",width=17)    
        combo_branch["values"]=("Select Branch","Computer","IT","Civil","Mechanical","Electrical","Electronics","Chemical","BioTechnology","Production")
        combo_branch.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        combo_branch.current(0)
        
        #department details label
        lbl_dept=Label(cc_left,text="Department",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl_dept.grid(row=1,column=0,padx=10,sticky=W)
        combo_dept=ttk.Combobox(cc_left,textvariable=self.var_department,font=("times new roman",13,"bold"),state="readonly",width=17)
        combo_dept["values"]=("Select Department","Computer","IT","Civil","Mechanical","Electrical","Electronics","Chemical","BioTechnology","Production")
        combo_dept.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        combo_dept.current(0)
        
        #year details label
        lbl_year=Label(cc_left,text="Year:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl_year.grid(row=2,column=0,padx=10,sticky=W)
        combo_year=ttk.Combobox(cc_left,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=17)
        combo_year["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        combo_year.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        combo_year.current(0)
        
        #sem details label
        lbl_sem=Label(cc_left,text="Semester:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl_sem.grid(row=3,column=0,padx=10,sticky=W)
        combo_sem=ttk.Combobox(cc_left,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=17)
        combo_sem["values"]=("Select Semester","1","2","3","4","5","6","7","8")
        combo_sem.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        combo_sem.current(0)
        
        #course details label
        lbl_course=Label(cc_left,text="Course:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl_course.grid(row=4,column=0,padx=10,sticky=W)
        combo_course=ttk.Combobox(cc_left,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=17)
        combo_course["values"]=("Select Course","FE","SE","TE","BE")
        combo_course.grid(row=4,column=1,padx=5,pady=5,sticky=W)
        combo_course.current(0)
        
        
        #student information in left frame
        si_left=LabelFrame(data_left,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",14,"bold"),fg="black")
        si_left.place(x=5,y=210,width=330,height=310)

        lbl_name=Label(si_left,text="Name:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl_name.grid(row=0,column=0,padx=10,sticky=W)
        txt_name=ttk.Entry(si_left,textvariable=self.var_student_name,width=20,font=("times new roman",13,"bold"))
        txt_name.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        #student id label
        lbl_stuid=Label(si_left,text="Student ID:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl_stuid.grid(row=1,column=0,padx=10,sticky=W)
        txt_stuid=ttk.Entry(si_left,width=20,font=("times new roman",13,"bold"))
        txt_stuid.grid(row=1,column=1,padx=5,pady=5,sticky=W)
         
        #genders
        lbl_gender=Label(si_left,text="Gender:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl_gender.grid(row=2,column=0,padx=10,sticky=W)
        combo_gender=ttk.Combobox(si_left,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        combo_gender["values"]=("select gender ","Male","Female","transgender")
        combo_gender.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        combo_gender.current(0)
        
        #dob
        lbl_dob=Label(si_left,text="Date of Birth:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl_dob.grid(row=3,column=0,padx=10,sticky=W)
        txt_dob=ttk.Entry(si_left,textvariable=self.var_date_of_birth,width=20,font=("times new roman",13,"bold"))
        txt_dob.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        
        #section
        lbl_section=Label(si_left,text="Section:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl_section.grid(row=4,column=0,padx=10,sticky=W)
        combo_section=ttk.Combobox(si_left,textvariable=self.var_branch_section,font=("times new roman",13,"bold"),state="readonly",width=18)
        combo_section["values"]=("select section ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
        combo_section.grid(row=4,column=1,padx=5,pady=5,sticky=W)
        
        #phone_no.
        lbl_phone=Label(si_left,text="Phone No:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl_phone.grid(row=5,column=0,padx=10,sticky=W)
        txt_phone=ttk.Entry(si_left,textvariable=self.var_phone_number,width=20,font=("times new roman",13,"bold"))
        txt_phone.grid(row=5,column=1,padx=5,pady=5,sticky=W)
        
        #address
        lbl_address=Label(si_left,text="Address:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl_address.grid(row=6,column=0,padx=10,sticky=W)
        txt_address=ttk.Entry(si_left,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        txt_address.grid(row=6,column=1,padx=5,pady=5,sticky=W)
        
        #email address
        lbl_email=Label(si_left,text="Email:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl_email.grid(row=7,column=0,padx=10,sticky=W)
        txt_email=ttk.Entry(si_left,textvariable=self.var_e_mail,width=20,font=("times new roman",13,"bold"))
        txt_email.grid(row=7,column=1,padx=5,pady=5,sticky=W)
        
        
        #button box
        btn_box=LabelFrame(data_left,bd=2,bg="white",relief=RIDGE,text="ButtonBox",font=("times new roman",14,"bold"),fg="black")
        btn_box.place(x=5,y=525,width=330,height=115)
        
        #add button
        btn_add=Button(btn_box,text="Add",command=self.add_var,font=("times new roman",13,"bold"),fg="white",bg="black",width=13)
        btn_add.grid(row=0,column=0,padx=12,pady=5,sticky=W)
        
        #update button
        btn_update=Button(btn_box,text="Update",command=self.update_data,font=("times new roman",13,"bold"),fg="white",bg="black",width=13)
        btn_update.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        #delete button
        btn_delete=Button(btn_box,text="Delete",command=self.delete_data,font=("times new roman",13,"bold"),fg="white",bg="black",width=13)
        btn_delete.grid(row=1,column=0,padx=12,pady=5,sticky=W)
        
        #reset buttons
        btn_reset=Button(btn_box,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),fg="white",bg="black",width=13)
        btn_reset.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        
        #right frame above
        data_right=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Data",font=("times new roman",15,"bold"),fg="black")
        data_right.place(x=365,y=0,width=1145,height=668)
        
        #search frame
        search_frame=LabelFrame(data_right,bd=2,bg="white",relief=RIDGE,text="Search Student Information",font=("times new roman",14,"bold"),fg="black")
        search_frame.place(x=5,y=0,width=1000,height=70)
        
        #search label
        lbl_search=Label(search_frame,text="Search:",font=("times new roman",13,"bold"),bg="white",fg="black")
        lbl_search.grid(row=0,column=0,padx=10,sticky=W)
        
        self.var_com_search=StringVar()
        txt_search=ttk.Combobox(search_frame,text="Search:",textvariable=self.var_com_search,font=("times new roman",13),width=19)
        txt_search["values"]=("select option","Name","Student ID","Gender","Date of Birth","Branch","Phone No","Address","Email","Phone Number","Address",)
        txt_search.current(0)
        txt_search.grid(row=0,column=1,padx=10,pady=0,sticky=W)
        
        #search entry
        self.var_search=StringVar()
        txt_search_entry=ttk.Entry(search_frame,textvariable=self.var_search,width=20,font=("times new roman",13,"bold"))
        txt_search_entry.grid(row=0,column=2,padx=10,pady=0,sticky=W)
        
        #search button
        btn_search=Button(search_frame,text="Search",command=self.search_data,font=("times new roman",13,"bold"),fg="white",bg="black",width=13)
        btn_search.grid(row=0,column=3,padx=10,pady=0,sticky=W)
        
        #show all results button
        btn_show_all=Button(search_frame,command=self.fetch_data,text="Show All",font=("times new roman",13,"bold"),fg="white",bg="black",width=13)
        btn_show_all.grid(row=0,column=4,padx=10,pady=0,sticky=W)
        
        #show selected results button
        btn_show_selected=Button(search_frame,text="Show Selected",font=("times new roman",13,"bold"),fg="white",bg="black",width=13)
        btn_show_selected.grid(row=0,column=5,padx=10,pady=0,sticky=W)
        
        #========================student table========================
        #student table
        student_table =Frame(data_right,bd=2,relief=RIDGE,bg="white")
        student_table.place(x=5,y=80,width=1130,height=550)
        
        #scroll bars
        scroll_x = Scrollbar(student_table,orient=HORIZONTAL)
        scroll_y = Scrollbar(student_table,orient=VERTICAL)
        
        #table
        self.table = ttk.Treeview(student_table,columns=("BRANCH","DEPARTMENT","YEAR","COURSE","SEMESTER","STUDENT-ID","STUDENT-NAME","GENEDER","DATE-OF-BIRTH","BRANCH-SECTION","PHONE-NUMBER","ADDRESS","E-MAIL"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

        #scroll bars
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)
        #show columns
        self.table.heading("BRANCH",text="BRANCH") 
        self.table.heading("DEPARTMENT",text="DEPARTMENT")
        self.table.heading("YEAR",text="YEAR")
        self.table.heading("COURSE",text="COURSE")
        self.table.heading("SEMESTER",text="SEMESTER")
        self.table.heading("STUDENT-ID",text="STUDENT-ID")
        self.table.heading("STUDENT-NAME",text="STUDENT-NAME")
        self.table.heading("GENEDER",text="GENEDER")
        self.table.heading("DATE-OF-BIRTH",text="DATE-OF-BIRTH")
        self.table.heading("BRANCH-SECTION",text="BRANCH-SECTION")
        self.table.heading("PHONE-NUMBER",text="PHONE-NUMBER")
        self.table.heading("ADDRESS",text="ADDRESS")
        self.table.heading("E-MAIL",text="E-MAIL")
        #for set the width of the column
        self.table["show"]="headings"
        self.table.column("BRANCH",width=150)
        self.table.column("DEPARTMENT",width=150)
        self.table.column("YEAR",width=150)
        self.table.column("COURSE",width=150)
        self.table.column("SEMESTER",width=150)
        self.table.column("STUDENT-ID",width=150)
        self.table.column("STUDENT-NAME",width=150)
        self.table.column("GENEDER",width=150)
        self.table.column("DATE-OF-BIRTH",width=150)
        self.table.column("BRANCH-SECTION",width=150)
        self.table.column("PHONE-NUMBER",width=150)
        self.table.column("ADDRESS",width=150)
        self.table.column("E-MAIL",width=150)
        
        self.table.pack(fill=BOTH,expand=1)
        self.table.bind("<ButtonRelease>",self.get_cursor)       
        """self.fetch_data()"""#for show data in table by connecting my sql
        
        
                
    def add_var(self):
        if (self.var_date_of_birth.get()=="" or self.var_phone_number.get()=="" or self.var_address.get()=="" or self.var_e_mail.get()==""):
            messagebox.showerror("Error","Please fill all the fields")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Mayank12@",database="datasystem")
                my_cursur=conn.cursor()
                my_cursur.execute=("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_branch.get(),self.var_department.get(),self.var_year.get(),self.var_course.get(),self.var_semester.get(),self.var_student_id.get(),self.var_student_name.get(),self.var_gender.get(),self.var_date_of_birth.get(),self.var_branch_section.get(),self.var_phone_number.get(),self.var_address.get(),self.var_e_mail.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data inserted successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)
                
    #fetch function
    def fetch_data(self):
        conn=mysql.connector.connect(host="locals.host",username="root",password="Mayank12@",database="datasystem")
        my_cursur=conn.cursor()
        my_cursur.execute=("select * from student")
        data=my_cursur.fetchall()
        if len(data)!=0:
            self.table.delete(*self.table.get_children())
            for row in data:
                self.table.insert("",END,values=row)
                
            conn.commit()
            conn.close()
        
    #getcursor()
    def get_cursor(self,event=""): 
        cursor_row = self.table.focus()
        content=self.table.items(cursor_row)
        data=content["values"]
        
        self.var_branch.set(data[0])
        self.var_department.set(data[1])
        self.var_year.set(data[2])
        self.var_course.set(data[3])
        self.var_semester.set(data[4])
        self.var_student_id.set(data[5])
        self.var_student_name.set(data[6])
        self.var_gender.set(data[7])
        self.var_date_of_birth.set(data[8])
        self.var_branch_section.set(data[9])
        self.var_phone_number.set(data[10])
        self.var_address.set(data[11])
        self.var_e_mail.set(data[12])
        
    #update the data
    def update_data(self):
        if (self.var_date_of_birth.get()=="" or self.var_phone_number.get()=="" or self.var_address.get()=="" or self.var_e_mail.get()==""):
            messagebox.showerror("Error","Please fill all the fields")
        else:
            try:
                update=messagebox.askyesno("update","Are you sure you want to update this data",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Mayank12@",database="datasystem")
                    my_cursur=conn.cursor()
                    my_cursur.execute=("update student set branch=%s,department=%s,year=%s,course=%s,semester=%s,student_id=%s,student_name=%s,gender=%s,date_of_birth=%s,branch_section=%s,phone_number=%s,address=%s,e_mail=%s where student_id=%s",(self.var_branch.get(),self.var_department,self.var_year,self.var_course,self.var_semester,self.var_student_name,self.var_gender,self.var_date_of_birth,self.var_branch_section,self.phone_number,self.address,self.e_mail,self.var_student_id))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data updated successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)
                            
                            
    #delete the data
    def delete_data(self):
        if self.var_student_id.get()=="":
            messagebox.showerror("Error","Please select the row")
        else:
            try:
                delete=messagebox.askyesno("delete","Are you sure you want to delete this data",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Mayank12@",database="datasystem")
                    my_cursur=conn.cursor()
                    my_cursur.execute=("delete from student where student_id=%s",(self.var_student_id.get()))
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Data deleted successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)
                
    #reset the data
    def reset_data(self):
        self.var_branch.set("select branch")
        self.var_department.set("select department")
        self.var_year.set("select year")
        self.var_course.set("select course")
        self.var_semester.set("select semester")
        self.var_student_id.set("")
        self.var_student_name.set("")
        self.var_gender.set("")
        self.var_date_of_birth.set("")
        self.var_branch_section.set("select branch section")
        self.var_phone_number.set("select phone number")
        self.var_address.set("")
        self.var_e_mail.set("")
        
    #search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Please fill all the fields")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Mayank12@",database="datasystem")
                my_cursur=conn.cursor()
                my_cursur.execute=("select * from student where %s=%s",(self.var_com_search.get(),self.var_search.get()))  
                #at this the command is used is this  "select * from student where "+str(self.var_search.get())+" LIKE '%"+str(self.var_search.get())+"'%"
                #(agar iss command ke use krne par error to where ke baad se space remove karke check kafr skte hai)
                data=my_cursur.fetchall()
                if len(data)!=0:
                    self.table.delete(*self.table.get_children())
                    for row in data:
                        self.table.insert("",END,values=row)
                        
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Data searched successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showerror("error",f"due to:{str(es)}",parent=self.root)
#for connecting database firsty know what is your username.
#1)for input the data from frontend change the exact username in add function
#2)for connect backend and frontend run the fetch function statement just above the all fuctions
#3)for all the functions running change the username
#step 1:done in add funtion
#step 2:done above the add function
#step 3:done below the get_cursor function    


# for making backend only make your scherme in student mode     
            
        
if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
