from pdf2docx import Converter

pdf_file  = r'C:\Users\Verlab\Downloads\Document1.pdf'# source file 
docx_file = r'C:\Users\Verlab\Downloads\Document1.docx'  # destination file

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()
