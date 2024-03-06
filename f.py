from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter.ttk import Combobox
root = Tk()
root.title("My app")
root.geometry("500x500")

def connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port=3306,
        database="python"
    )

def insertdata(uname,email,phone,gender,city,state):
    if(uname=="" or email=="" or phone=="" or gender=="" or city=="" or state==""):
        messagebox.showinfo("massage","please fill the form")
    
    else:    
        con = connection()
        cursor =con.cursor()
        qry = "insert into reg values(%s,%s,%s,%s,%s,%s,%s)"
        val = (0,uname,email,phone,gender,city,state)
        cursor.execute(qry,val)
        con.commit()

var=StringVar()
var.set("radio")
varcity=StringVar()
varstate=StringVar()

l1= Label(text="name*").place(x=100,y=100)
l2= Label(text="email*").place(x=100,y=130)
l3= Label(text="phone*").place(x=100,y=160)
l4= Label(text="gender*").place(x=100,y=190)
l5= Label(text="city*").place(x=100,y=220)
l6= Label(text="state*").place(x=100,y=250)

t1 = Entry(root)
t2 = Entry(root)
t3 = Entry(root)
radio=Radiobutton(root,text="male",padx=14,variable=var,value="male")
radio1=Radiobutton(root,text="female",padx=14,variable=var,value="female")
box=Combobox(root,textvariable=varcity,values=["surat","ahemdabad","rajkot","jamnagar","amrali"])
box1=Combobox(root,textvariable=varstate,values=["gujarat","bombay","chennai","banglore","kolkata"])

t1.place(x=170,y=100)
t2.place(x=170,y=130)
t3.place(x=170,y=160)
radio.place(x=170,y=190)
radio1.place(x=270,y=190)
box.place(x=200,y=220)
box1.place(x=200,y=250)

btn  = Button(root,text="Submit", fg="red",bg="yellow",command=lambda:insertdata(t1.get(),t2.get(),t3.get(),var.get(),varcity.get(),varstate.get())).place(x=170,y=280)

root.mainloop()