import PyPDF2
import docx
import re
def extract(file):
    text = ""
    extension = re.search(r"\.+[A-Za-z]*", file).group()

    match extension:
        case ".docx":
            doc = docx.Document(file)
            for para in doc.paragraphs:
                text += para.text + "\n"
            return text
        case ".pdf":
            with open(file, "rb") as f:
                pdf = PyPDF2.PdfFileReader(f)
                for page in range(pdf.getNumPages()):
                    text += pdf.getPage(page).extract_text()
            return text
        case ".txt":
            with open(file, "r") as f:
                text = f.read()
            return text
    return None