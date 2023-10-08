# for apple card. 
from PyPDF2 import PdfReader
import re
from dateutil.parser import parse
reader = PdfReader('example3.pdf')
print(len(reader.pages))
i=0

# date_pattern = r"\d{2}/\d{2}/\d{4}"
date_pattern = r"\d{2}/\d{2}/\d{4}"  # MM/DD/YYYY
percentage_pattern = r"\d+(\.\d+)?%"  # X% or X.X%
currency_pattern = r"\$\d+(\.\d{2})?"  # $X.XX

text_pattern = r"(\d+(\.\d+)?%)"
pattern_with_text = r".*?(?:(\d{2}/\d{2}/\d{4})|(\d+(\.\d+)?%)|(\$[\d.]+)).*?"

# for page in reader.pages:
page = reader.pages[1]
text = page.extract_text()
if "Transactions" in text and "Legal" not in text:
    print(text)
    
    # TODO::
    # pattern = re.finditer(rf"({pattern_with_text})", text, re.MULTILINE)
    # # print(pattern)
    # if pattern:
    #     for p in pattern:
    #         print("Match:", p.group(0))
    # else:
    #     print("No match found.")
    
    # pattern_amount = r'\d{2}/\d{2}/\d{2}.*?(\$\d+\.\d{2})'
    # pattern_line = r'\d{2}/\d{2}/\d{2}.*?(?=\n|$)'
    # matches_amount = re.findall(pattern_amount, text, re.DOTALL)# match new line char as well
    # matches_line = re.findall(pattern_line, text)
    
else:
    print("Not processing page : ", i)
i+=1
