import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ========================= DB Setup =========================
def init_db():
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    class TEXT,
                    fees_paid REAL DEFAULT 0.0
                )''')
    conn.commit()
    conn.close()

# ===================== Backend Functions =====================
def add_student(name, age, student_class, fees_paid):
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute("INSERT INTO students (name, age, class, fees_paid) VALUES (?, ?, ?, ?)",
              (name, age, student_class, fees_paid))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Student added successfully!")

def fetch_students():
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    data = c.fetchall()
    conn.close()
    return data

def delete_student(student_id):
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Deleted", "Student deleted successfully!")

# ======================= GUI Application ======================
class SchoolApp:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("800x500")
        
        tab_control = ttk.Notebook(self.root)
        
        self.tab_register = ttk.Frame(tab_control)
        self.tab_view = ttk.Frame(tab_control)
        
        tab_control.add(self.tab_register, text='Register Student')
        tab_control.add(self.tab_view, text='View Students')
        tab_control.pack(expand=1, fill='both')

        self.create_register_tab()
        self.create_view_tab()

    # -------------------- Register Tab --------------------
    def create_register_tab(self):
        frame = tk.LabelFrame(self.tab_register, text="Student Info", padx=10, pady=10)
        frame.pack(padx=20, pady=20)

        tk.Label(frame, text="Name:").grid(row=0, column=0, sticky='w')
        self.name_entry = tk.Entry(frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(frame, text="Age:").grid(row=1, column=0, sticky='w')
        self.age_entry = tk.Entry(frame)
        self.age_entry.grid(row=1, column=1)

        tk.Label(frame, text="Class:").grid(row=2, column=0, sticky='w')
        self.class_entry = tk.Entry(frame)
        self.class_entry.grid(row=2, column=1)

        tk.Label(frame, text="Fees Paid:").grid(row=3, column=0, sticky='w')
        self.fees_entry = tk.Entry(frame)
        self.fees_entry.grid(row=3, column=1)

        submit_btn = tk.Button(frame, text="Add Student", command=self.submit_student)
        submit_btn.grid(row=4, column=0, columnspan=2, pady=10)

    def submit_student(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        student_class = self.class_entry.get()
        fees = self.fees_entry.get()

        if name and age.isdigit() and student_class and fees.replace('.', '', 1).isdigit():
            add_student(name, int(age), student_class, float(fees))
            self.clear_entries()
            self.refresh_table()
        else:
            messagebox.showerror("Error", "Invalid input. Please check your entries.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.class_entry.delete(0, tk.END)
        self.fees_entry.delete(0, tk.END)

    # -------------------- View Tab --------------------
    def create_view_tab(self):
        self.tree = ttk.Treeview(self.tab_view, columns=("ID", "Name", "Age", "Class", "Fees"), show='headings')
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(expand=True, fill='both', padx=20, pady=20)

        delete_btn = tk.Button(self.tab_view, text="Delete Selected", command=self.delete_selected)
        delete_btn.pack(pady=10)

        self.refresh_table()

    def refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for student in fetch_students():
            self.tree.insert('', 'end', values=student)

    def delete_selected(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showwarning("Warning", "Select a student to delete.")
            return
        student_id = self.tree.item(selected)['values'][0]
        delete_student(student_id)
        self.refresh_table()

# ===================== Initialize App =======================
if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = SchoolApp(root)
    root.mainloop()
