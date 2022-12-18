from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class qr_generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator Developed by Shreya Biswas")
        self.root.resizable(False,False)
        title=Label(self.root,text="Qr_Code_Generator",font=("times new roman",40),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)
        #=====Employee details window======
        #=====variables====
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()
        emp_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_frame.place(x=20,y=100,width=460,height=380)
        emp_title=Label(emp_frame,text="Employee Details",font=("goudy old style",20),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)
        lbl_emp_code=Label(emp_frame,text="Employee ID",font=("times new roman",15,'bold'),bg='white').place(x=5,y=40)
        lbl_name=Label(emp_frame,text="Name",font=("times new roman",15,'bold'),bg='white').place(x=5,y=80)
        lbl_department=Label(emp_frame,text="Department",font=("times new roman",15,'bold'),bg='white').place(x=5,y=120)
        lbl_designation=Label(emp_frame,text="Designation",font=("times new roman",15,'bold'),bg='white').place(x=5,y=160)
        txt_emp_code=Entry(emp_frame,font=("times new roman",15),textvariable=self.var_emp_code,bg='lightyellow').place(x=200,y=43)
        txt_name=Entry(emp_frame,font=("times new roman",15),textvariable=self.var_name,bg='lightyellow').place(x=200,y=80)
        txt_department=Entry(emp_frame,font=("times new roman",15),textvariable=self.var_department,bg='lightyellow').place(x=200,y=120)
        txt_designation=Entry(emp_frame,font=("times new roman",15),textvariable=self.var_designation,bg='lightyellow').place(x=200,y=160)

        btn_generate=Button(emp_frame,text='Generate QR',command=self.generate,font=("times new roman",15,'bold'),bg='#2196f3',fg='white').place(x=40,y=240,width=130,height=40)
        btn_clear=Button(emp_frame,text='Clear',command=self.clear,font=("times new roman",15,'bold'),bg='#607d8b',fg='white').place(x=250,y=240,width=100,height=40)
        self.msg=''
        self.lbl_msg=Label(emp_frame,text=self.msg,font=("times new roman",15,'bold'),bg='white',fg='green')
        self.lbl_msg.place(x=100,y=310)
        emp_frame2=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_frame2.place(x=550,y=100,width=300,height=380)
        emp_title=Label(emp_frame2,text="Employee QR code",font=("goudy old style",20),bg='#053246',fg='white').place(x=0,y=0,relwidth=1)
        self.emp_frame2=Label(emp_frame2,text="QR CODE \nNot Available",font=('times new roman',15),bg='#053246',fg='white',bd=1,relief=RIDGE)
        self.emp_frame2.place(x=60,y=100,height=180,width=180)
    def clear(self):
            self.var_emp_code.set('')
            self.var_name.set('')
            self.var_department.set('')
            self.var_designation.set('')
            self.msg=''
            self.lbl_msg.config(text=self.msg)
            self.emp_frame2.config(image='')
    def generate(self):
            if self.var_emp_code.get()=='' or self.var_name.get()=='' or self.var_department.get()=='' or self.var_designation.get()=='':
                self.msg='All fields are required!!!!'
                self.lbl_msg.config(text=self.msg,fg='red')
            else:
                qr_data=(f"Employee ID:{self.var_emp_code.get()}\n Employee Name:{self.var_name.get()}\n Employee Dept:{self.var_department.get()} \n Employee Designation:{self.var_designation.get()}")
                emp_frame2=qrcode.make(qr_data)
                #print(qr_code)
                emp_frame2=resizeimage.resize_cover(emp_frame2,[180,180])
                #qr_code.save("employee")
                self.im=ImageTk.PhotoImage(emp_frame2)
                self.emp_frame2.config(image=self.im)
                self.msg='Qr Generated Successfully!!!'
                self.lbl_msg.config(text=self.msg,fg='green')
root=Tk()
obj=qr_generator(root)
root.mainloop()

