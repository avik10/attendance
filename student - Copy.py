from time import strftime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from PIL import Image, ImageTk
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Student Details')


#       ============Varriables ========
        self.var_class = StringVar()
        self.var_year = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_sec = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_address = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_guardian = StringVar()
        self.var_radio1 = StringVar()


# first iamge
        img1 = Image.open('./img/header_img1.jpg')
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=500, height=130)
# second image

        img2 = Image.open('./img/header_img2.png')
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500, y=0, width=500, height=130)
# Third image

        img3 = Image.open('./img/header_img3.jpg')
        img3 = img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=500, height=130)
# background image

        img4 = Image.open('./img/face_detector1.jpg')
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_lbl = Label(self.root, image=self.photoimg4)
        bg_lbl.place(x=0, y=130, width=1530, height=710)
# heading
        title_lbl = Label(bg_lbl, text="Student Management", font=(
            "times new roman", 30, 'bold'), bg='white', fg='red')
        title_lbl.place(x=0, y=0, width=1530, height=45)
        def time():
                string = strftime("%H:%M:%S %p")
                lbl.config(text = string)
                lbl.after(1000,time)

        lbl = Label(bg_lbl, font=("times new roman",26,'bold'),bg='white', fg='BLUE')
        lbl.place(x=1200,y=0,width=230,height=45)
        time()

# Main Frame
        main_frame = Frame(bg_lbl, bd=2)
        main_frame.place(x=10, y=55, width=1330, height=500)

# Left Frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, 'bold'))
        left_frame.place(x=10, y=10, width=650, height=480)

        left_img = Image.open('./img/student.jpg')
        left_img = left_img.resize((635, 50), Image.ANTIALIAS)
        self.left_img = ImageTk.PhotoImage(left_img)

        f_lbl = Label(left_frame, image=self.left_img)
        f_lbl.place(x=5, y=0, width=635, height=50)

# current course
        current_course_frame = LabelFrame(
            left_frame, bd=2, relief=RIDGE, text="Current Course", font=("times new roman", 12, 'bold'))
        current_course_frame.place(x=5, y=55, width=635, height=70)

# class(Deparment)
        cls_label = Label(current_course_frame, text="Class",
                          font=("times new roman", 12))
        cls_label.grid(row=0, column=0, padx=5)

        cls_combo = ttk.Combobox(current_course_frame, textvariable=self.var_class, font=(
            "times new roman", 12), state="readonly")
        cls_combo["values"] = ("Please Select", '1', '2', '3')
        cls_combo.current(0)
        cls_combo.grid(row=0, column=1, padx=5)

# Year
        yr_label = Label(current_course_frame, text="Year",
                         font=("times new roman", 12))
        yr_label.grid(row=0, column=2, padx=5, pady=5)

        yr_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 12), state="readonly")
        yr_combo["values"] = ("Please Select", '2018',
                              '2019', '2020', '2021', '2022')
        yr_combo.current(0)
        yr_combo.grid(row=0, column=3, padx=5, pady=5)

# Class Student info
        class_student_frame = LabelFrame(
            left_frame, bd=2, relief=RIDGE, text="Class Student Information", font=("times new roman", 12, 'bold'))
        class_student_frame.place(x=5, y=135, width=635, height=220)

# Student Id
        std_id_label = Label(class_student_frame, text="# ID",
                             font=("times new roman", 12))
        std_id_label.grid(row=0, column=0, padx=5)

        std_id_inp = Entry(class_student_frame,  textvariable=self.var_id, justify=CENTER, font=(
            "times new roman", 12, 'bold'), width=22, bd=2)
        std_id_inp.grid(row=0, column=1, padx=5, sticky=W)

# Student name
        std_name_label = Label(class_student_frame,
                               text="Name", font=("times new roman", 12))
        std_name_label.grid(row=0, column=2, padx=5)

        std_name_inp = Entry(class_student_frame,  textvariable=self.var_name, justify=CENTER, font=(
            "times new roman", 12, 'bold'), width=22, bd=2)
        std_name_inp.grid(row=0, column=3, padx=5, sticky=W)

