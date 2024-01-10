from time import strftime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
from PIL import Image, ImageTk
import mysql.connector
import cv2
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Train Dataset')

# heading
        title_lbl = Label(self.root, text="Teain Data", font=(
            "times new roman", 30, 'bold'), bg='white', fg='red')
        title_lbl.place(x=0, y=0, width=1530, height=45)
        def time():
                string = strftime("%H:%M:%S %p")
                lbl.config(text = string)
                lbl.after(1000,time)

        lbl = Label(title_lbl, font=("times new roman",26,'bold'),bg='white', fg='BLUE')
        lbl.place(x=1200,y=0,width=230,height=45)
        time()

# TOP image

        top_img = Image.open('./img/header_img2.png')
        top_img = top_img.resize((1530, 300), Image.ANTIALIAS)
        self.top_img = ImageTk.PhotoImage(top_img)

        f_lbl = Label(self.root, image=self.top_img)
        f_lbl.place(x=0, y=48, width=1530, height=300)
# Train Image button
        take_photo_btn = Button(self.root, text="Train Data", width=30, font=(
            "times new roman", 12, 'bold'), bg="black", fg='white', command=self.train_calssifier)
        take_photo_btn.place(x=0, y=350, height=50, width=1530)

# Bottom image

        bottom_img = Image.open('./img/photos.jpg')
        bottom_img = bottom_img.resize((1530, 300), Image.ANTIALIAS)
        self.bottom_img = ImageTk.PhotoImage(bottom_img)

        f_lbl = Label(self.root, image=self.bottom_img)
        f_lbl.place(x=0, y=405, width=1530, height=300)

    def train_calssifier(self):
        data_dir = ('data')
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]


        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow('Training', imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids) 


        # === Train clasiifier and save == 

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write('classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo('Success', 'Training completed..!!')

if __name__ == '__main__':
    root = Tk()
    obj = Train(root)
    root.mainloop()