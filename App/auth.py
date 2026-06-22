import tkinter as tk
from tkinter import messagebox
import sqlite3


class AuthFrame(tk.Frame):
    def __init__(self, master, on_success_callback):
        super().__init__(master, bg="#f4f9f4")
        self.on_success_callback = on_success_callback
        self.is_login_mode = True

        # Heading Style
        self.title_lbl = tk.Label(self, text="NutriGrow Portal 🌿💚", font=("Helvetica", 22, "bold"), bg="#f4f9f4",
                                  fg="#1e4620")
        self.title_lbl.pack(pady=(60, 10))

        self.subtitle_lbl = tk.Label(self, text="Sign in to manage your public health distributions",
                                     font=("Helvetica", 11), bg="#f4f9f4", fg="#555555")
        self.subtitle_lbl.pack(pady=(0, 30))

        # Fields
        tk.Label(self, text="Username:", font=("Helvetica", 10, "bold"), bg="#f4f9f4", fg="#1e4620").pack(anchor="w",
                                                                                                          padx=100)
        self.username_entry = tk.Entry(self, font=("Helvetica", 12), width=30)
        self.username_entry.pack(pady=(5, 15))

        tk.Label(self, text="Password:", font=("Helvetica", 10, "bold"), bg="#f4f9f4", fg="#1e4620").pack(anchor="w",
                                                                                                          padx=100)
        self.password_entry = tk.Entry(self, font=("Helvetica", 12), show="*", width=30)
        self.password_entry.pack(pady=(5, 25))

        # Dynamic Action Button
        self.submit_btn = tk.Button(self, text="Login ➡️", font=("Helvetica", 11, "bold"), bg="#1e4620", fg="white",
                                    width=15, command=self.process_auth)
        self.submit_btn.pack(pady=10)

        # Mode Changer Switch
        self.toggle_btn = tk.Button(self, text="New User? Register Account 🌱", font=("Helvetica", 9, "underline"),
                                    bg="#f4f9f4", fg="#1e4620", bd=0, cursor="hand2", command=self.toggle_mode)
        self.toggle_btn.pack(pady=5)

    def toggle_mode(self):
        self.is_login_mode = not self.is_login_mode
        if self.is_login_mode:
            self.title_lbl.configure(text="NutriGrow Portal 🌿💚")
            self.submit_btn.configure(text="Login ➡️")
            self.toggle_btn.configure(text="New User? Register Account 🌱")
        else:
            self.title_lbl.configure(text="Join NutriGrow 🌱🌾")
            self.submit_btn.configure(text="Register 🤝")
            self.toggle_btn.configure(text="Have an account? Login here")

    def process_auth(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showwarning("Incomplete", "Both configuration fields are mandatory! ⚠️")
            return

        conn = sqlite3.connect("nutrigrow.db")
        cursor = conn.cursor()

        if self.is_login_mode:
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            if cursor.fetchone():
                conn.close()
                self.on_success_callback()
            else:
                messagebox.showerror("Error", "Invalid user credential pairing. ❌")
        else:
            try:
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Account established successfully! 🌱")
                self.on_success_callback()
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "Username has already been chosen. ⚠️")
        conn.close()