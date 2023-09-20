from PyPDF2 import PdfReader
import datefinder
import re
from dateutil.parser import parse
reader = PdfReader('example2.pdf')
# print(len(reader.pages))
page = reader.pages[2]
text = page.extract_text()
# print('first')
# print(text[229:267])
# print(text[276:335])

# Define a regular expression pattern to match dates in MM/DD/YY format
date_pattern = r'\d{2}/\d{2}/\d{2}'

# Find all matches of the date pattern in the text
date_matches = re.finditer(date_pattern, text)

# Iterate through the matches and extract the amounts for each date
for match in date_matches:
    date = match.group()
    start_position = match.end() + 1  # Move past the date and one extra character
    # Search for numeric values (amount) after the date
    amount_match = re.search(r'-?\$[\d,.]+', text[start_position:])#\$ to find the $
    amount_match_end=amount_match.end()+1+start_position
    if amount_match:
        amount = amount_match.group()
    else:
        amount = "Amount not found"
    
    print(f"Date: {date}, Amount: {amount},Text:{text[start_position:amount_match_end]}")
    # print(start_position)
    # print(amount_match_end)