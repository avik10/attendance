from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog
from PIL import Image, ImageTk
import mysql.connector
import cv2

myData = []
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('Attendance Details')

        # ============Varriables ========
        self.attend_id = StringVar()
        self.attend_name = StringVar()
        self.attend_class = StringVar()
        self.attend_sec = StringVar()
        self.attend_roll = StringVar()
        self.attend_date = StringVar()
        self.attend_time = StringVar()
        self.attend_status = StringVar()
        

# first iamge
        img1 = Image.open('./img/smart-attendance.jpg')
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=800, height=200)
# second image

        img2 = Image.open('./img/clg.jpg')
        img2 = img2.resize((800, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800, y=0, width=800, height=200)

        img4 = Image.open('./img/face_detector1.jpg')
        img4 = img4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_lbl = Label(self.root, image=self.photoimg4)
        bg_lbl.place(x=0, y=130, width=1530, height=710)
# heading
        title_lbl = Label(bg_lbl, text="Attendance Management", font=(
            "times new roman", 30, 'bold'), bg='white', fg='red')
        title_lbl.place(x=0, y=0, width=1530, height=45)
# Main Frame
        main_frame = Frame(bg_lbl, bd=2)
        main_frame.place(x=10, y=55, width=1330, height=500)
# Left Frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details", font=(
            "times new roman", 12, 'bold'))
        left_frame.place(x=10, y=10, width=650, height=480)

        left_img = Image.open('./img/student.jpg')
        left_img = left_img.resize((635, 150), Image.ANTIALIAS)
        self.left_img = ImageTk.PhotoImage(left_img)

        f_lbl = Label(left_frame, image=self.left_img)
        f_lbl.place(x=5, y=0, width=635, height=150)

        left_inside_frame = LabelFrame(left_frame, bd=2, relief=RIDGE)
        left_inside_frame.place(x=5, y=160, width=635, height=290)
# Attendance Id
        attendance_label = Label(left_inside_frame, text="Attendance ID",
                                font=("times new roman", 12))
        attendance_label.grid(row=0, column=0, padx=5)

        attendance_inp = Entry(left_inside_frame, justify=CENTER, font=(
            "times new roman", 12, 'bold'), width=22, bd=2 , textvariable=self.attend_id)
        attendance_inp.grid(row=0, column=1, padx=5,  pady= 5, sticky=W)
# Roll
        std_roll_label = Label(left_inside_frame,
                               text="Roll", font=("times new roman", 12))
        std_roll_label.grid(row=0, column=2, padx=15, pady=5)

        std_roll_inp = Entry(left_inside_frame, justify=CENTER, font=(
            "times new roman", 12, 'bold'), width=22, bd=2, textvariable=self.attend_roll)
        std_roll_inp.grid(row=0, column=3, padx=5, pady=5)
# Student name
        std_name_label = Label(left_inside_frame,
                               text="Name", font=("times new roman", 12))
        std_name_label.grid(row=1, column=0, padx=5)

        std_name_inp = Entry(left_inside_frame, justify=CENTER, font=(
            "times new roman", 12, 'bold'), width=22, bd=2, textvariable=self.attend_name)
        std_name_inp.grid(row=1, column=1, padx=5, sticky=W)
# Class
        std_sec_label = Label(left_inside_frame,
                              text="Class", font=("times new roman", 12))
        std_sec_label.grid(row=1, column=2, padx=15)

        std_sec_inp = ttk.Combobox(left_inside_frame, font=(
            "times new roman", 12), state="readonly" , textvariable=self.attend_class)
        std_sec_inp["values"] = ("Please Select", '1', '2', '3')
        std_sec_inp.current(0)
        std_sec_inp.grid(row=1, column=3, padx=5, pady=5)
# Section
        # std_sec_label = Label(left_inside_frame,
        #                       text="Section", font=("times new roman", 12))
        # std_sec_label.grid(row=1, column=4, padx=15)

        # std_sec_inp = ttk.Combobox(left_inside_frame, font=(
        #     "times new roman", 12), state="readonly")
        # std_sec_inp["values"] = ("Please Select", 'A', 'B', 'C')
        # std_sec_inp.current(0)
        # std_sec_inp.grid(row=1, column=5, padx=5, pady=5)
# Date
        std_name_label = Label(left_inside_frame,
                               text="Date", font=("times new roman", 12))
        std_name_label.grid(row=2, column=0, padx=5)

        std_name_inp = Entry(left_inside_frame, justify=CENTER, font=(
            "times new roman", 12, 'bold'), width=22, bd=2, textvariable=self.attend_date)
        std_name_inp.grid(row=2, column=1, padx=5, sticky=W)
# Time
        std_roll_label = Label(left_inside_frame,
                               text="Time", font=("times new roman", 12))
        std_roll_label.grid(row=2, column=2, padx=15, pady=5)

        std_roll_inp = Entry(left_inside_frame, justify=CENTER, font=(
            "times new roman", 12, 'bold'), width=22, bd=2, textvariable=self.attend_time)
        std_roll_inp.grid(row=2, column=3, padx=5, pady=5)
