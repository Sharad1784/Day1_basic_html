import tkinter as tk
from tkinter import messagebox

root=tk.Tk()
root.geometry("300x300")
root.title("Listbox")

def show_selection():
    selected_indices:any=List1.curselection()
    if selected_indices:
        selected_item: any=List1.get(selected_indices[0])
        messagebox.showinfo("Selected value",f"You selected {selected_item} at {selected_indices[0]}")
    else:
        messagebox.showinfo("You havent selected a value")

def clear_selection():
    selected_indices: any=List1.curselection()
    if selected_indices:
        List1.selection_clear(selected_indices[0])
        messagebox.showinfo('clearification','your selection has been cleared')
List1=tk.Listbox(root,height=5,width=5,selectmode='single')
List1.pack()

values: list[str]=['Python','Java','react','C++']
for value in values:
    List1.insert(tk.END,value)

btn1 = tk.Button(root,text="selection made",font=('Arial',14),command=show_selection)
btn1.pack()

btn2 = tk.Button(root,text="clear",font=('Arial',14),command=clear_selection)
btn2.pack()

root.mainloop()
