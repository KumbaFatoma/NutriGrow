import sqlite3
from tkinter import messagebox
# If you don't have reportlab installed yet, run 'pip install reportlab' in your PyCharm terminal
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from datetime import datetime

def generate_pdf_report(report_type):
    """
    Generates a structured PDF report based on the selected type: 'Weekly', 'Monthly', or 'Yearly'.
    """
    # 1. Fetch filtered data from the SQLite database
    conn = sqlite3.connect("nutrigrow.db")
    cursor = conn.cursor()

    current_year = datetime.now().year

    if report_type == "Weekly":
        # Example query: Records from the last 7 days
        cursor.execute(
            "SELECT id, full_name, location, specialization, payment_fee, status FROM farmers WHERE created_date >= date('now', '-7 days')")
        date_range_str = "Past 7 Days"
    elif report_type == "Monthly":
        # Example query: Records from the current month
        cursor.execute(
            "SELECT id, full_name, location, specialization, payment_fee, status FROM farmers WHERE strftime('%m', created_date) = strftime('%m', 'now')")
        date_range_str = datetime.now().strftime("%B %Y")
    else:  # Yearly
        cursor.execute(
            "SELECT id, full_name, location, specialization, payment_fee, status FROM farmers WHERE strftime('%Y', created_date) = strftime('%Y', 'now')")
        date_range_str = str(current_year)

    records = cursor.fetchall()

    # Calculate Summary Statistics using structural decision rules
    total_records = len(records)
    active_count = sum(1 for r in records if r[5] == 'Active')
    total_fees = sum(r[4] for r in records)

    conn.close()

    # 2. Setup PDF Document Layout
    filename = f"NutriGrow_{report_type}_Report.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []

    # Nature-themed palette styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'ReportTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=24,
        textColor=colors.HexColor("#1e4620"), spaceAfter=15
    )
    section_style = ParagraphStyle(
        'SectionHeader', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=14,
        textColor=colors.HexColor("#2a5c2d"), spaceBefore=15, spaceAfter=10
    )
    body_style = ParagraphStyle('ReportBody', parent=styles['Normal'], fontName='Helvetica', fontSize=11, leading=16)

    # 3. Add Document Contents
    story.append(Paragraph(f"NutriGrow System Report 🌿🇸🇱", title_style))
    story.append(Paragraph(f"<b>Report Type:</b> {report_type} Lifecycle Audit", body_style))
    story.append(Paragraph(f"<b>Target Window:</b> {date_range_str}", body_style))
    story.append(Paragraph(f"<b>Generated At:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", body_style))
    story.append(Spacer(1, 15))

    # 4. Add Summary Metrics Section
    story.append(Paragraph("Summary Insights 📊", section_style))
    metrics_summary = (
        f"• Consolidated Record Count: {total_records} producers matched<br/>"
        f"• Operational Deployments ('Active' Status): {active_count} farmers<br/>"
        f"• Cumulative Capitalized Sourcing Fees: Le {total_fees:,.2f}"
    )
    story.append(Paragraph(metrics_summary, body_style))
    story.append(Spacer(1, 15))

    # 5. Add Data Table
    story.append(Paragraph("Detailed Farmer Registry Ledger", section_style))

    # Table data structure initialization with column headers
    table_data = [["ID", "Farmer Name", "District", "Specialization", "Fee (Le)", "Status"]]

    for row in records:
        table_data.append([str(row[0]), row[1], row[2], row[3], f"{row[4]:.1f}", row[5]])

    # Beautiful Forest-Green Table Styling
    record_table = Table(table_data, colWidths=[30, 110, 80, 170, 70, 60])
    record_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#1e4620")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#f4f9f4")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbdcbd")),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    story.append(record_table)

    # Build Document Engine Target Output
    try:
        doc.build(story)
        messagebox.showinfo("Export Success", f"{report_type} PDF report successfully saved as '{filename}'! 📄💚")
    except Exception as e:
        messagebox.showerror("Export Error", f"Failed to build PDF binary file: {str(e)}")