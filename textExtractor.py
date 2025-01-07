import io

import PyPDF2
import docx
import re
def extract(file):
    text = ""
    extension = findExtension(file)
    uploaded_file = io.BytesIO(file.read())
    match extension:
        case ".docx":
            doc = docx.Document(uploaded_file)
            for para in doc.paragraphs:
                text += para.text + "\n"
            return text
        case ".pdf":
            pdf = PyPDF2.PdfFileReader(uploaded_file)
            for page in range(pdf.getNumPages()):
                text += pdf.getPage(page).extract_text()
            return text
        case ".txt":
            text = uploaded_file.read()
            return text
    return None

def findExtension(file):
    return re.search(r"\.+[A-Za-z]*", file.name).group()
