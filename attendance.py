from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognization System by Srishti and Bhushan")

        #=======================variables========================================
        self.var_atten_id=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_sem=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #first image
        img=Image.open(r"D:\minor\face detection attendence full\Face Recognition System\Images\attendance3.jpg")
        img=img.resize((900,250), Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0, y=0, width=900, height=250)


        #second image
        img1=Image.open(r"D:\minor\face detection attendence full\Face Recognition System\Images\attendance2.jpg")
        img1=img1.resize((1000,250), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=900, y=0, width=1000, height=250)

        #bg image
        img3=Image.open(r"D:\minor\face detection attendence full\Face Recognition System\Images\attbg.png")
        img3=img3.resize((1920,880), Image.ANTIALIAS) 
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0, y=250, width=1920, height=800)

        title_lbl=Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="light green")
        title_lbl.place(x=0, y=0, width=1920, height=40)

        main_frame=Frame(bg_img, bg="white", bd=2)
        main_frame.place(x=30, y=75, width=1850, height=640)

        #left label frame
        Left_frame=LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=20, y=10, width=850, height=600)

        img_left=Image.open(r"D:\minor\face detection attendence full\Face Recognition System\Images\attendance.jpg")
        img_left=img_left.resize((840,200), Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=840, height=200)

        left_inside_frame=Frame(Left_frame, bg="white", bd=2, relief=RIDGE)
        left_inside_frame.place(x=10, y=230, width=820, height=350)

        #=====================labels and entry==================================
 
        #attendance id
        attendanceID_label=Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 13, "bold"), bg="white")
        attendanceID_label.grid(row=0, column=0, padx=10, pady=5, sticky=W) 

        attendanceID_entry=ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_id, font=("times new roman", 13, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W) 

        #Sem

        sem_label=Label(left_inside_frame, text="Semester:", font=("times new roman", 13, "bold"), bg="white")
        sem_label.grid(row=0, column=2, padx=4, pady=8) 

        self.sem_atten=ttk.Combobox(left_inside_frame, font=("times new roman", 12, "bold"), state="read only", width=20, textvariable=self.var_atten_sem)
        self.sem_atten["values"]=("", "Odd", "Even")
        self.sem_atten.current(0)
        self.sem_atten.grid(row=0, column=3, pady=8)


        #Student Name
        name_label=Label(left_inside_frame, text="Name:", font=("times new roman", 13, "bold"), bg="white")
        name_label.grid(row=1, column=0) 

        atten_name=ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_name, font=("times new roman", 13, "bold"))
        atten_name.grid(row=1, column=1, padx=8) 

        #Dep
        dep_label=Label(left_inside_frame, text="Department:", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=1, column=2) 

        atten_dep=ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_dep, font=("times new roman", 13, "bold"))
        atten_dep.grid(row=1, column=3, pady=8) 

        #Time
        time_label=Label(left_inside_frame, text="Time:", font=("times new roman", 13, "bold"), bg="white")
        time_label.grid(row=2, column=0) 

        atten_time=ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_time, font=("times new roman", 13, "bold"))
        atten_time.grid(row=2, column=1, pady=8) 

        #Date
        date_label=Label(left_inside_frame, text="Date:", font=("times new roman", 13, "bold"), bg="white")
        date_label.grid(row=2, column=2) 

        atten_date=ttk.Entry(left_inside_frame, width=20, textvariable=self.var_atten_date, font=("times new roman", 13, "bold"))
        atten_date.grid(row=2, column=3, pady=3) 

        #attendance
        attendance_label=Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 13, "bold"), bg="white")
        attendance_label.grid(row=3, column=0) 

        self.atten_status=ttk.Combobox(left_inside_frame, width=20, textvariable=self.var_atten_attendance, font=("times new roman", 13, "bold"), state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        #buttons frame
        btn_frame=Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=830, height=40)

        import_btn=Button(btn_frame, text="Import csv", width=20, command=self.importCsv, font=("times new roman", 13, "bold"), bg="light green", fg="white")
        import_btn.grid(row=0, column=0)

        export_btn=Button(btn_frame, text="Export csv", width=19, command=self.exportCsv, font=("times new roman", 13, "bold"), bg="light green", fg="white")
        export_btn.grid(row=0, column=1)

        update_btn=Button(btn_frame, text="Update", width=19, font=("times new roman", 13, "bold"), bg="light green", fg="white")
        update_btn.grid(row=0, column=2)

        reset_btn=Button(btn_frame, text="Reset", width=20, command=self.reset_data, font=("times new roman", 13, "bold"), bg="light green", fg="white")
        reset_btn.grid(row=0, column=3)

 
        #right label frame
        Right_frame=LabelFrame(main_frame, bg="white", bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=900, y=10, width=920, height=600) 

        table_frame=Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=5, width=890, height=550)

        #==========================scroll bar table=========================
        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame, column=("ID", "SName", "Sem", "Dep", "Time", "Date", "Attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID", text="Attendance ID")
        self.AttendanceReportTable.heading("SName", text="Student")
        self.AttendanceReportTable.heading("Sem", text="Semester")
        self.AttendanceReportTable.heading("Dep", text="Department")
        self.AttendanceReportTable.heading("Time", text="Time")
        self.AttendanceReportTable.heading("Date", text="Date")
        self.AttendanceReportTable.heading("Attendance", text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("ID", width=130)
        self.AttendanceReportTable.column("SName", width=130)
        self.AttendanceReportTable.column("Sem", width=130)
        self.AttendanceReportTable.column("Dep", width=130)
        self.AttendanceReportTable.column("Time", width=130)
        self.AttendanceReportTable.column("Date", width=130)
        self.AttendanceReportTable.column("Attendance", width=130)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    #==============================fetch data==================================

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)


    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data", "No data found to export.", parent=self.root)
                return False
            fln=filedialog.asksaveasfile(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("ALL File" "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write=csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data has been exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_sem.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_name.set("")
        self.var_atten_sem.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
    
  

if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()