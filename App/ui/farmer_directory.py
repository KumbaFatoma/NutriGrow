import tkinter as tk
from tkinter import ttk


class FarmerDirectoryWorkspace(tk.Frame):
    def __init__(self, parent_frame):
        super().__init__(parent_frame, bg="#eef5ee")

        # Header Canvas Label
        header_lbl = tk.Label(
            self, text="Producer & Farmer Inspection Directory 🔍",
            font=("Helvetica", 16, "bold"), bg="#eef5ee", fg="#1b381c"
        )
        header_lbl.pack(anchor="w", padx=20, pady=15)

        # Sub-explainer text
        explainer = tk.Label(
            self,
            text="Inspect details, specialization fields, and operational fees before advancing to sourcing logs.",
            font=("Helvetica", 10, "italic"), bg="#eef5ee", fg="#555555"
        )
        explainer.pack(anchor="w", padx=20, pady=0)

        # ---- FILTER SECTION BAR ----
        filter_frame = tk.Frame(self, bg="#eef5ee")
        filter_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(filter_frame, text="Search Specialization:", bg="#eef5ee", font=("Helvetica", 10, "bold")).pack(
            side="left", padx=5)
        self.spec_entry = tk.Entry(filter_frame, font=("Helvetica", 10), width=15)
        self.spec_entry.pack(side="left", padx=5)

        tk.Label(filter_frame, text="District/Town:", bg="#eef5ee", font=("Helvetica", 10, "bold")).pack(side="left",
                                                                                                         padx=5)
        self.town_entry = tk.Entry(filter_frame, font=("Helvetica", 10), width=15)
        self.town_entry.pack(side="left", padx=5)

        search_btn = tk.Button(
            filter_frame, text="Apply Filter", bg="#2a5c2d", fg="white",
            font=("Helvetica", 9, "bold"), command=self.apply_directory_filter
        )
        search_btn.pack(side="left", padx=10)

        reset_btn = tk.Button(
            filter_frame, text="Clear", bg="#c0392b", fg="white",
            font=("Helvetica", 9, "bold"), command=self.reset_directory_data
        )
        reset_btn.pack(side="left", padx=2)

        # ---- THE INVENTORY DATA TABLE CONTAINER ----
        table_frame = tk.Frame(self, bg="white", bd=1, relief="groove")
        table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Define Spreadsheet structural layout headers (Capacity swapped for Base Fee)
        columns_definition = ("id", "name", "status", "location", "specialization", "fee")
        self.tree = ttk.Treeview(table_frame, columns=columns_definition, show="headings", selectmode="browse")

        # Assign UI titles to column fields
        self.tree.heading("id", text="Farmer ID")
        self.tree.heading("name", text="Full Name")
        self.tree.heading("status", text="Status")
        self.tree.heading("location", text="District / Town")
        self.tree.heading("specialization", text="Specialization Area")
        self.tree.heading("fee", text="Base Fee (Le)")

        # Manage widths perfectly for regular viewing window panels
        self.tree.column("id", width=70, anchor="center")
        self.tree.column("name", width=140, anchor="w")
        self.tree.column("status", width=90, anchor="center")
        self.tree.column("location", width=120, anchor="w")
        self.tree.column("specialization", width=150, anchor="w")
        self.tree.column("fee", width=110, anchor="e")

        # Add a scrolling track wheel
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # 25 Unique Datasets matching Sierra Leone regional hubs and matching exact internal database references
        self.all_farmers_dataset = [
            ("1", "Sia Sarah Kamara", "🟩 Active", "Kono District", "Cassava & Tubers", "500.00"),
            ("2", "Mohamed Bangura", "🟩 Active", "Bo Town", "Nutritional Legumes", "600.00"),
            ("3", "Alhaji Conteh", "🟨 Pending", "Kambia", "High-Yield Grains", "550.00"),
            ("4", "Fatmata Sesay", "🟩 Active", "Kenema District", "Organic Sweet Potatoes", "700.00"),
            ("5", "Emmanuel Turay", "🟥 Halted", "Makeni", "Poultry Aggregates", "450.00"),
            ("6", "Mariama Dumbuya", "🟩 Active", "Waterloo", "Leafy Vegetables", "400.00"),
            ("7", "Sahr Fofanah", "🟩 Active", "Koidu Town", "Millet & Sorghum", "650.00"),
            ("8", "Amadu Jalloh", "🟩 Active", "Kabala", "Dairy & Livestock", "800.00"),
            ("9", "Zainab Kargbo", "🟩 Active", "Port Loko", "Seed Multiplication", "520.00"),
            ("10", "Mustapha Koroma", "🟨 Pending", "Moyamba", "Ginger Processing", "480.00"),
            ("11", "Kadiatu Mansaray", "🟩 Active", "Magburaka", "Inland Valley Rice", "580.00"),
            ("12", "Findah Kanu", "🟩 Active", "Lunsar", "Groundnut Cultivation", "510.00"),
            ("13", "Samuel Conteh", "🟥 Halted", "Bonthe", "Mangrove Rice", "620.00"),
            ("14", "Rebecca Bangura", "🟩 Active", "Segbwema", "Cocoa Sourcing", "900.00"),
            ("15", "Samuel Tarawally", "🟩 Active", "Pujehun", "Oil Palm Base", "750.00"),
            ("16", "Grace Sesay", "🟨 Pending", "Tombo", "Artisanal Fish Processing", "670.00"),
            ("17", "Ibrahim Bah", "🟩 Active", "Mile 91", "Maize Production", "530.00"),
            ("18", "Kumba Fatoma", "🟩 Active", "Kailahun", "Coffee Aggregates", "880.00"),
            ("19", "Abu Bakarr Kamara", "🟩 Active", "Rokupr", "Rice Research Cultivar", "610.00"),
            ("20", "Sia Mattia", "🟩 Active", "Yengema", "Horticulture", "460.00"),
            ("21", "Marcushia Marcus-Bangura", "🟨 Pending", "Freetown", "Urban Hydroponics", "950.00"),
            ("22", "Lamin Sidibay", "🟩 Active", "Koindu", "Border Trade Produce", "720.00"),
            ("23", "Findah Samai", "🟩 Active", "Gbangbatoke", "Cassava Flour", "490.00"),
            ("24", "Hassanatu Jalloh", "🟥 Halted", "Fadugu", "Sorghum Supply", "420.00"),
            ("25", "Alusine Marah", "🟩 Active", "Kabala", "Upland Vegetables", "660.00"),
        ]

        self.populate_table_view(self.all_farmers_dataset)

    def populate_table_view(self, data_subset):
        for active_item in self.tree.get_children():
            self.tree.delete(active_item)
        for registry_entry in data_subset:
            self.tree.insert("", "end", values=registry_entry)

    def apply_directory_filter(self):
        filter_spec = self.spec_entry.get().strip().lower()
        filter_town = self.town_entry.get().strip().lower()

        filtered_results = []
        for baseline_row in self.all_farmers_dataset:
            match_spec = filter_spec in baseline_row[4].lower()
            match_town = filter_town in baseline_row[3].lower()

            if match_spec and match_town:
                filtered_results.append(baseline_row)

        self.populate_table_view(filtered_results)

    def reset_directory_data(self):
        self.spec_entry.delete(0, tk.END)
        self.town_entry.delete(0, tk.END)
        self.populate_table_view(self.all_farmers_dataset)