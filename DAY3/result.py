import pandas as pd
from fpdf import FPDF
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class ResultPDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 15)
        self.cell(0, 10, 'OFFICIAL STUDENT REPORT CARD', 1, 1, 'C')
        self.ln(10)

class ResultApp:
    def __init__(self, root):
        self.root = root
        self.root.title("School Result Generator Pro")
        self.root.geometry("500x350")
        self.root.configure(bg="#f0f0f0")

        # UI Elements
        tk.Label(root, text="Result Card Generator", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=20)
        
        self.file_label = tk.Label(root, text="No file selected", fg="blue", bg="#f0f0f0")
        self.file_label.pack(pady=5)

        tk.Button(root, text="Step 1: Select Excel File", command=self.select_file, width=25).pack(pady=10)
        
        self.process_btn = tk.Button(root, text="Step 2: Generate PDF Cards", command=self.process_data, 
                                     state=tk.DISABLED, width=25, bg="green", fg="white")
        self.process_btn.pack(pady=10)

        self.status_label = tk.Label(root, text="", bg="#f0f0f0")
        self.status_label.pack(pady=10)

        self.selected_path = ""

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            self.selected_path = file_path
            self.file_label.config(text=os.path.basename(file_path))
            self.process_btn.config(state=tk.NORMAL)

    def calculate_grade(self, pct):
        if pct >= 80: return "A+"
        elif pct >= 70: return "A"
        elif pct >= 60: return "B"
        elif pct >= 50: return "C"
        elif pct >= 40: return "D"
        else: return "F"

    def process_data(self):
        try:
            df = pd.read_excel(self.selected_path)
            df.columns = df.columns.str.strip()
            
            # Dynamic Subject Detection
            non_subjects = ['Name', 'Roll_No']
            subjects = [col for col in df.columns if col not in non_subjects]
            
            output_dir = "Generated_Results"
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            for _, row in df.iterrows():
                pdf = ResultPDF()
                pdf.add_page()
                
                # Info
                pdf.set_font('helvetica', 'B', 12)
                pdf.cell(0, 10, f"Name: {row['Name']}", 0, 1)
                pdf.cell(0, 10, f"Roll No: {row['Roll_No']}", 0, 1)
                pdf.ln(5)

                # Table Header
                pdf.set_fill_color(230, 230, 230)
                pdf.cell(90, 10, "Subject", 1, 0, 'C', 1)
                pdf.cell(0, 10, "Marks", 1, 1, 'C', 1)

                total = 0
                for sub in subjects:
                    val = row[sub]
                    pdf.set_font('helvetica', '', 12)
                    pdf.cell(90, 10, sub, 1)
                    pdf.cell(0, 10, str(val), 1, 1, 'C')
                    total += val

                # Calculations
                max_m = len(subjects) * 100
                pct = (total / max_m) * 100
                grade = self.calculate_grade(pct)

                pdf.ln(5)
                pdf.set_font('helvetica', 'B', 12)
                pdf.cell(0, 10, f"Total: {total}/{max_m}  |  Percentage: {pct:.2f}%", 0, 1)
                pdf.cell(0, 10, f"Grade: {grade}", 0, 1)

                pdf.output(f"{output_dir}/{row['Roll_No']}_{row['Name']}.pdf")

            messagebox.showinfo("Success", f"Results generated in '{output_dir}' folder!")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ResultApp(root)
    root.mainloop()