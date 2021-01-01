from tkinter import *
from tkinter import messagebox
import time
import os
class File_App:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Database Management System")
        self.root.geometry("1350x700+0+0")

        
        title=Label(self.root,text="Student Database Management System",bd=10,pady=15,font=("times new roman",35,"bold")).pack(fill=X)
        studentFrame=Frame(self.root,bd=15)
        studentFrame.place(x=20,y=100,height=400)
        
        studentTitle=Label(studentFrame,text="Student Profile",font=("times new roman",25,"bold")).grid(row=0,column=0,pady=20)

        self.sId=StringVar()
        self.sContact=StringVar()
        self.sName=StringVar()
        self.sDob=StringVar()

        
        studentID=Label(studentFrame,text="Student ID",font=("times new roman",25,"bold")).grid(row=1,column=0,pady=10,padx=20)
        textID=Entry(studentFrame,bd=7,width=25,textvariable=self.sId,font="arial 15 bold").grid(row=1,column=1,padx=20,pady=10)
        
        studentContact=Label(studentFrame,text="Contact",font=("times new roman",25,"bold")).grid(row=1,column=2,pady=10,padx=20)
        textContact=Entry(studentFrame,bd=7,textvariable=self.sContact,width=25,font="arial 15 bold").grid(row=1,column=3,padx=20,pady=10)

        studentName=Label(studentFrame,text="Name",font=("times new roman",25,"bold")).grid(row=2,column=0,pady=10,padx=20)
        textName=Entry(studentFrame,bd=7,width=25,textvariable=self.sName,font="arial 15 bold").grid(row=2,column=1,padx=20,pady=10)

        studentDOB=Label(studentFrame,text="DOB(dd/mm/yyyy)",font=("times new roman",25,"bold")).grid(row=2,column=2,pady=10,padx=20)
        textDOB=Entry(studentFrame,bd=7,width=25,textvariable=self.sDob,font="arial 15 bold").grid(row=2,column=3,padx=20,pady=10)

        btnFrame=Frame(self.root,bd=10)
        btnFrame.place(x=10,y=600)

        btnCreate=Button(btnFrame,text="Create",command=self.save_data,font="arial 15 bold",bd=7,width=15).grid(row=0,column=0,padx=20,pady=20)
        btnRead=Button(btnFrame,command=self.get_data,text="Read",font="arial 15 bold",bd=7,width=15).grid(row=0,column=3,padx=20,pady=20)
        btnDelete=Button(btnFrame,command=self.delete,text="Delete",font="arial 15 bold",bd=7,width=15).grid(row=0,column=5,padx=20,pady=20)

    def save_data(self):
        if self.sId.get()=='':
            messagebox.showerror("Error","Student ID is required")
        else:
            present='no'
            f=os.listdir("files/")
            for i in f:
                    if i.split(".")[0]==self.sId.get():
                        present='yes'
            if present=='yes':
                messagebox.showerror("Error","File already exists")
            else:
                f=open("files/"+str(self.sId.get())+".txt","w")
                f.write(str(self.sId.get())+","+
                        str(self.sContact.get())+","+
                        str(self.sName.get())+","+
                        str(self.sDob.get())+",")
                f.close()
                messagebox.showinfo("Success","Record has been saved")
            
    def get_data(self):
        present='no'
        if self.sId.get()=='':
            messagebox.showerror("Error","Student ID is required")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0]==self.sId.get():
                        present='yes'
            if present=='no':
                messagebox.askquestion("what","name")
                messagebox.showerror("Error","File not found")
            else:
                f1=open("files/"+self.sId.get()+'.txt')
                value=[]
                for f in f1:
                    value=f.split(",")
                messagebox.showinfo("Student Details",
                "Student Id : %s\nStudent Name : %s\nStudent Contact : %s\nStudent DOB : %s "%(value[0],value[2],value[1],value[3]))
                f1.close()

    def delete(self):
        present='no'
        if self.sId.get()=='':
            messagebox.showerror("Error","Student ID is required")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0]==self.sId.get():
                        present='yes'
            if present=='no':
                messagebox.askquestion("what","name")
                messagebox.showerror("Error","File not found")
            else:
                ask=messagebox.askyesno("Delete","Do you really want to delete "+self.sId.get()+"?")
                if ask>0:
                    os.remove("files/"+self.sId.get()+".txt")
                    messagebox.showinfo("Success","Deleted Successfully")
                 
                    
    
root=Tk()
ob=File_App(root)
root.mainloop()
                                                                              
