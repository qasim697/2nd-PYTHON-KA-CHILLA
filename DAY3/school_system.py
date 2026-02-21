import sqlite3
from tkinter import *
from tkinter import ttk, messagebox

# --- Database Setup ---
def initialize_db():
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            grade TEXT,
            gender TEXT
        )
    """)
    conn.commit()
    conn.close()

# --- Backend Functions ---
def add_student(name, age, grade, gender):
    if name == "" or age == "" or grade == "":
        messagebox.showerror("Error", "Please fill all fields")
        return
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade, gender) VALUES (?, ?, ?, ?)", 
                   (name, age, grade, gender))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Student added successfully!")

def fetch_data():
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_student(student_id):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()

# --- UI Setup ---
class SchoolManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("800x500")

        # Variables
        self.name_var = StringVar()
        self.age_var = StringVar()
        self.grade_var = StringVar()
        self.gender_var = StringVar()

        # Title
        title = Label(self.root, text="Student Management System", font=("Arial", 20, "bold"), bg="blue", fg="white")
        title.pack(side=TOP, fill=X)

        # Input Frame
        manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="silver")
        manage_frame.place(x=20, y=70, width=300, height=400)

        Label(manage_frame, text="Name:", bg="silver").grid(row=1, column=0, pady=10, padx=5, sticky="w")
        Entry(manage_frame, textvariable=self.name_var).grid(row=1, column=1, pady=10, padx=5)

        Label(manage_frame, text="Age:", bg="silver").grid(row=2, column=0, pady=10, padx=5, sticky="w")
        Entry(manage_frame, textvariable=self.age_var).grid(row=2, column=1, pady=10, padx=5)

        Label(manage_frame, text="Grade:", bg="silver").grid(row=3, column=0, pady=10, padx=5, sticky="w")
        Entry(manage_frame, textvariable=self.grade_var).grid(row=3, column=1, pady=10, padx=5)

        Label(manage_frame, text="Gender:", bg="silver").grid(row=4, column=0, pady=10, padx=5, sticky="w")
        combo_gender = ttk.Combobox(manage_frame, textvariable=self.gender_var, state="readonly")
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, pady=10, padx=5)

        # Buttons
        btn_frame = Frame(manage_frame, bg="silver")
        btn_frame.place(x=10, y=300, width=270)
        
        Button(btn_frame, text="Add", width=10, command=self.save_data).grid(row=0, column=0, padx=5)
        Button(btn_frame, text="Delete", width=10, command=self.remove_data).grid(row=0, column=1, padx=5)
        Button(btn_frame, text="Clear", width=10, command=self.clear_fields).grid(row=0, column=2, padx=5)

        # Display Frame
        display_frame = Frame(self.root, bd=4, relief=RIDGE)
        display_frame.place(x=340, y=70, width=440, height=400)

        self.student_table = ttk.Treeview(display_frame, columns=("id", "name", "age", "grade", "gender"))
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("age", text="Age")
        self.student_table.heading("grade", text="Grade")
        self.student_table.heading("gender", text="Gender")
        self.student_table['show'] = 'headings'
        
        self.student_table.column("id", width=30)
        self.student_table.column("name", width=100)
        self.student_table.column("age", width=50)
        self.student_table.pack(fill=BOTH, expand=1)
        self.display_all()

    def save_data(self):
        add_student(self.name_var.get(), self.age_var.get(), self.grade_var.get(), self.gender_var.get())
        self.display_all()
        self.clear_fields()

    def display_all(self):
        records = fetch_data()
        self.student_table.delete(*self.student_table.get_children())
        for row in records:
            self.student_table.insert('', END, values=row)

    def remove_data(self):
        selected_item = self.student_table.focus()
        if not selected_item:
            messagebox.showwarning("Warning", "Select a student to delete")
            return
        content = self.student_table.item(selected_item)
        row = content['values']
        delete_student(row[0])
        self.display_all()

    def clear_fields(self):
        self.name_var.set("")
        self.age_var.set("")
        self.grade_var.set("")
        self.gender_var.set("")

if __name__ == "__main__":
    initialize_db()
    root = Tk()
    obj = SchoolManagement(root)
    root.mainloop()