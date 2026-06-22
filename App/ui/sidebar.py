import tkinter as tk
from App.reports import generate_pdf_report


class SidebarNavigation(tk.Frame):
    def __init__(self, master, on_switch_tab_callback):
        super().__init__(master, bg="#1e4620", width=220)
        self.on_switch_tab = on_switch_tab_callback
        self.pack_propagate(False)

        # Identity Icon Section
        tk.Label(self, text="NutriGrow 🌿", font=("Helvetica", 18, "bold"), bg="#1e4620", fg="white").pack(pady=30)

        # Navigation Options
        self.create_nav_btn("📊 Dashboard Matrix", "dashboard")

        # NEW ROW ADDED HERE: Inspect Farmers directory row before log sourcing
        self.create_nav_btn("🔍 Inspect Farmers", "inspect_farmers")

        self.create_nav_btn("📅 Log Sourcing", "booking")

        # Management Report Section
        tk.Label(self, text="MANAGEMENT REPORTS", font=("Helvetica", 9, "bold"), bg="#1e4620", fg="#8eb38f").pack(
            anchor="w", padx=15, pady=(15, 5))

        self.weekly_report_btn = tk.Button(
            self, text="📄 Generate Weekly PDF", font=("Helvetica", 10, "bold"),
            bg="#1b381c", fg="#d1ebd2", activebackground="#2ecc71", activeforeground="white",
            bd=0, cursor="hand2", anchor="w", padx=10, pady=6,
            command=lambda: generate_pdf_report("Weekly")
        )
        self.weekly_report_btn.pack(fill="x", pady=4, padx=15)

        self.monthly_report_btn = tk.Button(
            self, text="📄 Generate Monthly PDF", font=("Helvetica", 10, "bold"),
            bg="#1b381c", fg="#d1ebd2", activebackground="#2ecc71", activeforeground="white",
            bd=0, cursor="hand2", anchor="w", padx=10, pady=6,
            command=lambda: generate_pdf_report("Monthly")
        )
        self.monthly_report_btn.pack(fill="x", pady=4, padx=15)

        # Exit Button Anchor
        tk.Button(self, text="🚪 Shutdown Engine", font=("Helvetica", 11, "bold"), bg="#c0392b", fg="white",
                  activebackground="#e74c3c", activeforeground="white", command=master.quit).pack(side="bottom",
                                                                                                  fill="x", pady=20,
                                                                                                  padx=15)

    def create_nav_btn(self, display_text, reference_key):
        btn = tk.Button(
            self, text=display_text, font=("Helvetica", 11, "bold"),
            bg="#2a5c2d", fg="white", activebackground="#2ecc71", activeforeground="white",
            bd=0, relief="flat", padx=8, anchor="w",
            command=lambda: self.on_switch_tab(reference_key)
        )
        btn.pack(fill="x", pady=6, padx=15)