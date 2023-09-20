from PyPDF2 import PdfReader
import datefinder
import re
from dateutil.parser import parse
reader = PdfReader('example2.pdf')
# print(len(reader.pages))
# page = reader.pages[4]
# text = page.extract_text()
# print(text)

for i in range(1,8):
    page = reader.pages[i]
    text = page.extract_text()
    # print(text)

    date_patterns = re.finditer(r"\d\d\/\d\d\/\d\d", text)
    for dates in date_patterns:
        start_date=dates.start()
        date=dates.group(0)
        start = dates.start()
        t=text[start:]
        match_dollar = re.search(r".*.\$\d{1,3}(?:,\d{3})*\.\d+", t)
        if match_dollar:
            start_pos = start+match_dollar.end()
            re.search(r".*.\$\d{1,3}(?:,\d{3})*\.\d+", t)
            matched_text = match_dollar.group(0)
            detailed_text=(text[start:start_pos])
            price=(re.findall(".\$\d{1,3}(?:,\d{3})*\.\d+",match_dollar.group(0)))
        else:
            print("No match found")
        if not price[0][0].isalpha():

            final_price = price[0]
        else:
            price_zero=price[0]
            final_price=price_zero[1:len(price_zero)]
        print(f"Date: {date}, Detailed_text: {detailed_text}, Price: {final_price}")
    if "Total Fees forthis Period" in text:
        break
            
