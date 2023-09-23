from PyPDF2 import PdfReader
import datefinder
import re
from dateutil.parser import parse
reader = PdfReader('example2.pdf')
print(len(reader.pages))
page = reader.pages[3]
text = page.extract_text()
print(text)


date_strings = re.findall(r'\d{2}/\d{2}/\d{2}', text)
pattern_amount = r'\d{2}/\d{2}/\d{2}.*?(\$\d+\.\d{2})'
pattern_line = r'\d{2}/\d{2}/\d{2}.*?(?=\n|$)'
matches_amount = re.findall(pattern_amount, text, re.DOTALL)# match new line char as well
matches_line = re.findall(pattern_line, text)
# print((date_strings))
print(matches_amount)
print(matches_line)
print(len(matches_amount))
print(len(matches_line))
