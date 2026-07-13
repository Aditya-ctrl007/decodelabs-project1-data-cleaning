"""
Generates Change_Log.pdf - the stakeholder-facing artifact documenting
what was changed in the dataset and why, as required by the brief:
"If It Isn't Documented, It Didn't Happen."
"""

import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                 Table, TableStyle, HRFlowable)

log_df = pd.read_csv("change_log.csv")

doc = SimpleDocTemplate("Change_Log.pdf", pagesize=letter,
                         topMargin=0.7 * inch, bottomMargin=0.7 * inch,
                         leftMargin=0.7 * inch, rightMargin=0.7 * inch)

styles = getSampleStyleSheet()
title_style = ParagraphStyle("TitleStyle", parent=styles["Title"],
                              textColor=colors.HexColor("#1F3B33"))
h2 = ParagraphStyle("H2", parent=styles["Heading2"],
                     textColor=colors.HexColor("#2F5D50"))
body = styles["Normal"]

story = []

story.append(Paragraph("Data Cleaning &amp; Preparation - Change Log", title_style))
story.append(Paragraph("DecodeLabs Data Analytics Internship &bull; Project 1", styles["Normal"]))
story.append(Spacer(1, 4))
story.append(HRFlowable(width="100%", color=colors.HexColor("#2F5D50")))
story.append(Spacer(1, 14))

meta = [
    ["Prepared by:", "Singh Aditya Manoj Kumar"],
    ["Dataset:", "Dataset_for_Data_Analytics.xlsx"],
    ["Records processed:", "1,200"],
    ["GitHub:", "github.com/Aditya-ctrl007"],
    ["LinkedIn:", "linkedin.com/in/singhadityamanoj"],
]
meta_table = Table(meta, colWidths=[1.6 * inch, 4.5 * inch])
meta_table.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]))
story.append(meta_table)
story.append(Spacer(1, 20))

story.append(Paragraph("Summary", h2))
story.append(Paragraph(
    "The raw dataset was audited against three data-integrity checkpoints: "
    "missing values, duplicate records, and inconsistent formatting. "
    "All identified issues were resolved and the cleaned dataset passed "
    "the verification gate with a 0% error rate on unique identifiers and "
    "date formats.", body))
story.append(Spacer(1, 16))

story.append(Paragraph("Change Register", h2))
story.append(Spacer(1, 6))

table_data = [["Change ID", "Description", "Impact", "Status"]]
for _, row in log_df.iterrows():
    table_data.append([
        row["Change ID"],
        Paragraph(row["Description"], body),
        Paragraph(row["Impact"], body),
        row["Status"],
    ])

change_table = Table(table_data, colWidths=[0.7 * inch, 2.7 * inch, 2.1 * inch, 0.7 * inch])
change_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2F5D50")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F2F7F5")]),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(change_table)
story.append(Spacer(1, 20))

story.append(Paragraph("Verification Gate Results", h2))
gate_data = [
    ["Check", "Result"],
    ["Duplicate OrderIDs", "0 (Pass)"],
    ["Incorrectly formatted dates", "0 (Pass)"],
    ["Remaining null values", "0 (Pass)"],
]
gate_table = Table(gate_data, colWidths=[3.5 * inch, 2.7 * inch])
gate_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2F5D50")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
]))
story.append(gate_table)
story.append(Spacer(1, 24))

story.append(Paragraph(
    "Conclusion: The dataset now meets the Project 2 threshold and is "
    "certified as production-ready, gold-standard data.", styles["Italic"]))

doc.build(story)
print("Change_Log.pdf generated.")
