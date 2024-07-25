from customtkinter import *
from PIL import Image
from tkinter import messagebox
import subprocess

def login():
    if usernameEntry.get()=="" or passwordEntry.get()=="":
        messagebox.showerror("Error","All fields are required")
    
    elif usernameEntry.get()=="Aftab Alam" or passwordEntry.get()==1234:
        messagebox.showinfo("Success","Login Successfull")
        root.destroy()
        try:   
            subprocess.Popen(["python", r"C:\Users\DELL\OneDrive\Desktop\Tkinter Project\Employee Management system\ems.py"])
        except Exception as e:
                messagebox.showerror("Error", f"Failed to open the file: {e}")
    else:
        messagebox.showerror("Error", "Invalid credentials")
    # root.destroy()
    
# main window
root=CTk()
root.geometry("930x478")
root.title("Login Page")
root.resizable(0,0)
root.config(background="white")
image=CTkImage(Image.open("C:/Users/DELL/OneDrive/Desktop/Tkinter Project/Employee Management system/OIP2.jpg"),size=(930,478))
imageLabel=CTkLabel(root,image=image,text="")
imageLabel.place(x=110,y=0)

headinglabel=CTkLabel(root,text="Employee Management System",bg_color="white",font=("Goudy Old Style",20,"bold"),text_color="dark blue")
headinglabel.place(x=30,y=120)

usernameEntry=CTkEntry(root,placeholder_text="Enter Your Username",width=180)
usernameEntry.place(x=50,y=170)

passwordEntry=CTkEntry(root,placeholder_text="Enter Your Password",width=180,show="*")
passwordEntry.place(x=50,y=220)

loginButton=CTkButton(root,text="Login",cursor="hand2",command=login)
loginButton.place(x=70,y=270)

root.mainloop()