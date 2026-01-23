from fpdf import FPDF
import glob
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob("files/*.txt")

# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each text file
for filepath in filepaths:
    # Add a page to the PDF document for each text file
    pdf.add_page()

    # Get the filename without the extension
    # and convert it to title case (e.g. Cat)
    filename = Path(filepath).stem
    name = filename.title()
    desc = Path(filepath).read_text()

    # Add the name to the PDF
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=name, ln=1)

    # Add the description to the PDF
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=8, txt=desc)

# Produce the PDF
pdf.output("output.pdf")