# Attendance Status
        std_sec_label = Label(left_inside_frame,
                              text="Attendance Status", font=("times new roman", 12))
        std_sec_label.grid(row=3, column=0, padx=15)

        std_sec_inp = ttk.Combobox(left_inside_frame, font=(
            "times new roman", 12), state="readonly", textvariable=self.attend_status)
        std_sec_inp["values"] = ("Please Select", 'Present', 'Absent')
        std_sec_inp.current(0)
        std_sec_inp.grid(row=3, column=1, padx=5, pady=5)
# Buttons
        button_frame = Frame(left_frame, bd=2, relief=RIDGE)
        button_frame.place(x=5, y=360, width=635, height=90)

        save_btn = Button(button_frame, text="Import", width=10, font=(
            "times new roman", 12, 'bold'), bg="cyan", command=self.importCsv)
        save_btn.grid(row=0, column=0, padx=25, pady=15)

        update_btn = Button(button_frame, text="Export", width=10, font=(
            "times new roman", 12, 'bold'), bg="yellow", command=self.exportCsv)
        update_btn.grid(row=0, column=1, padx=25, pady=15)

        delete_btn = Button(button_frame, text="Update", width=10, font=(
            "times new roman", 12, 'bold'), bg="grey", command=self.updateData)
        delete_btn.grid(row=0, column=2, padx=25, pady=15)

        reset_btn = Button(button_frame, text="Reset", width=10, font=(
            "times new roman", 12, 'bold'), bg="red", command=self.reset_data)
        reset_btn.grid(row=0, column=3, padx=25, pady=15)
# Right Frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details", font=(
            "times new roman", 12, 'bold'))
        right_frame.place(x=680, y=10, width=640, height=480)
# Table Frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE)
        table_frame.place(x=5, y=5, width=630, height=450)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=('ID', 'Name',  'Class', 'Section', 'Roll', 'Time', 'Attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('ID', text='ID')
        self.student_table.heading('Name', text='Name')
        self.student_table.heading('Class', text='Class')
        self.student_table.heading('Section', text='Section')
        self.student_table.heading('Roll', text='Roll')
        # self.student_table.heading('Date', text='Date')
        self.student_table.heading('Time', text='Time')
        self.student_table.heading('Attendance', text='Attendance')

        self.student_table['show'] = "headings"

        self.student_table.column('ID', width=20)
        self.student_table.column('Name', width=150)
        self.student_table.column('Class', width=50)
        self.student_table.column('Section', width=50)
        self.student_table.column('Roll', width=50)
        # self.student_table.column('Date', width=100)
        self.student_table.column('Time', width=100)
        self.student_table.column('Attendance', width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind('<ButtonRelease>', self.getCursor)

# ########## Functions ##########
# Fetch Data
    def fetchData(self,rows):
        self.student_table.delete(*self.student_table.get_children())
        for i in rows:
            self.student_table.insert('',END,values=i)
#  import csv
    def importCsv(self):
        global myData
        myData.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select CSV File', filetypes=(("CSV File","*csv"),("ALL File",'.')),parent=self.root)
        with open(fln) as myFile:
            csvreader = csv.reader(myFile,delimiter=',')
            for  i in csvreader:
                myData.append(i)
            self.fetchData(myData)
#  export csv
    def exportCsv(self):
        if len(myData) < 1 :
            messagebox.showerror('Data Export', 'No Data to Export', parent=self.root)
            return
        fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title='Select CSV File', filetypes=(("CSV File","*csv"),("ALL File",'.')),parent=self.root)
        with open(fln, mode='w', newline='') as myFile:
            exp_write = csv.writer(myFile, delimiter=',') 
            for i in myData:
                exp_write.writerow(i)
            messagebox.showinfo('Data Export','Data Export to '+os.path.basename(fln)+ 'file Successfully')
#  get cursor
    def getCursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        rows = content['values']
        self.attend_id.set(rows[0])
        self.attend_name.set(rows[1])
        self.attend_class.set(rows[2])
        self.attend_sec.set(rows[3])
        self.attend_roll.set(rows[4])
        self.attend_date.set(rows[5])
        self.attend_time.set(rows[6])
        self.attend_status.set(rows[7])
#  reset Data
    def reset_data(self):
        self.attend_id.set('')
        self.attend_name.set('')
        self.attend_class.set('')
        self.attend_sec.set('')
        self.attend_roll.set('')
        self.attend_date.set('')
        self.attend_time.set('')
        self.attend_status.set('Please Select')

    def updateData(self):
        with open('attendance.csv', 'r+', newline='\n') as f:
            f.writelines(f"{self.attend_id},{self.attend_name},{self.attend_class},{self.attend_sec},{self.attend_roll},{self.attend_date},{self.attend_time},{self.attend_status}")
        # self.fetchData
if __name__ == '__main__':
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
