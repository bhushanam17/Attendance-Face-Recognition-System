from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System by Srishti and Bhushan")


        #==========variables=================================
        self.var_dep=StringVar()
        self.var_year=StringVar()
        self.var_batch=StringVar()
        self.var_sem=StringVar()
        self.var_sid=StringVar()
        self.var_sname=StringVar()
        self.var_sec=StringVar()
        self.var_gname=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()


        #first image
        img=Image.open(r"D:\minor\face detection attendence full\Face Recognition System\Images\student_img1.jpg")
        img=img.resize((500,130), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)


        #second image
        img1=Image.open(r"D:\minor\face detection attendence full\Face Recognition System\Images\MUJ.jpg")
        img1=img1.resize((500,130), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)


        #third image
        img2=Image.open(r"D:\minor\face detection attendence full\Face Recognition System\Images\student_img2.jpg")
        img2=img2.resize((500,130), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)


        #bg image
        img3=Image.open(r"D:\minor\face detection attendence full\Face Recognition System\Images\bgimg2.jpg")
        img3=img3.resize((1530,710), Image.ANTIALIAS) 
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        
        title_lbl=Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame=Frame(bg_img, bg="white", bd=2)
        main_frame.place(x=20, y=50, width=1480, height=600)

        #left label frame
        Left_frame=LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE, text="Student Information", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left=Image.open(r"D:\minor\face detection attendence full\Face Recognition System\Images\raisinghand.jpg")
        img_left=img_left.resize((720,130), Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        #current course
        current_course_frame=LabelFrame(Left_frame, bg="white", bd=2, relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=125)

        #department
        dep_label=Label(current_course_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W) 

        dep_combo=ttk.Combobox(current_course_frame, textvariable=self.var_dep ,font=("times new roman", 12, "bold"), state="read only", width=20)
        dep_combo["values"]=("Select Department", "CSE", "IT", "CCE", "ECE", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        #Year
        year_label=Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=0, column=2, padx=10, sticky=W) 

        year_combo=ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="read only", width=20)
        year_combo["values"]=("Select Year", "First Year", "Second Year", "Third Year", "Final Year")
        year_combo.current(0)
        year_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        #Batch
        batch_label=Label(current_course_frame, text="Batch", font=("times new roman", 13, "bold"), bg="white")
        batch_label.grid(row=1, column=0, padx=10, sticky=W) 

        batch_combo=ttk.Combobox(current_course_frame, textvariable=self.var_batch, font=("times new roman", 12, "bold"), state="read only", width=20)
        batch_combo["values"]=("Select Batch", "2020-2024", "2021-2025", "2022-2026", "2023-2027")
        batch_combo.current(0)
        batch_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        #Semester
        sem_label=Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=10, sticky=W) 

        sem_combo=ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=("times new roman", 12, "bold"), state="read only", width=20)
        sem_combo["values"]=("Select Semester", "Odd", "Even")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        #Class student information
        class_student_frame=LabelFrame(Left_frame, bg="white", bd=2, relief=RIDGE, text="Current Course Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=720, height=300)

        #studentID
        studentID_label=Label(class_student_frame, text="StudentID:", font=("times new roman", 13, "bold"), bg="white")
        studentID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W) 

        studentID_entry=ttk.Entry(class_student_frame, textvariable=self.var_sid, width=20, font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W) 

        #student name
        studentName_label=Label(class_student_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, pady=5, sticky=W) 

        studentName_entry=ttk.Entry(class_student_frame, textvariable=self.var_sname, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W) 

        #Section
        section_label=Label(class_student_frame, text="Section:", font=("times new roman", 13, "bold"), bg="white")
        section_label.grid(row=1, column=0, padx=10, pady=5, sticky=W) 

        section_combo=ttk.Combobox(class_student_frame, textvariable=self.var_sec, font=("times new roman", 12, "bold"), state="read only", width=20)
        section_combo["values"]=("A", "B", "C", "D", "E")
        section_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        #Guardian's Name
        guardian_label=Label(class_student_frame, text="Guardian Name:", font=("times new roman", 13, "bold"), bg="white")
        guardian_label.grid(row=1, column=2, padx=10, pady=5, sticky=W) 

        guardian_entry=ttk.Entry(class_student_frame, textvariable=self.var_gname, width=20, font=("times new roman", 13, "bold"))
        guardian_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W) 

        #Gender
        gender_label=Label(class_student_frame, text="Gender", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W) 

        gender_combo=ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 12, "bold"), state="read only", width=20)
        gender_combo["values"]=("Male", "Female", "Others")
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        #DOB
        dob_label=Label(class_student_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W) 

        dob_entry=ttk.Entry(class_student_frame, textvariable=self.var_dob, width=20, font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W) 

        #Email
        email_label=Label(class_student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W) 

        email_entry=ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W) 

        #Phone No.
        phone_label=Label(class_student_frame, text="Phone No:", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W) 

        phone_entry=ttk.Entry(class_student_frame, textvariable=self.var_phone, width=20, font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W) 


        #radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame, text= "Take photo sample", value="YES", variable=self.var_radio1)
        radiobtn1.grid(row=6, column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame, text= "No photo sample", value="NO", variable=self.var_radio1)
        radiobtn2.grid(row=6, column=1)


        #buttons frame
        btn_frame=Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=70)

        save_btn=Button(btn_frame, text="Save", command=self.add_data, width=18, font=("times new roman", 13, "bold"), bg="light blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn=Button(btn_frame, text="Update", command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="light blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn=Button(btn_frame, text="Delete", command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="light blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn=Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="light blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1=Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)

        take_photo_btn=Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample", width=36, font=("times new roman", 13, "bold"), bg="light blue", fg="white")
        take_photo_btn.grid(row=0, column=0)

        update_photo_btn=Button(btn_frame1, text="Update Photo Sample", width=36, font=("times new roman", 13, "bold"), bg="light blue", fg="white")
        update_photo_btn.grid(row=0, column=1)


        #right label frame
        Right_frame=LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580) 

        img_right=Image.open(r"D:\minor\face detection attendence full\Face Recognition System\Images\xyz.jpg")
        img_right=img_right.resize((720,130), Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        #============Search System==================================
        # =====================SEARCH SYSTEM=======================
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5,y=135,width=710,height=70)
        
        search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="orange")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="read only",width=15)
        search_combo["values"]=("Select","Roll No.","Phone no.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(Search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="lightblue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn=Button(Search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="lightblue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #===========Table Frame=====================================
        table_frame=Frame(Right_frame, bg="white", bd=2, relief=RIDGE)
        table_frame.place(x=5, y=210, width=710, height=350)

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame, column=("Dep", "Year", "Batch", "Sem", "SID", "SName", "Sec", "GName", "Gender", "DOB", "Email", "Phone", "Photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Batch", text="Batch")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("SID", text="StudentID")
        self.student_table.heading("SName", text="Student Name")
        self.student_table.heading("Sec", text="Section")
        self.student_table.heading("GName", text="Guardian Name")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone No.")
        self.student_table.heading("Photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("Dep", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Batch", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("SID", width=100)
        self.student_table.column("SName", width=100)
        self.student_table.column("Sec", width=100)
        self.student_table.column("GName", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Photo", width=100)
        self.student_table["show"]="headings"

        

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    #====================Function Declaration=======================

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_sname.get()=="" or self.var_sid.get()=="":
            messagebox.showerror("Error", "Please fill the required info.", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="bhushan@123", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                                                                    self.var_dep.get(), 
                                                                                                                    self.var_year.get(), 
                                                                                                                    self.var_batch.get(), 
                                                                                                                    self.var_sem.get(), 
                                                                                                                    self.var_sid.get(), 
                                                                                                                    self.var_sname.get(), 
                                                                                                                    self.var_sec.get(), 
                                                                                                                    self.var_gname.get(), 
                                                                                                                    self.var_gender.get(), 
                                                                                                                    self.var_dob.get(), 
                                                                                                                    self.var_email.get(), 
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_radio1.get()
                                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully.", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)


    #==============================Fetch Data==============================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="bhushan@123", database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()



    #==============================Get Cursor==================================
    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_year.set(data[1])
        self.var_batch.set(data[2])
        self.var_sem.set(data[3])
        self.var_sid.set(data[4])
        self.var_sname.set(data[5])
        self.var_sec.set(data[6])
        self.var_gname.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_radio1.set(data[12])


    #===================Update Fuction======================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_sname.get()=="" or self.var_sid.get()=="":
            messagebox.showerror("Error", "Please fill the required info.", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update", "Do you want to update the Student Details?", parent=self.root)
                if Update>0:
                        conn=mysql.connector.connect(host="localhost", username="root", password="bhushan@123", database="face_recognizer")
                        my_cursor=conn.cursor()
                        my_cursor.execute("Update Student Set Dep=%s, Year=%s, Batch=%s, Sem=%s, SName=%s, Sec=%s, GName=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Photo=%s where SID=%s",(

                                                                                                                                                            self.var_dep.get(), 
                                                                                                                                                            self.var_year.get(), 
                                                                                                                                                            self.var_batch.get(), 
                                                                                                                                                            self.var_sem.get(),  
                                                                                                                                                            self.var_sname.get(), 
                                                                                                                                                            self.var_sec.get(), 
                                                                                                                                                            self.var_gname.get(), 
                                                                                                                                                            self.var_gender.get(), 
                                                                                                                                                            self.var_dob.get(), 
                                                                                                                                                            self.var_email.get(), 
                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                            self.var_sid.get(),
                                                                                                                                                        ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student Details have been successfully updated.", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)


    #delete function
    def delete_data(self):
        if self.var_sid.get()=="":
            messagebox.showerror("Error", "Student ID must be rquired.", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page", "Do you want to delete this student's details?", parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="bhushan@123", database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where SID=%s"
                    val=(self.var_sid.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted respective student's details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)

    #reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_year.set("Select Year")
        self.var_batch.set("Select Batch")
        self.var_sem.set("Select Semester")
        self.var_sid.set("")
        self.var_sname.set("")
        self.var_sec.set("")
        self.var_gname.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")


    #=====================Generate Data Set or Take Photo Samples===================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_sname.get()=="" or self.var_sid.get()=="":
            messagebox.showerror("Error", "Please fill the required info.", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="bhushan@123", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update Student Set Dep=%s, Year=%s, Batch=%s, Sem=%s, SName=%s, Sec=%s, GName=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Photo=%s where SID=%s",(

                                                                                                                                                            self.var_dep.get(), 
                                                                                                                                                            self.var_year.get(), 
                                                                                                                                                            self.var_batch.get(), 
                                                                                                                                                            self.var_sem.get(),  
                                                                                                                                                            self.var_sname.get(), 
                                                                                                                                                            self.var_sec.get(), 
                                                                                                                                                            self.var_gname.get(), 
                                                                                                                                                            self.var_gender.get(), 
                                                                                                                                                            self.var_dob.get(), 
                                                                                                                                                            self.var_email.get(), 
                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                            self.var_sid.get()==id+1
                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #=====================Load predefined data on face frontals from OpenCV=================

                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray, 1.3, 5)
                    #scaling factor=1.3
                    #minimum neighbour=5

                    for (x, y, w, h) in faces:
                        face_cropped=img[y:y+h, x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame), (450, 450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) 
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data set completed successfully.")
            except Exception as es:
                messagebox.showerror("Error", f"Due to:{str(es)}", parent=self.root)





if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()