import sys
import os
import tkinter as tk

# Append directory structure runtime flags to avoid environment path traces
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from App.database import initialize_db
from App.auth import AuthFrame
from App.ui.dashboard import OnboardingFrame, MainDashboardWorkspace
from App.booking import BookingWorkspace
# FIX: Explicitly import the sidebar structural engine!
from App.ui.sidebar import SidebarNavigation


class NutriGrowCoreApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("NutriGrow Digital Public Good v1.0 🌿🇸🇱")
        self.geometry("900x550")
        self.configure(bg="#f4f9f4")
        self.resizable(False, False)

        # Initialize internal storage references
        initialize_db()

        # Runtime container window setup
        self.current_window_frame = None
        self.sidebar = None
        self.workspace_area = None

        # Begin system flow at authentication gateway
        self.boot_authentication_gateway()

    def clear_active_layout_frames(self):
        """Cleans out old frames to prevent overlapping windows."""
        if self.current_window_frame:
            self.current_window_frame.destroy()
            self.current_window_frame = None
        if self.sidebar:
            self.sidebar.destroy()
            self.sidebar = None
        if self.workspace_area:
            self.workspace_area.destroy()
            self.workspace_area = None

    def boot_authentication_gateway(self):
        """Loads login/registration view."""
        self.clear_active_layout_frames()
        self.current_window_frame = AuthFrame(self, on_success_callback=self.activate_onboarding_sequence)
        self.current_window_frame.pack(fill="both", expand=True)

    def activate_onboarding_sequence(self):
        """Transition interface layer directly to structural project welcome screen."""
        self.clear_active_layout_frames()
        self.current_window_frame = OnboardingFrame(self, on_start_callback=self.load_central_workspace)
        self.current_window_frame.pack(fill="both", expand=True)

    def load_central_workspace(self):
        """Builds multi-panel interface layout including sidebar navigation controls."""
        self.clear_active_layout_frames()

        # Render Sidebar navigation controller panel on the left margin
        self.sidebar = SidebarNavigation(self, on_switch_tab_callback=self.route_workspace_view)
        self.sidebar.pack(side="left", fill="y")

        # Render primary monitoring area space frame containers on the right
        self.workspace_area = tk.Frame(self, bg="#eef5ee")
        self.workspace_area.pack(side="right", fill="both", expand=True)

        # Default initialization page target
        self.route_workspace_view("dashboard")

    def route_workspace_view(self, reference_key):
        """Switches display inside workspace area based on selection keys."""
        # Clean out old components inside workspace window view only
        for structural_widget in self.workspace_area.winfo_children():
            structural_widget.destroy()

        if reference_key == "dashboard":
            sub_interface = MainDashboardWorkspace(self.workspace_area)
            sub_interface.pack(fill="both", expand=True)

        elif reference_key == "inspect_farmers":
            # Dynamic workspace route importing your directory component grid view
            from App.ui.farmer_directory import FarmerDirectoryWorkspace
            sub_interface = FarmerDirectoryWorkspace(self.workspace_area)
            sub_interface.pack(fill="both", expand=True)

        elif reference_key == "booking":
            sub_interface = BookingWorkspace(self.workspace_area)
            sub_interface.pack(fill="both", expand=True)