import tkinter
from time import strftime
from datetime import datetime
from face_recognition import Face_Recognition
from student import Student
from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
import os
from student import *
from train import *
from face_recognition import*
from attendance import *

class Face_Recognition_System:
    def __init__ (self, root):
        self.root  = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face_Recognition System')
# first iamge
        img1 = Image.open('./img/header_img1.jpg')
        img1 = img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0,y=0,width=500,height=130)
# second image

        img2 = Image.open('./img/header_img2.png')
        img2 = img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=500,y=0,width=500,height=130)
# Third image

        img3 = Image.open('./img/header_img3.jpg')
        img3 = img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000,y=0,width=500,height=130)

# background image

        img4 = Image.open('./img/face_detector1.jpg')
        img4 = img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_lbl = Label(self.root, image=self.photoimg4)
        bg_lbl.place(x=0,y=130,width=1530,height=710)

# heading
        title_lbl = Label(bg_lbl, text = "Face Recognition System Attendance", font=("times new roman",30,'bold'),bg='white', fg='red')
        title_lbl.place(x=0,y=0,width=1530,height=45)
        def time():
                string = strftime("%H:%M:%S %p")
                lbl.config(text = string)
                lbl.after(1000,time)

        lbl = Label(bg_lbl, font=("times new roman",26,'bold'),bg='white', fg='BLUE')
        lbl.place(x=1200,y=0,width=230,height=45)
        time()
# student button

  
        student_img = Image.open('./img/student.jpg')
        student_img = student_img.resize((120,120),Image.ANTIALIAS)
        self.student_img = ImageTk.PhotoImage(student_img)

        btn1 = Button(bg_lbl, image=self.student_img,command=self.student_details, cursor="hand2")
        btn1.place(x=200,y=100,width=120,height=120)

        btn1_1 = Button(bg_lbl, text='Student Details',cursor="hand2",command=self.student_details, font=("times new roman",12,'bold'),bg='darkblue', fg='white')
        btn1_1.place(x=200,y=220,width=120,height=30)


# Detect Face button

  
        detect_face_img = Image.open('./img/face_detector1.jpg')
        detect_face_img = detect_face_img.resize((120,120),Image.ANTIALIAS)
        self.detect_face_img = ImageTk.PhotoImage(detect_face_img)

        btn2 = Button(bg_lbl, image=self.detect_face_img,command=self.face_detect, cursor="hand2")
        btn2.place(x=500,y=100,width=120,height=120)

        btn1_2 = Button(bg_lbl, text='Face Detector', cursor="hand2",command=self.face_detect, font=("times new roman",12,'bold'),bg='darkblue', fg='white')
        btn1_2.place(x=500,y=220,width=120,height=30)

        
# Attendance button

  
        attendance_img = Image.open('./img/attendance.png')
        attendance_img = attendance_img.resize((120,120),Image.ANTIALIAS)
        self.attendance_img = ImageTk.PhotoImage(attendance_img)

        btn2 = Button(bg_lbl, image=self.attendance_img, cursor="hand2", command=self.attendance)
        btn2.place(x=800,y=100,width=120,height=120)

        btn1_2 = Button(bg_lbl, text='Attendance', cursor="hand2",command=self.attendance, font=("times new roman",12,'bold'),bg='darkblue', fg='white')
        btn1_2.place(x=800,y=220,width=120,height=30)

      
# Help Desk button

  
        # help_desk_img = Image.open('./img/help.jpg')
        # help_desk_img = help_desk_img.resize((120,120),Image.ANTIALIAS)
        # self.help_desk_img = ImageTk.PhotoImage(help_desk_img)

        # btn2 = Button(bg_lbl, image=self.help_desk_img, cursor="hand2")
        # btn2.place(x=1100,y=100,width=120,height=120)

        # btn1_2 = Button(bg_lbl, text='Help Desk', cursor="hand2", font=("times new roman",12,'bold'),bg='darkblue', fg='white')
        # btn1_2.place(x=1100,y=220,width=120,height=30)


# Train Data button

  
        train_data_img = Image.open('./img/training_data.jpg')
        train_data_img = train_data_img.resize((120,120),Image.ANTIALIAS)
        self.train_data_img = ImageTk.PhotoImage(train_data_img)

        btn1 = Button(bg_lbl, image=self.train_data_img, cursor="hand2",command=self.train_data)
        btn1.place(x=200,y=350,width=120,height=120)

        btn1_1 = Button(bg_lbl, text='Train Data', cursor="hand2",command=self.train_data, font=("times new roman",12,'bold'),bg='darkblue', fg='white')
        btn1_1.place(x=200,y=470,width=120,height=30)


# Photos button

  
        photos_img = Image.open('./img/photos.jpg')
        photos_img = photos_img.resize((120,120),Image.ANTIALIAS)
        self.photos_img = ImageTk.PhotoImage(photos_img)

        btn2 = Button(bg_lbl, image=self.photos_img, command=self.open_photos,cursor="hand2")
        btn2.place(x=500,y=350,width=120,height=120)

        btn1_2 = Button(bg_lbl, text='Photos',command=self.open_photos, cursor="hand2", font=("times new roman",12,'bold'),bg='darkblue', fg='white')
        btn1_2.place(x=500,y=470,width=120,height=30)

        
# Developer button

  
        developer_img = Image.open('./img/developer.jpeg')
        developer_img = developer_img.resize((120,120),Image.ANTIALIAS)
        self.developer_img = ImageTk.PhotoImage(developer_img)

        btn2 = Button(bg_lbl, image=self.developer_img, cursor="hand2")
        btn2.place(x=800,y=350,width=120,height=120)

        btn1_2 = Button(bg_lbl, text='Developer', cursor="hand2", font=("times new roman",12,'bold'),bg='darkblue', fg='white')
        btn1_2.place(x=800,y=470,width=120,height=30)

      
# Exit button

  
        exit_img = Image.open('./img/exit.jpg')
        exit_img = exit_img.resize((120,120),Image.ANTIALIAS)
        self.exit_img = ImageTk.PhotoImage(exit_img)

        btn2 = Button(bg_lbl, image=self.exit_img, cursor="hand2", command=self.iExit)
        btn2.place(x=1100,y=350,width=120,height=120)

        btn1_2 = Button(bg_lbl, text='Exit', cursor="hand2", font=("times new roman",12,'bold'),bg='darkblue', fg='white', command=self.iExit)
        btn1_2.place(x=1100,y=470,width=120,height=30)

# =================Button Functions==========

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_detect(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def open_photos(self):
        os.startfile('data')
        
    def iExit(self):
            self.iexit = messagebox.askyesno('Face Recognition', "Are You Want to exit..!!",parent=self.root)
            if self.iexit > 0:
                    self.root.destroy()
            else:
                    return


if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
    