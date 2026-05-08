from tkinter import *
from tkinter import messagebox
import pymysql as my
backround="#06238D"
framebg="#EDEDED"
framefg="#06283D"

def register():
    root.destroy()
    import Registersys


def login():
    username=user.get()
    password=passw.get()
    if username=="" or password=="" or username=="UserName" or password=="Password":
       messagebox.showerror("Error","Please Enter Username and Password 😞")
    else:
        try:
            mydb=my.connect(
                host="localhost",
                user="root",
                password="indhu",
                database="data",
                # charset="utf8"
                
            )
            mycursor=mydb.cursor()
            print("Database Connected")
        except:
            messagebox.showerror("DatabaseError","Database Connectivity Issue 😞")
            return
        try:
            command="select * from employee where username=%s and password=%s"
            mycursor.execute(command,(username,password))
            result=mycursor.fetchone() #fetchone-it displays first row
            if(result==None):
                    messagebox.showerror("Error","Invalid Username or Password 😞")
            else:
                messagebox.showinfo("Success","Login Successful 😊")
                messagebox.showinfo("Welcome",f"Welcome {username} 😊") #message content (f-string)
                user.delete(0,"end")
                passw.delete(0,"end")
                root.destroy()
        except:
            messagebox.showerror("Error","Invalid Username or Password 😞")







root=Tk()
root.title("Login System")
root.geometry("1250x700+210+100")
root.config(bg=backround)
root.resizable(True,True)

# #icon image
image_icon=PhotoImage(file="Project/icon.png")
root.iconphoto(False,image_icon)

# # #background image
frame=Frame(root,bg="red")
frame.pack(fill=Y) #vertical
bg_img=PhotoImage(file="Project/LOGIN.png")
Label(frame,image=bg_img,bg=framebg).pack()

# # #username
def mouse_over(e):
    name=user.get()
    if name=="UserName":
        user.delete(0,END)
def mouse_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"UserName")
    

user=Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=('Arial Bold',24))
user.insert(0,"UserName")
user.place(x=500,y=310)
user.bind("<FocusIn>",mouse_over) #bind method is used for events
user.bind("<FocusOut>",mouse_leave)

# # #password
def mouse_over(e):
    data=passw.get()
    if data=="Password":
        passw.delete(0,END)
        passw.config(show="*")
def mouse_leave(e):
    data=passw.get()
    if data=="":
        passw.insert(0,"Password")
        passw.config(show="")
        
passw=Entry(frame,width=18,fg="#fff",border=0,bg="#375174",font=('Arial Bold',24))
passw.insert(0,"Password")
passw.bind("<FocusIn>",mouse_over)
passw.bind("<FocusOut>",mouse_leave)
passw.place(x=500,y=405)

# # # open and close eye
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
eyeButton.place(x=780,y=410)


# # # LoginButton

Button(frame,width=10,height=1,fg="#fff",border=0,bg="#375174",font=('Arial Bold',24),text="Login",cursor='hand2',activebackground="#375174",command=login).place(x=530,y=587)

# # # Message for new account
label=Label(root,text="Don't have an account?",fg="#fff",bg="#00264d",font=('Microsoft New Tai Lue',15))
label.place(x=530,y=500)
register_btn=Button(root,width=11,text="Add New User",bg="#00264d",cursor='hand2',fg='#57a1f8',font=('Microsoft New Tai Lue',15),bd=0,activebackground="#00264d",command=register)
register_btn.place(x=750,y=495)

root.mainloop()