# Section
        std_sec_label = Label(class_student_frame,
                              text="Section", font=("times new roman", 12))
        std_sec_label.grid(row=1, column=0, padx=5)

        std_sec_inp = ttk.Combobox(class_student_frame, textvariable=self.var_sec, font=(
            "times new roman", 12), state="readonly")
        std_sec_inp["values"] = ("Please Select", 'A', 'B', 'C')
        std_sec_inp.current(0)
        std_sec_inp.grid(row=1, column=1, padx=5, pady=5)

# Roll
        std_roll_label = Label(class_student_frame,
                               text="Roll", font=("times new roman", 12))
        std_roll_label.grid(row=1, column=2, padx=5, pady=5)

        std_roll_inp = Entry(class_student_frame, textvariable=self.var_roll, justify=CENTER, font=(
            "times new roman", 12, 'bold'), width=22, bd=2)
        std_roll_inp.grid(row=1, column=3, padx=5, pady=5)

# Gender
        std_gender_label = Label(
            class_student_frame, text="Gender", font=("times new roman", 12))
        std_gender_label.grid(row=2, column=0, padx=5, pady=5)

        std_gender_inp = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 12), state="readonly")
        std_gender_inp["values"] = (
            "Please Select", 'Male', 'Female', 'Others')
        std_gender_inp.current(0)
        std_gender_inp.grid(row=2, column=1, padx=5, pady=5)

# Address
        std_address_label = Label(
            class_student_frame, text="Address", font=("times new roman", 12))
        std_address_label.grid(row=2, column=2, padx=5, pady=5)

        std_address_inp = Entry(class_student_frame, textvariable=self.var_address, justify=CENTER, font=(
            "times new roman", 12, 'bold'), width=22, bd=2)
        std_address_inp.grid(row=2, column=3, padx=5, pady=5)

# dob
        std_dob_label = Label(class_student_frame,
                              text="DOB", font=("times new roman", 12))
        std_dob_label.grid(row=3, column=0, padx=5, pady=5)

        std_dob_inp = Entry(class_student_frame, textvariable=self.var_dob, justify=CENTER, font=(
            "times new roman", 12, 'bold'), width=22, bd=2)
        # std_dob_inp.insert(0,'DD/MM/YYYY')
        std_dob_inp.grid(row=3, column=1, padx=5, pady=5)

# Email
        std_email_label = Label(class_student_frame,
                                text="Email", font=("times new roman", 12))
        std_email_label.grid(row=3, column=2, padx=5, pady=5)

        std_email_inp = Entry(class_student_frame,  textvariable=self.var_email, justify=CENTER, font=(
            "times new roman", 12, 'bold'), width=22, bd=2)
        # std_email_inp.insert(0,'abc@example.com')
        std_email_inp.grid(row=3, column=3, padx=5, pady=5)

# phone
        std_phone_label = Label(class_student_frame,
                                text="Phone No", font=("times new roman", 12))
        std_phone_label.grid(row=4, column=0, padx=5, pady=5)

        std_phone_inp = Entry(class_student_frame, textvariable=self.var_phone, justify=CENTER, font=(
            "times new roman", 12, 'bold'), width=22, bd=2)
        std_phone_inp.grid(row=4, column=1, padx=5, pady=5)

# Guardian Name
        std_guardian_label = Label(
            class_student_frame, text="Guardian Name", font=("times new roman", 12))
        std_guardian_label.grid(row=4, column=2, padx=5, pady=5)

        std_guardian_inp = Entry(class_student_frame,  textvariable=self.var_guardian, justify=CENTER, font=(
            "times new roman", 12, 'bold'), width=22, bd=2)
        std_guardian_inp.grid(row=4, column=3, padx=5, pady=5)

