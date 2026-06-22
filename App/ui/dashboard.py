import tkinter as tk
# Connect directly to your local chart rendering engines
from App.charts.gender_chart import create_gender_chart
from App.charts.status_chart import create_status_chart


class OnboardingFrame(tk.Frame):
    """The initial welcome screen displaying project goals and SDGs."""

    def __init__(self, master, on_start_callback=None):
        super().__init__(master, bg="#f4f9f4")
        self.on_start_callback = on_start_callback

        # Welcome Header Banner
        tk.Label(
            self, text="Welcome to NutriGrow 🌿🇸🇱",
            font=("Helvetica", 22, "bold"), bg="#f4f9f4", fg="#1e4620"
        ).pack(pady=(40, 10))

        # Subtitle targeting Sustainable Development Goals (SDGs)
        tk.Label(
            self, text="Addressing Childhood Malnutrition via Sustainable Agriculture",
            font=("Helvetica", 12, "italic"), bg="#f4f9f4", fg="#555555"
        ).pack(pady=(0, 15))

        # Mission Card Description Box
        intro_text = (
            "NutriGrow is designed to optimize supply chains and manage local producer "
            "metrics across Sierra Leone. By bridging the gap between agro-producers and "
            "public health distributions, this digital tool actively aligns with UN SDG 2 (Zero Hunger) "
            "and SDG 3 (Good Health & Well-being)."
        )
        msg_label = tk.Label(
            self, text=intro_text, font=("Helvetica", 11), bg="white", fg="#333333",
            wrap=450, justify="center", bd=1, relief="solid", padx=20, pady=20
        )
        msg_label.pack(pady=15)

        # Interactive launch button to load the dashboard view
        launch_btn = tk.Button(
            self, text="📊 Enter Central Analytics Dashboard", font=("Helvetica", 11, "bold"),
            bg="#2a5c2d", fg="white", activebackground="#1e4620", activeforeground="white",
            bd=0, cursor="hand2", padx=15, pady=8,
            command=self.launch_workspace
        )
        launch_btn.pack(pady=15)

    def launch_workspace(self):
        """Triggers the dashboard loading callback sequence."""
        if self.on_start_callback:
            self.on_start_callback()


class MainDashboardWorkspace(tk.Frame):
    """The analytical workspace displaying embedded visual charts and metrics."""

    def __init__(self, master):
        super().__init__(master, bg="#eef5ee")

        tk.Label(
            self, text="Central Analytics Dashboard Matrix 📊",
            font=("Helvetica", 16, "bold"), bg="#eef5ee", fg="#1e4620"
        ).pack(anchor="w", padx=20, pady=15)

        # Counter Row Panel
        cards_frame = tk.Frame(self, bg="#eef5ee")
        cards_frame.pack(fill="x", padx=20, pady=10)

        self.create_metric_card(cards_frame, "Total Producers", "25", "#1e4620")
        self.create_metric_card(cards_frame, "Active Deployments", "18", "#2a5c2d")
        self.create_metric_card(cards_frame, "Pending Validations", "4", "#e67e22")

        # Bottom Graphic Panel Splitter
        chart_grid = tk.Frame(self, bg="#eef5ee")
        chart_grid.pack(fill="both", expand=True, padx=20, pady=10)

        # Left Panel (Gender Pie Chart)
        left_panel = tk.LabelFrame(chart_grid, text="Gender Diversification Profile", bg="white",
                                   font=("Helvetica", 10, "bold"))
        left_panel.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        create_gender_chart(left_panel)

        # Right Panel (Status Bar Chart)
        right_panel = tk.LabelFrame(chart_grid, text="Producer Status Allocation", bg="white",
                                    font=("Helvetica", 10, "bold"))
        right_panel.pack(side="right", fill="both", expand=True, padx=5, pady=5)
        create_status_chart(right_panel)

    def create_metric_card(self, parent, label_text, count_value, text_color):
        card = tk.Frame(parent, bg="white", bd=1, relief="groove", width=160, height=80)
        card.pack(side="left", padx=10, expand=True, fill="x")
        card.pack_propagate(False)

        tk.Label(card, text=label_text, font=("Helvetica", 10), bg="white", fg="#666666").pack(pady=(12, 2))
        tk.Label(card, text=count_value, font=("Helvetica", 16, "bold"), bg="white", fg=text_color).pack()