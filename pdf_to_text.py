from PyPDF2 import PdfReader
import datefinder
import re
from dateutil.parser import parse
reader = PdfReader('example2.pdf')
print(len(reader.pages))
page = reader.pages[3]
text = page.extract_text()
print(text)


date_patterns = re.finditer(r"\d\d\/\d\d\/\d\d", text)