# Radio  Buttons

        radionbtn1 = ttk.Radiobutton(
            class_student_frame,  variable=self.var_radio1, text="Take Sample Image", value='Yes')
        radionbtn1.grid(row=5, column=1, pady=5)

        radionbtn2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="No Sample Image", value='No')
        radionbtn2.grid(row=5, column=3, padx=5, pady=5)

# Buttons
        button_frame = Frame(left_frame, bd=2, relief=RIDGE)
        button_frame.place(x=5, y=360, width=635, height=90)

        take_photo_btn = Button(button_frame, text="Take Photo", width=30, font=(
            "times new roman", 12, 'bold'), bg="black", fg='white', command=self.generate_dataset)
        take_photo_btn.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

        upload_photo_btn = Button(button_frame, text="Upload Photo", width=30, font=(
            "times new roman", 12, 'bold'), bg="green")
        upload_photo_btn.grid(row=0, column=2, padx=5, pady=5, columnspan=2)

        save_btn = Button(button_frame, text="Save", command=self.add_data, width=10, font=(
            "times new roman", 12, 'bold'), bg="cyan")
        save_btn.grid(row=1, column=0, padx=5, pady=5)

        update_btn = Button(button_frame, text="Update", width=10, font=(
            "times new roman", 12, 'bold'), bg="yellow", command=self.update_data)
        update_btn.grid(row=1, column=1, padx=5, pady=5)

        delete_btn = Button(button_frame, text="Delete", width=10, font=(
            "times new roman", 12, 'bold'), bg="red", command=self.delete_data)
        delete_btn.grid(row=1, column=2, padx=5, pady=5)

        reset_btn = Button(button_frame, text="Reset", width=10, font=(
            "times new roman", 12, 'bold'), bg="grey", command=self.reset_data)
        reset_btn.grid(row=1, column=3, padx=5, pady=5)

# Right Frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, 'bold'))
        right_frame.place(x=680, y=10, width=640, height=480)

        right_img = Image.open('./img/clg.jpg')
        right_img = right_img.resize((630, 50), Image.ANTIALIAS)
        self.right_img = ImageTk.PhotoImage(right_img)

        f_lbl = Label(right_frame, image=self.right_img)
        f_lbl.place(x=5, y=0, width=630, height=50)

# Search Frame

        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, 'bold'))
        search_frame.place(x=5, y=55, width=630, height=70)

        search_label = Label(search_frame, text="Seacrh By",
                             font=("times new roman", 12, 'bold'))
        search_label.grid(row=0, column=0, padx=5, pady=5)

        search_combo = ttk.Combobox(search_frame, font=(
            "times new roman", 12,), state="readonly", width=18)
        search_combo["values"] = ("Please Select", 'Roll No', 'Phone No')
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5)

        search_inp = Entry(search_frame, width=15, justify=CENTER, font=(
            "times new roman", 12, 'bold'), bd=2)
        search_inp.grid(row=0, column=2, padx=5, pady=5)

        search_btn = Button(search_frame, text="Search", width=10, font=(
            "times new roman", 12, 'bold'), bg="blue")
        search_btn.grid(row=0, column=3, padx=5, pady=5)

        show_all_btn = Button(search_frame, text="Show All", width=10, font=(
            "times new roman", 12, 'bold'), bg="white", fg='black')
        show_all_btn.grid(row=0, column=4, padx=5, pady=5)

