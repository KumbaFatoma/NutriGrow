import sqlite3


def get_db_connection():
    # This creates or connects to the main database file
    return sqlite3.connect("nutrigrow.db")


def initialize_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Create Users Table (Handles Login & Registration)
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       username
                       TEXT
                       UNIQUE
                       NOT
                       NULL,
                       password
                       TEXT
                       NOT
                       NULL
                   )
                   ''')

    # 2. Create Farmers Table (With local Sierra Leonean context)
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS farmers
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       full_name
                       TEXT
                       NOT
                       NULL,
                       gender
                       TEXT
                       NOT
                       NULL,
                       location
                       TEXT
                       NOT
                       NULL,
                       town
                       TEXT
                       NOT
                       NULL,
                       specialization
                       TEXT
                       NOT
                       NULL,
                       payment_fee
                       REAL
                       NOT
                       NULL,
                       status
                       TEXT
                       NOT
                       NULL,
                       created_date
                       DATE
                       NOT
                       NULL
                   )
                   ''')

    # 3. Create Bookings Table (For matching and logging requests)
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS bookings
                   (
                       id
                       INTEGER
                       PRIMARY
                       KEY
                       AUTOINCREMENT,
                       farmer_id
                       INTEGER,
                       client_name
                       TEXT
                       NOT
                       NULL,
                       booking_date
                       DATE
                       NOT
                       NULL,
                       status
                       TEXT
                       DEFAULT
                       'Pending',
                       FOREIGN
                       KEY
                   (
                       farmer_id
                   ) REFERENCES farmers
                   (
                       id
                   )
                       )
                   ''')

    conn.commit()

    # 4. Automatically seed the database with 20 mandatory local records if empty
    cursor.execute("SELECT COUNT(*) FROM farmers")
    if cursor.fetchone()[0] == 0:
        seed_data = [
            ("Sia Sarah Kamara", "Female", "Kono", "District", "Cassava & Tubers", 500.0, "Active", "2026-01-15"),
            ("Mohamed Bangura", "Male", "Bo", "Town", "Nutritional Legumes", 600.0, "Active", "2026-01-15"),
            ("Alhaji Conteh", "Male", "Kambia", "District", "High-Yield Grains", 550.0, "Pending", "2026-01-15"),
            ("Fatmata Sesay", "Female", "Kenema", "District", "Organic Sweet Potatoes", 700.0, "Active", "2026-02-10"),
            ("Emmanuel Turay", "Male", "Makeni", "District", "Poultry Aggregates", 450.0, "Active", "2026-03-01"),
            ("Mariama Dumbuya", "Female", "Waterloo", "Town", "Leafy Vegetables", 400.0, "Active", "2026-03-12"),
            ("Sahr Fofanah", "Male", "Koidu", "Town", "Millet & Sorghum", 650.0, "Active", "2026-01-15"),
            ("Amadu Jalloh", "Male", "Kabala", "District", "Diary & Livestock", 800.0, "Active", "2026-01-15"),
            ("Zainab Kargbo", "Female", "Port Loko", "District", "Seed Multiplication", 520.0, "Active", "2026-04-18"),
            ("Mustapha Koroma", "Male", "Moyamba", "District", "Ginger Procesing", 480.0, "Pending", "2026-05-02"),
            ("Kadiatu Mansaray", "Female", "Tonkolili", "Magburaka", "Inland Valley Rice", 580.0, "Active", "2026-05-20"),
            ("Findah Kanu", "Female", "Port Loko", "Lunsar", "Groundnut Cultivation", 510.0, "Active", "2026-05-20"),
            ("Samuel Conteh", "Male", "Bonthe", "Mattru Jong", "Mangrove Rice", 620.0, "Inactive", "2026-06-01"),
            ("Rebecca Bangura", "Female", "Segbwema", "District", "Cocoa Sourcing", 900.0, "Inactive", "2026-06-05"),
            ("Samuel Tarawally", "Male", "Pujehun", "Zimmi", "Oil Palm Base", 750.0, "Active", "2026-06-08"),
            ("Grace Sesay", "Female", "Tombo", "Town", "Artisanal Fish Processing", 670.0, "Pending", "2026-06-10"),
            ("Ibrahim Bah", "Male", "Mile 91", "District", "Maize Production", 530.0, "Active", "2026-06-14"),
            ("Kumba Fatoma", "Female", "Kailahun", "Boidu", "Coffee Aggregates", 880.0, "Pending", "2026-06-12"),
            ("Abu Bakarr Kamara", "Male", "Kambai", "Rokupr", "Rice Research Cultivar", 610.0, "Active", "2026-06-14"),
            ("Sia Miatta", "Female", "Kono", "Yengema", "Horticulture", 460.0, "Active", "2026-06-15"),
            ("Marcushia Marcus-Bangura", "Female", "Western-Area", "Freetown", "Urban Hydroponics", 950.0, "Pending", "2026-06-21"),
            ("Lamin Sidibay", "Male", "Koindu", "District", "Border Trade Produce", 720.0, "Active", "2026-06-18"),
            ("Findah Samai", "Female", "Gbangbatoke", "District", "Cassava Flour", 490.0, "Active", "2026-06-19"),
            ("Hassnatu Jalloh", "Female", "Koinadugu", "Fadugu", "Sorghum Supply", 420.0, "Inactive", "2026-06-21"),
            ("Alusine Marrah", "Male", "Kabala", "District", "Upland Vegetbles", 660.0, "Active", "2026-06-20"),
        ]
        cursor.executemany('''
                           INSERT INTO farmers (full_name, gender, location, town, specialization, payment_fee, status,
                                                created_date)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                           ''', seed_data)
        conn.commit()

    conn.close()