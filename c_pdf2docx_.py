from pdf2docx import converter
pdf_file= ''
docx_file= ''
converted=converter(pdf_file)
converted.convert(docx_file)
converted.close()