import tkinter as tk


def create_gender_chart(parent_frame):
    """Draws a clean, native geometric pie chart."""
    canvas = tk.Canvas(parent_frame, width=180, height=180, bg="white", bd=0, highlightthickness=0)
    canvas.pack(pady=10)

    # Render Pie Wedges (48% Male, 52% Female)
    # 360 degrees * 0.48 = 172.8 degrees for Male
    canvas.create_arc(20, 20, 160, 160, start=0, extent=172.8, fill="#2a5c2d", outline="white")
    canvas.create_arc(20, 20, 160, 160, start=172.8, extent=187.2, fill="#8eb38f", outline="white")

    # Legend Labels
    legend_frame = tk.Frame(parent_frame, bg="white")
    legend_frame.pack()

    m_box = tk.Frame(legend_frame, bg="#2a5c2d", width=12, height=12)
    m_box.pack(side="left", padx=(0, 4))
    tk.Label(legend_frame, text="Male (48%)", font=("Helvetica", 9), bg="white").pack(side="left", padx=(0, 15))

    f_box = tk.Frame(legend_frame, bg="#8eb38f", width=12, height=12)
    f_box.pack(side="left", padx=(0, 4))
    tk.Label(legend_frame, text="Female (52%)", font=("Helvetica", 9), bg="white").pack(side="left")