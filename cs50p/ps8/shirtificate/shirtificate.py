from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Times", size=40)
        self.cell(text="CS50 Shirtificate", align="c", center=True, border=1, new_y="NEXT")


pdf = PDF()
pdf.add_page()
pdf.image("shirtificate.png", x="C",)
pdf.set_font("Times", style="I", size=30)
name = input("Name: ")
pdf.cell(h=-270,text=f"{name} took CS50", align="C", center=True )
pdf.set_auto_page_break(True)
pdf.output("shirtificate.pdf")
