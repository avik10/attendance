from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import strftime
from datetime import datetime
from PIL import Image, ImageTk
import mysql.connector
import cv2
import numpy as np
import os

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Face Recognition')
        # title
        title_lbl = Label(self.root, text="Face Recognition", font=(
            "times new roman", 30, 'bold'), bg='white', fg='red')
        title_lbl.place(x=0, y=0, width=1530, height=45)
        # main frame
        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=0, y=50, width=1330, height=500)
        # background image
        top_img = Image.open('./img/face_detector_2.jpg')
        top_img = top_img.resize((1530, 740), Image.ANTIALIAS)
        self.top_img = ImageTk.PhotoImage(top_img)
        bg_lbl = Label(self.root, image=self.top_img)
        bg_lbl.place(x=0, y=48, width=1530, height=740)
        # face detect button
        student_img = Image.open('./img/face_detector1.jpg')
        student_img = student_img.resize((120,120),Image.ANTIALIAS)
        self.student_img = ImageTk.PhotoImage(student_img)

        face_detect_btn = Button(bg_lbl, image=self.student_img, cursor="hand2", command=self.face_recognition)
        face_detect_btn.place(x=700,y=250,width=120,height=120)

        face_detect_btn_1 = Button(bg_lbl, text='Recognize Face',command=self.face_recognition, cursor="hand2", font=("times new roman",12,'bold'),bg='darkgreen', fg='white')
        face_detect_btn_1.place(x=700,y=370,width=120,height=30)
        def time():
                string = strftime("%H:%M:%S %p")
                lbl.config(text = string)
                lbl.after(1000,time)

        lbl = Label(bg_lbl, font=("times new roman",26,'bold'),bg='white', fg='BLUE')
        lbl.place(x=1200,y=0,width=230,height=45)
        time()
############### Mark Attendance ##########
    def mark_attendance(self, id, name, cls, sec, roll):
        now = datetime.now()
        d1 = now.strftime("%d-%m-%Y")
        filename = str(d1)+'.csv'
        try:
            with open(filename, 'r+', newline='\n') as f:
                myDatalis = f.readlines()
                name_list = [] 
                for line in myDatalis:
                    entry = line.split((','))
                    name_list.append(entry[0])
                if ((id not in name_list) and (name not in name_list) and (cls not in name_list) and (sec not in name_list) and (roll not in name_list)):
                    dtString = now.strftime("%H:%M:%S")
                    f.write(f"{id},{name},{cls},{sec},{roll},{dtString},Present")
                    f.write("\n")
        except FileNotFoundError :
            f = open(filename, 'w')
            pass
            f.close()
            self.mark_attendance(id=id, name=name, cls=cls, sec=sec,roll=roll)


        # Face Recognition function
    def face_recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeigour, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeigour)

            coords = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y), (x+w, y+h), (0,255,0), 1)
                id, predict = clf.predict(gray_img[y: y+h, x: x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                host='localhost', username='root', password='root', database='face_recognition_system')
                my_cursor = conn.cursor()
            
                my_cursor.execute('select name from student where student_id='+str(id))
                name = my_cursor.fetchone()
                name = '+'.join(name)

                my_cursor.execute('select roll from student where student_id='+str(id))
                roll = my_cursor.fetchone()
                roll = '+'.join(roll)

                my_cursor.execute('select class from student where student_id='+str(id))
                cls = my_cursor.fetchone()
                cls = '+'.join(cls)

                my_cursor.execute('select sec from student where student_id='+str(id))
                sec = my_cursor.fetchone()
                sec = '+'.join(sec)

                my_cursor.execute('select student_id from student where student_id='+str(id))
                std_id = my_cursor.fetchone()
                std_id = '+'.join(std_id)



                if confidence > 77:
                    cv2.putText(img, f'ID: {std_id}', (x, y-85), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,0), 2)
                    cv2.putText(img, f'Name: {name}', (x, y-65), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,0), 2)
                    cv2.putText(img, f'class: {cls}', (x, y-45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,0), 2)
                    cv2.putText(img, f'Section: {sec}', (x, y-25), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,0), 2)
                    cv2.putText(img, f'Roll: {roll}', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,0), 2)
                    self.mark_attendance(id=std_id, name=name, cls=cls, sec=sec,roll=roll)
                else:
                    cv2.rectangle(img,(x,y), (x+w, y+h), (0,0,255), 1)
                    cv2.putText(img,'Unknown Face', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,0), 2)

                
                coords = [x,y,w,h]
            return coords


        def recognize(img, clf, faceCascade):
            coords =  draw_boundary(img,faceCascade, 1.1,10, (255,25,255), 'Face', clf)
            return img

        
        faceCasCade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read('classifier.xml')

        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read() 
            img = recognize(img, clf, faceCasCade)
            cv2.imshow('Welcome to Face Recognition', img)

            if cv2.waitKey(1)==13:
                break;
        cap.release()
        cv2.destroyAllWindows()



if __name__ == '__main__':
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()