# Table Frame
        table_frame =LabelFrame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=140, width=630, height=310)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=(
            'ID', 'Name', 'Class', 'Section', 'Roll', 'Gender', 'Year', 'Address', 'DOB', 'Email', 'Phone', 'Guardian', 'Photo'))

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('ID', text='ID')
        self.student_table.heading('Name', text='Name')
        self.student_table.heading('Class', text='Class')
        self.student_table.heading('Section', text='Section')
        self.student_table.heading('Roll', text='Roll')
        self.student_table.heading('Gender', text='Gender')
        self.student_table.heading('Year', text='Year')
        self.student_table.heading('Address', text='Address')
        self.student_table.heading('DOB', text='DOB')
        self.student_table.heading('Email', text='Email')
        self.student_table.heading('Phone', text='Phone No')
        self.student_table.heading('Guardian', text='Guardian Name')
        self.student_table.heading('Photo', text='Photo Status')
        self.student_table['show'] = "headings"

        self.student_table.column('ID', width=20)
        self.student_table.column('Name', width=150)
        self.student_table.column('Class', width=50)
        self.student_table.column('Section', width=50)
        self.student_table.column('Roll', width=50)
        self.student_table.column('Gender', width=80)
        self.student_table.column('Year', width=80)
        self.student_table.column('Address', width=100)
        self.student_table.column('DOB', width=100)
        self.student_table.column('Email', width=120)
        self.student_table.column('Phone', width=120)
        self.student_table.column('Guardian', width=100)
        self.student_table.column('Photo', width=40)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind('<ButtonRelease>', self.get_cursor)
        self.fetch_data()

