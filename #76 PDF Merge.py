from pypdf import PdfWriter
merger = PdfWriter()

pdf_files=[r"C:\Users\Pranjul\Downloads\Mayank Aadhaar.pdf",
           r"C:\Users\Pranjul\Downloads\Mukund PAN.pdf"]
for pdf in pdf_files:
    merger.append(pdf)
merger.write(r"P:\desired_output.pdf")
merger.close()
print("Successfully Done!")