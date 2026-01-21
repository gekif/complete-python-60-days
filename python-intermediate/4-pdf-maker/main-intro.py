from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Times",
             style="B", size=12)
pdf.cell(w=10, h=24, txt="Hello There!",
         align="L", ln=1)

pdf.set_font(family="Times",
             style="B", size=10)
pdf.cell(w=0, h=12, txt="Hi There!",
         align="L", ln=1)

if pdf:
    pdf.output("output.pdf")
    print("PDF generated successfully.")
