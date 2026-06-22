import tkinter as tk


def create_status_chart(parent_frame):
    """Draws a clean vertical column bar chart."""
    canvas = tk.Canvas(parent_frame, width=180, height=180, bg="white", bd=0, highlightthickness=0)
    canvas.pack(pady=10)

    # Base baseline axis line
    canvas.create_line(20, 150, 170, 150, fill="#cccccc", width=1)

    # Bar 1: Active (Height corresponds to data value 14)
    canvas.create_rectangle(35, 40, 65, 150, fill="#1e4620", outline="")
    canvas.create_text(50, 25, text="18", font=("Helvetica", 9, "bold"), fill="#1e4620")

    # Bar 2: Pending (Height corresponds to data value 3)
    canvas.create_rectangle(80, 110, 110, 150, fill="#e67e22", outline="")
    canvas.create_text(95, 95, text="4", font=("Helvetica", 9, "bold"), fill="#e67e22")

    # Bar 3: Inactive (Height corresponds to data value 3)
    canvas.create_rectangle(125, 120, 155, 150, fill="#95a5a6", outline="")
    canvas.create_text(140, 105, text="3", font=("Helvetica", 9, "bold"), fill="#95a5a6")

    # Labels row
    legend = tk.Frame(parent_frame, bg="white")
    legend.pack()
    tk.Label(legend, text="🟢 Act  |  🟠 Pend  |  ⚪ Inact", font=("Helvetica", 9), bg="white", fg="#555555").pack()