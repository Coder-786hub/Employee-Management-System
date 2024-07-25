from customtkinter import *
from PIL import Image
from tkinter import ttk, messagebox
import database







# Functions

def delete_all():
    result=messagebox.askyesno("Confirm","Do yo really want to delete")
    if result:
        database.deleteall_records()
        treeview_data()

def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set("Search By")

def search_employee():
    if searchEntry.get() == "":
        messagebox.showerror("Error", "Enter value to search")
    elif searchBox.get() == "Search By":
        messagebox.showerror("Error", "Please Choose Option")
    else:
        search_data = database.search(searchBox.get(), searchEntry.get())
        
        tree.delete(*tree.get_children())
        for employee in search_data:
            tree.insert("",END,values=employee)

def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error", "Select data to delete")
    else:
        try:
            id_to_delete = int(idEntry.get())  
            database.delete(id_to_delete)
            treeview_data()
            clear()
            messagebox.showinfo("Success", "Data Deleted Successfully")
        except ValueError:
            messagebox.showerror("Error", "Invalid ID. Please enter a valid numeric ID.")



def update_employee():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("Error","select data to update")
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Data is updated")

def selection(event):
    selection_item=tree.selection()
    if selection_item:
        row=tree.item(selection_item)["values"]
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])





def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    roleBox.set("Select Role")
    genderBox.set("Choose Gender")
    salaryEntry.delete(0,END)


def treeview_data():
    employees=database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert("",END,values=employee)



def add_employee():
    if idEntry.get()=="" or nameEntry.get()=="" or phoneEntry.get()=="" or salaryEntry.get()=="":
        messagebox.showerror("Error","All fields are required")

    elif not idEntry.get().startswith("EMP"):
        messagebox.showerror("Error","ID should be start With 'EMP' ")

    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Data inserted in MySql Database")
 

# GUI Part
window=CTk()
window.geometry("1050x580+100+100")
window.resizable(False,False)
window.configure(fg_color="#161C30")
window.title("Employee Management System")
logo=CTkImage(Image.open("C:/Users/DELL/OneDrive/Desktop/Tkinter Project/Employee Management system/background.jpg"),size=(1050,158))
logoLabel=CTkLabel(window,image=logo,text="")
logoLabel.grid(row=0,column=0,columnspan=2)


# Left frame
leftframe=CTkFrame(window,fg_color="#161C30")
leftframe.grid(row=1,column=0)

idlabel=CTkLabel(leftframe,text="Id",font=("arial",18,"bold"),text_color="white")
idlabel.grid(row=0,column=0,padx=20,pady=15,sticky="w")

idEntry=CTkEntry(leftframe,font=("arial",15,"bold"),width=180)
idEntry.grid(row=0,column=1)

namelabel=CTkLabel(leftframe,text="Name",font=("arial",18,"bold"),text_color="white")
namelabel.grid(row=1,column=0,padx=20,pady=15,sticky="w")

nameEntry=CTkEntry(leftframe,font=("arial",15,"bold"),width=180)
nameEntry.grid(row=1,column=1)

phonelabel=CTkLabel(leftframe,text="Phone",font=("arial",18,"bold"),text_color="white")
phonelabel.grid(row=2,column=0,padx=20,pady=15,sticky="w")

phoneEntry=CTkEntry(leftframe,font=("arial",15,"bold"),width=180)
phoneEntry.grid(row=2,column=1)

rolelabel=CTkLabel(leftframe,text="Role",font=("arial",18,"bold"),text_color="white")
rolelabel.grid(row=3,column=0,padx=20,pady=15,sticky="w")

role_options = [
    "Web Developer",
    "Cloud Architect",
    "Data Scientist",
    "Machine Learning Engineer",
    "Cybersecurity Analyst",
    "DevOps Engineer",
    "Software Engineer",
    "Network Engineer",
    "Database Administrator",
    "Systems Analyst",
    "IT Support Specialist",
    "IT Project Manager",
    "Full Stack Developer",
    "Mobile App Developer",
    "Blockchain Developer",
    "AI Research Scientist",
    "Game Developer",
    "IT Consultant",
    "Product Manager",
    "UI/UX Designer",
    "Business Analyst",
    "Site Reliability Engineer",
    "Technical Writer",
    "IT Auditor"
]
roleBox=CTkComboBox(leftframe,values=role_options,width=180,state="readonly",font=("arial",15,"bold"))
roleBox.grid(row=3,column=1)
roleBox.set("Select Role")

