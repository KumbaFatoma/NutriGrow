import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class LineGraphChart(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")

        # Tracking trends up to Farmer ID 25
        data_points = [1, 5, 10, 15, 20, 25]
        fee_trends = [500, 450, 480, 750, 460, 660]

        fig, ax = plt.subplots(figsize=(7, 2.5))
        ax.plot(data_points, fee_trends, marker='o', color='#1e4620', linewidth=2, markersize=5)

        ax.set_title("Fee Rate Horizon Trend (Le)", fontname="Helvetica", fontsize=11, fontweight="bold", pad=8)
        ax.set_xlabel("Farmer ID Sequence Range", fontsize=9)
        ax.set_ylabel("Leones (Base)", fontsize=9)
        ax.tick_params(axis='both', labelsize=8)
        ax.grid(True, linestyle=':', alpha=0.6)

        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        plt.close(fig)