# ================= Functions ===============
    def add_data(self):
        if self.var_id.get().lower() == '':
            messagebox.showerror('Error', 'ID Required..!!')
        elif self.var_name.get().lower() == '':
            messagebox.showerror('Error', 'Name Required..!!')
        elif self.var_sec.get().lower() == 'please select':
            messagebox.showerror('Error', 'Section Required..!!')
        elif self.var_roll.get() == '':
            messagebox.showerror('Error', 'Roll Required..!!')
        elif self.var_gender.get() == 'please select':
            messagebox.showerror('Error', 'Gender Required..!!')
        elif self.var_name.get() == '':
            messagebox.showerror('Error', 'Name Required..!!')
        elif self.var_gender.get() == '':
            messagebox.showerror('Error', 'Gender Required..!!')
        elif self.var_address.get() == '':
            messagebox.showerror('Error', 'Address Required..!!')
        elif self.var_dob.get() == '':
            messagebox.showerror('Error', 'DOB Required..!!')
        elif self.var_email.get() == '':
            messagebox.showerror('Error', 'Email Required..!!')
        elif self.var_phone.get() == '':
            messagebox.showerror('Error', 'Phone Required..!!')
        elif self.var_guardian.get() == '':
            messagebox.showerror('Error', 'Guardian Required..!!')
        elif self.var_year.get().lower() == 'please select':
            messagebox.showerror('Error', 'Please Select Year..!!')
        elif self.var_class.get().lower() == 'please select':
            messagebox.showerror('Error', 'Please Select Class..!!')
        else:
            try:
                conn = mysql.connector.connect(
                    host='localhost', username='root', password='root', database='face_recognition_system')
                my_cursor = conn.cursor()
                my_cursor.execute('insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_class.get(),
                    self.var_sec.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_year.get(),
                    self.var_address.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_guardian.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    'Success', 'Student Detils Add Successfully')
            except Exception as e:
                messagebox.showerror(
                    'Error', f'Due to : {str(e)}', parent=self.root)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
                host='localhost', user='root', password='root', database='face_recognition_system')
            my_cursor = conn.cursor()
            my_cursor.execute('select * from student')
            data = my_cursor.fetchall()

            if not(len(data) == 0):
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert('', END, values=i)
                conn.commit()
            conn.close()
        except EXCEPTION as e:
            messagebox.showerror('Error', f'Due to {str(e)}', parent=self.root)

    def get_cursor(self, event=''):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content['values']
        print(data)
        self.var_id.set(data[0]),
        self.var_name.set(data[1]),
        self.var_class.set(data[2]),
        self.var_sec.set(data[3]),
        self.var_roll.set(data[4]),
        self.var_gender.set(data[5]),
        self.var_year.set(data[6]),
        self.var_address.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_guardian.set(data[11]),
        self.var_radio1.set(data[12])

    def update_data(self):
        if self.var_id.get() == '':
            messagebox.showerror('Error', 'ID is required')
        else:
            try:
                update = messagebox.askyesno(
                    'Update', 'Do you want to update this student data', parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host='localhost', user='root', password='root', database='face_recognition_system')
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        'update student set name=%s, class=%s, sec=%s, roll =%s,gender=%s, year=%s, address=%s, dob=%s, email=%s, phone=%s,guardian=%s,photo=%s where student_id = %s', (self.var_name.get(),
                                                                                                                                                                         self.var_class.get(),
                                                                                                                                                                         self.var_sec.get(),
                                                                                                                                                                         self.var_roll.get(),
                                                                                                                                                                         self.var_gender.get(),
                                                                                                                                                                         self.var_year.get(),
                                                                                                                                                                         self.var_address.get(),
                                                                                                                                                                         self.var_dob.get(),
                                                                                                                                                                         self.var_email.get(),
                                                                                                                                                                         self.var_phone.get(),
                                                                                                                                                                         self.var_guardian.get(),
                                                                                                                                                                         self.var_radio1.get(),
                                                                                                                                                                         self.var_id.get()
                                                                                                                                                                         ))
                else:
                    if not update:
                        return
                messagebox.showinfo('Success','Student details update successfully..!!',parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror('Error', f'Due to: {str(e)}', parent = self.root)

    def delete_data(self):
        if self.var_id.get() == '':
            messagebox.showerror('error','Student ID Must be required')
        else:
            try:
                delete = messagebox.askyesno('Delete', 'Do you want to delete this student..??')
                if delete > 0 :
                    conn = mysql.connector.connect(host='localhost', user='root', password='root', database='face_recognition_system')
                    my_cursor = conn.cursor()
                    sql = "delete from student where student_id=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql,val)

                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Student details Delete successfully..!!',parent=self.root)
            except Exception as e:
                messagebox.showerror('Error', f'Due to: {str(e)}', parent = self.root)

    def reset_data(self):

        self.var_id.set(''),
        self.var_name.set(''),
        self.var_class.set('Please Select'),
        self.var_sec.set('Please Select'),
        self.var_roll.set(''),
        self.var_gender.set('Please Select'),
        self.var_year.set('Please Select'),
        self.var_address.set(''),
        self.var_dob.set(''),
        self.var_email.set(''),
        self.var_phone.set(''),
        self.var_guardian.set(''),
        self.var_radio1.set('')


# =============== generate data set or take sample photo ============

    def generate_dataset(self):

        if self.var_id.get() == '':
                messagebox.showerror('error','Student ID Must be required')
        # elif self.var_name.get() == '':
        #         messagebox.showerror('error','Student Name Must be required')
        # elif self.var_class.get().lower() == 'please select':
        #          messagebox.showerror('error','Student Class Must be required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='root', database='face_recognition_system')
                my_cursor = conn.cursor()
                my_cursor.execute('select * from student')
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1
                my_cursor.execute('update student set name=%s, class=%s, sec=%s, roll =%s,gender=%s, year=%s, address=%s, dob=%s, email=%s, phone=%s,guardian=%s,photo=%s where student_id = %s', (self.var_name.get(),
                                                                                                                                                                        self.var_class.get(),
                                                                                                                                                                        self.var_sec.get(),
                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                        self.var_guardian.get(),
                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                        self.var_id.get() == id+1
                                                                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ==load face frontal harcascade opencv==

                face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.2, 5)  #scale factor, minimum neighour

                    for (x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, frame = cap.read()
                    if face_cropped(frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(frame), (450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = 'data/user.' + str(id) +'.'+ str(img_id) +'.jpg'
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255), 2)
                        cv2.imshow('Cropped Face', face)

                    if cv2.waitKey(1)==13 or img_id == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo('Success', 'Data Capture Successful..!!')
            except Exception as e:
                messagebox.showerror('Error', f'Due to: {str(e)}', parent = self.root)
                print(f'Due to: {str(e)}')

if __name__ == '__main__':
    root = Tk()
    obj = Student(root)
    root.mainloop()
