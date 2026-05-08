from tkinter import *
from tkinter import messagebox
import pymysql as my

backround="#06238D"
framebg="#EDEDED"
framefg="#06283D"


def register():
    username=user.get()
    password=passw.get()
    admincode=adminaccess.get()
    if(admincode=="1234"):
        if(username=="" or password=="" or username=="UserName" or password=="Password"):
            messagebox.showerror("Error","Please Enter Username and Password !!!")
        else:
            try:
                mydb=my.connect(
                    host="localhost",
                    user="root",
                    password="indhu",
                    # charset="utf8"
                )
                mycursor=mydb.cursor()
                print("Database Connected")
            except:
                messagebox.showerror("Error","Database Connectivity Issue !!!")
            try:
                command="create database data"
                mycursor.execute(command)
                command="use data"
                mycursor.execute(command)
                command="create table employee(sno int primary key auto_increment,username varchar(50) not null,password varchar(50) not null)"
                mycursor.execute(command)
                command="insert into employee(username,password) values(%s,%s)"
                mycursor.execute(command,(username,password))
                mydb.commit()
                messagebox.showinfo("Success","User Added Successfully !!!")
                user.delete(0,"end")
                passw.delete(0,"end")
                adminaccess.delete(0,"end")
            except:
                print("Error in try block")
                command="use data"
                mycursor.execute(command)
                command="insert into employee(username,password) values(%s,%s)"
                mycursor.execute(command,(username,password))
                mydb.commit()
                messagebox.showinfo("Success","User Added Successfully !!!")
                user.delete(0,"end")
                passw.delete(0,"end")
                adminaccess.delete(0,"end")
    else:
        messagebox.showerror("AdminCode Error!","Please Enter Correct Admin Code to Add New User !!!")







def login():
    root.destroy()
    import LoginSys

root=Tk()
root.title("New User Register")
root.geometry("1250x700+210+100")
root.config(bg=backround)
root.resizable(False,False)

#icon image
image_icon=PhotoImage(file="Project/icon.png")
root.iconphoto(False,image_icon)
#background image
frame=Frame(root,bg="red")
frame.pack(fill=Y)
backround_image=PhotoImage(file="Project/register.png")
Label(frame,image=backround_image).pack()

#AdminKey
adminaccess=Entry(frame,width=15,fg="#000",border=0,bg="#e8ecf7",font=("Arial Bold",20))
adminaccess.config(show="*")
adminaccess.place(x=550,y=280)
adminaccess.focus()

#username
def mouse_over(e):
    name=user.get()
    if name=="UserName":
        user.delete(0,"end")
def mouse_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"UserName")
user=Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=('Arial Bold',24))
user.place(x=500,y=375)
user.insert(0,"UserName")
user.bind("<FocusIn>",mouse_over)
user.bind("<FocusOut>",mouse_leave)

#password
def mouse_over(e):
    name=passw.get()
    if name=="Password":
        passw.delete(0,"end")
        passw.config(show="*")
def mouse_leave(e):
    name=passw.get()
    if name=="":
        passw.insert(0,"Password")
        passw.config(show="")
passw=Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=('Arial Bold',24))
passw.place(x=500,y=465)
passw.insert(0,"Password")
passw.bind("<FocusIn>",mouse_over)
passw.bind("<FocusOut>",mouse_leave)

# open eye and close eye

btneye=True

def hide():
    global btneye
    data=passw.get()
    if data!="Password":
        if btneye:
            passw.config(show="")
            eyeButton.config(image=closeeye)
            btneye=False
        else:
            passw.config(show="*")
            eyeButton.config(image=openeye)
            btneye=True
    
openeye=PhotoImage(file="Project/openeye.png")
closeeye=PhotoImage(file="Project/closeeye.png")

eyeButton=Button(frame,image=openeye,bg="#375174",bd=0,activebackground="#375174",cursor="hand2",command=hide)
eyeButton.place(x=780,y=473)

# RegisterButton

Button(frame,width=10,height=1,fg="#fff",border=0,bg="#445b88",font=('Arial Bold',24),text="Signup",cursor='hand2',activebackground="#445b88",command=register).place(x=530,y=587)

label=Label(root,text="Already have an account?",fg="#fff",bg="#00264d",font=('Microsoft New Tai Lue',15))
label.place(x=520,y=530)
login_btn=Button(root,width=11,text="Login",bg="#00264d",cursor='hand2',fg='#57a1f8',font=('Microsoft New Tai Lue',15),bd=0,activebackground="#00264d",command=login)
login_btn.place(x=750,y=525)

root.mainloop()