genderlabel=CTkLabel(leftframe,text="Gender",font=("arial",18,"bold"),text_color="white")
genderlabel.grid(row=4,column=0,padx=20,pady=15,sticky="w")

gender_options=["Male","Female"]
genderBox=CTkComboBox(leftframe,values=gender_options,width=180,state="readonly",font=("arial",15,"bold"))
genderBox.grid(row=4,column=1)
genderBox.set("Choose Gender")

salarylabel=CTkLabel(leftframe,text="Salary",font=("arial",18,"bold"),text_color="white")
salarylabel.grid(row=5,column=0,padx=20,pady=15,sticky="w")

salaryEntry=CTkEntry(leftframe,font=("arial",15,"bold"),width=180)
salaryEntry.grid(row=5,column=1)

# Right frame
rightframe=CTkFrame(window)
rightframe.grid(row=1,column=1)

search_options=["Id","Name","Phone","Role","Gender","Salary"]
searchBox=CTkComboBox(rightframe,values=search_options,state="readonly")
searchBox.grid(row=0,column=0)
searchBox.set("Search By")

searchEntry=CTkEntry(rightframe)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightframe,text="Serach",width=100,cursor="hand2",command=search_employee)
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightframe,text="Show All",width=100,cursor="hand2",command=show_all)
showallButton.grid(row=0,column=3,pady=5)

tree=ttk.Treeview(rightframe,height=11)
tree.grid(row=1,column=0,columnspan=4,padx=10)

tree["columns"]=("Id","Name","Phone","Role","Gender","Salary")
tree.heading("Id",text="Id")
tree.heading("Name",text="Name")
tree.heading("Phone",text="Phone")
tree.heading("Role",text="Role")
tree.heading("Gender",text="Gender")
tree.heading("Salary",text="Salary")

tree.config(show="headings")
tree.column("Id",width=100)
tree.column("Name",width=160)
tree.column("Phone",width=160)
tree.column("Role",width=240)
tree.column("Gender",width=80)
tree.column("Salary",width=140)

style=ttk.Style()
style.configure("Treeview.Heading",font=("arial",18,"bold"))
style.configure("Treeview",font=("arial",15,"bold"),rowheight=30,background="#161C30",foreground="white")

scrollbar=ttk.Scrollbar(rightframe,orient=VERTICAL,command=tree.yview)
scrollbar.grid(row=1,column=4,sticky="ns")

tree.config(yscrollcommand=scrollbar.set)
# Button Frame

buttonFrame=CTkFrame(window,fg_color="#161C30")
buttonFrame.grid(row=2,column=0,columnspan=2,pady=10)

newButton=CTkButton(buttonFrame,text="New Employee",font=("arial",15,"bold"),width=160,corner_radius=15,cursor="hand2",command=lambda:clear(True))
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text="Add Employee",font=("arial",15,"bold"),width=160,corner_radius=15,cursor="hand2",command=add_employee)
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFrame,text="Update Employee",font=("arial",15,"bold"),width=160,corner_radius=15,cursor="hand2",command=update_employee)
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFrame,text="Delete Employee",font=("arial",15,"bold"),width=160,corner_radius=15,cursor="hand2",command=delete_employee)
deleteButton.grid(row=0,column=3,pady=5,padx=5)

deleteallButton=CTkButton(buttonFrame,text="Delete All",font=("arial",15,"bold"),width=160,corner_radius=15,cursor="hand2",command=delete_all)
deleteallButton.grid(row=0,column=4,pady=5,padx=5)


treeview_data()

window.bind("<ButtonRelease>",selection)
# mainloop
window.mainloop()
