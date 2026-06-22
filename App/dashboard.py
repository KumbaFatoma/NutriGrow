import tkinter as tk
import sqlite3


class OnboardingFrame(tk.Frame):
    def __init__(self, master, on_next_callback):
        super().__init__(master, bg="#f4f9f4")
        self.on_next_callback = on_next_callback

        tk.Label(self, text="Welcome to NutriGrow! 🌿🇸🇱", font=("Helvetica", 24, "bold"), bg="#f4f9f4",
                 fg="#1e4620").pack(pady=(40, 20))

        description_text = (
            "NutriGrow is a software solution serving as a Digital Public Good to address\n"
            "childhood malnutrition across regional communities in Sierra Leone.\n\n"
            "By streamlining communication pathways with localized farmers, public health planners\n"
            "can coordinate and acquire biofortified crops to satisfy foundational goals\n"
            "aligned directly with SDG 2 (Zero Hunger) targets."
        )

        tk.Label(self, text=description_text, font=("Helvetica", 13, "italic"), bg="#f4f9f4", fg="#2c3e50",
                 justify="center").pack(pady=20)

        # Mission Points Table layout
        points_frame = tk.Frame(self, bg="#e2efe2", padx=20, pady=20, bd=1, relief="groove")
        points_frame.pack(pady=15)

        tk.Label(points_frame, text="💚 SDG 2 Integration: Direct alignment with Zero Hunger metrics.",
                 font=("Helvetica", 11), bg="#e2efe2", fg="#1e4620").pack(anchor="w", pady=4)
        tk.Label(points_frame, text="🌱 Direct Sourcing: Transparent payment requirements for smallholder farmers.",
                 font=("Helvetica", 11), bg="#e2efe2", fg="#1e4620").pack(anchor="w", pady=4)
        tk.Label(points_frame, text="📊 Quantified Analysis: Automated chart rendering and PDF exports.",
                 font=("Helvetica", 11), bg="#e2efe2", fg="#1e4620").pack(anchor="w", pady=4)

        tk.Button(self, text="Enter System Dashboard ➡️", font=("Helvetica", 12, "bold"), bg="#1e4620", fg="white",
                  padx=15, pady=5, command=self.on_next_callback).pack(pady=30)


class MainDashboardWorkspace(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")

        header = tk.Label(self, text="NutriGrow Central Command Matrix 📊🌱", font=("Helvetica", 18, "bold"), bg="white",
                          fg="#1e4620")
        header.pack(pady=15, anchor="w", padx=20)

        # Data presentation viewport
        self.display_scroll = tk.Text(self, font=("Courier", 10), bg="#f9fbf9", bd=1, relief="sunken")
        self.display_scroll.pack(fill="both", expand=True, padx=20, pady=10)
        self.load_table_records()

    def load_table_records(self):
        self.display_scroll.delete("1.0", tk.END)
        conn = sqlite3.connect("nutrigrow.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, full_name, district, specialization, payment_fee, status FROM farmers")
        records = cursor.fetchall()
        conn.close()

        template_header = f"{'ID':<4} | {'Farmer Name':<20} | {'District':<15} | {'Specialization':<30} | {'Fee (Le)':<10} | {'Status':<10}\n"
        divider = "-" * 98 + "\n"

        self.display_scroll.insert(tk.END, template_header)
        self.display_scroll.insert(tk.END, divider)

        for row in records:
            row_str = f"{row[0]:<4} | {row[1]:<20} | {row[2]:<15} | {row[3]:<30} | Le {row[4]:<7.1f} | {row[5]:<10}\n"
            self.display_scroll.insert(tk.END, row_str)