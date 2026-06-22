import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


class BookingWorkspace(tk.Frame):
    def __init__(self, parent_frame):
        super().__init__(parent_frame, bg="#f4f7f4")

        # Layout Main Header Title
        title_lbl = tk.Label(
            self, text="Log Sourcing & Client Contracts 📝",
            font=("Helvetica", 16, "bold"), bg="#f4f7f4", fg="#1e4620"
        )
        title_lbl.pack(anchor="w", padx=20, pady=15)

        # Main Input Form Container Frame
        form_frame = tk.LabelFrame(self, text=" Open New Sourcing Contract ", bg="white",
                                   font=("Helvetica", 10, "bold"), fg="#1e4620")
        form_frame.pack(fill="x", padx=20, pady=10)

        # Input Widgets Configuration
        tk.Label(form_frame, text="Farmer ID Number:", bg="white", font=("Helvetica", 10)).grid(row=0, column=0,
                                                                                                padx=15, pady=15,
                                                                                                sticky="w")
        self.farmer_id_entry = tk.Entry(form_frame, font=("Helvetica", 10), width=15)
        self.farmer_id_entry.grid(row=0, column=1, padx=5, pady=15, sticky="w")

        tk.Label(form_frame, text="Client/Buyer Corporate Name:", bg="white", font=("Helvetica", 10)).grid(row=1,
                                                                                                           column=0,
                                                                                                           padx=15,
                                                                                                           pady=15,
                                                                                                           sticky="w")
        self.client_name_entry = tk.Entry(form_frame, font=("Helvetica", 10), width=35)
        self.client_name_entry.grid(row=1, column=1, padx=5, pady=15, sticky="w")

        # Added: Phone Number Field
        tk.Label(form_frame, text="Contact Phone Number:", bg="white", font=("Helvetica", 10)).grid(row=2, column=0,
                                                                                                    padx=15, pady=15,
                                                                                                    sticky="w")
        self.phone_entry = tk.Entry(form_frame, font=("Helvetica", 10), width=20)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=15, sticky="w")

        # Action Execution Submission Button
        submit_btn = tk.Button(
            form_frame, text="Execute & Register Booking 🔒", bg="#1e4620", fg="white",
            font=("Helvetica", 10, "bold"), command=self.execute_booking, width=28, height=1
        )
        submit_btn.grid(row=3, column=1, padx=5, pady=15, sticky="e")

    def is_valid_sl_number(self, phone):
        """Validates Sierra Leone phone numbers (07X/08X/03X/09X or +232)."""
        phone = phone.replace(" ", "")
        # Format 0XXXXXXXX (9 digits)
        if phone.startswith("0") and len(phone) == 9 and phone[1] in ['2', '3', '7', '8', '9']:
            return True
        # Format +232XXXXXXXXX (13 characters)
        if phone.startswith("+232") and len(phone) == 13:
            return True
        return False

    def execute_booking(self):
        f_id = self.farmer_id_entry.get().strip()
        client = self.client_name_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not f_id or not client or not phone:
            messagebox.showwarning("Incomplete Fields", "Please populate all fields (Farmer ID, Client, and Phone).")
            return

        # Validate Sierra Leone Number
        if not self.is_valid_sl_number(phone):
            messagebox.showerror("Invalid Phone Number",
                                 "Please enter a valid Sierra Leone number (e.g., 076XXXXXX or +23276XXXXXX).")
            return

        # Connect to database
        try:
            conn = sqlite3.connect("nutrigrow.db")
            cursor = conn.cursor()
        except Exception as conn_err:
            messagebox.showerror("Connection Error", f"Could not open database: {conn_err}")
            return

        dataset_lookup = [
            ("1", "Sia Sarah Kamara", "Kono District", 500.00),
            ("2", "Mohamed Bangura", "Bo Town", 600.00),
            ("3", "Alhaji Conteh", "Kambia", 550.00),
            ("4", "Fatmata Sesay", "Kenema District", 700.00),
            ("5", "Emmanuel Turay", "Makeni", 450.00),
            ("6", "Mariama Dumbuya", "Waterloo", 400.00),
            ("7", "Sahr Fofanah", "Koidu Town", 650.00),
            ("8", "Amadu Jalloh", "Kabala", 800.00),
            ("9", "Zainab Kargbo", "Port Loko", 520.00),
            ("10", "Mustapha Koroma", "Moyamba", 480.00),
            ("11", "Kadiatu Mansaray", "Magburaka", 580.00),
            ("12", "Findah Kanu", "Lunsar", 510.00),
            ("13", "Samuel Conteh", "Bonthe", 620.00),
            ("14", "Rebecca Bangura", "Segbwema", 900.00),
            ("15", "Samuel Tarawally", "Pujehun", 750.00),
            ("16", "Grace Sesay", "Tombo", 670.00),
            ("17", "Ibrahim Bah", "Mile 91", 530.00),
            ("18", "Kumba Fatoma", "Kailahun", 880.00),
            ("19", "Abu Bakarr Kamara", "Rokupr", 610.00),
            ("20", "Sia Mattia", "Yengema", 460.00),
            ("21", "Marcushia Marcus-Bangura", "Freetown", 950.00),
            ("22", "Lamin Sidibay", "Koindu", 720.00),
            ("23", "Findah Samai", "Gbangbatoke", 490.00),
            ("24", "Hassanatu Jalloh", "Fadugu", 420.00),
            ("25", "Alusine Marah", "Kabala", 660.00),
        ]

        found = False
        farmer_name, district_location, base_fee = "", "", 0.0

        for item in dataset_lookup:
            if item[0] == f_id:
                farmer_name, district_location, base_fee = item[1], item[2], item[3]
                found = True
                break

        if not found:
            messagebox.showwarning("Unknown ID", f"Farmer ID '{f_id}' not found in registry.")
            conn.close()
            return

        # Calculations
        tax_calculation = base_fee * 0.05
        final_aggregate = base_fee + tax_calculation

        # DB Insertion
        try:
            cursor.execute(
                "INSERT INTO bookings (farmer_id, client_name, booking_date) VALUES (?, ?, ?)",
                (f_id, client, "2026-06-21")
            )
            conn.commit()
        except Exception as write_err:
            messagebox.showerror("Database Error", f"Insertion failed: {write_err}")
            conn.rollback()
        finally:
            conn.close()

        # Success Message
        success_message = (
            f"Contract Registered! 🟢\n\n"
            f"Producer: {farmer_name} ({district_location})\n"
            f"Base Fee Rate: Le {base_fee:.2f}\n"
            f"Consolidated Total (with tax): Le {final_aggregate:.2f}\n\n"
            f"📢 The farmer will be contacted at {phone} shortly using registered credentials."
        )

        messagebox.showinfo("Contract Confirmed", success_message)

        # Clear fields
        self.farmer_id_entry.delete(0, tk.END)
        self.client_name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)


# Boilerplate to run the frame
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Nutrigrow System")
    app = BookingWorkspace(root)
    app.pack(fill="both", expand=True)
    root.mainloop()