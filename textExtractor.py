import PyPDF2
def extract(file):
    """
    Extracts the text from a PDF file.
    """
    text = ""

    if file.endswith(".pdf"):
        with open(file, "rb") as f:
            pdf = PyPDF2.PdfFileReader(f)
            for page in range(pdf.getNumPages()):
                text += pdf.getPage(page).extract_text()
    elif file.endswith(".txt") || file.endswith(".docx"):
        with open(file, "r") as f:
            text = f.read()
