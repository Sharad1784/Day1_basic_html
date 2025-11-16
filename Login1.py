from tkinter import *
from tkinter import messagebox

tk=Tk()
tk.title("LOGIN")
tk.geometry("400x300")
tk.resizable(False,False)
tk.configure(bg="black")

def Register():
    tk.destroy()
    import User_Registration as UR
    Toplevel(UR.root)

def Login():
    Username=entry1.get()
    Password=entry2.get()
    if(Username=="" and Password==""):
        messagebox.showerror("error","Username and Password cannot be empty")
    elif(Username=="sdcn" and Password=="abcd1234"):
        messagebox.showinfo("success","login granted")
    else:
        messagebox.showerror("Sorry", "Invalid Credentials")


Label(tk,text="STUDENT LOGIN",font=("Arial",18,"bold","underline"),bg="black",fg="white").pack()
Label(tk,text="Username",font=("Arial",16,"bold"),bg="black").place(x=50,y=105)
Label(tk,text="Password",font=("Arial",16,"bold"),bg="black").place(x=50,y=155)
entry1=Entry(tk,bd=4)
entry1.place(x=150,y=100)
entry2=Entry(tk,bd=4,show="*")
entry2.place(x=150,y=150)

Button(tk,text="Login",font=("Arial",14,"bold"),command=Login).place(x=260,y=200)
Button(tk,text="Register",font=("Arial",14,"bold"),command=Register).place(x=170,y=200)



tk.mainloop()

