from card_interface import CardInterface
from PyPDF2 import PdfReader
import datefinder
import re
from dateutil.parser import parse

import csv
class Amex(CardInterface):
    
    def card_type(self):
        
        return "American Express"
    
    def extract_table(self, pdf_file):
        file_name = "statement.csv"
        reader = PdfReader(pdf_file)
        print(reader)
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows([["Date","Details","amount","Currency"]])

        for i in range(1,8):
            page = reader.pages[i]
            text = page.extract_text()
            # print(text)

            date_patterns = re.finditer(r"\d\d\/\d\d\/\d\d", text)
            for dates in date_patterns:
                #start_date=dates.start()
                date=dates.group(0)
                end_date = dates.end()
                t=text[end_date:]
                match_dollar = re.search(r".*.\$\d{1,3}(?:,\d{3})*\.\d+", t)
                if match_dollar:
                    start_pos = end_date+match_dollar.start()
                    re.search(r".*.\$\d{1,3}(?:,\d{3})*\.\d+", t)
                    matched_text = match_dollar.group(0)
                    detailed_text=(text[end_date:start_pos])
                    price=(re.findall(".\$\d{1,3}(?:,\d{3})*\.\d+",match_dollar.group(0)))
                    if(price[0].strip()!='$0.00'):
                        if price[0].strip()[0]== '-':
                            final_price = price[0]
                        else:
                            price_zero=price[0]
                            final_price=price_zero[1:len(price_zero)]
                        print(f"Date: {date}, Detailed_text: {detailed_text}, Price: {final_price}")
                        with open(file_name, mode='a', newline='') as file:
                            if(detailed_text!=''):
                                writer = csv.writer(file)
                                data=[[date,detailed_text.replace("\n",""),final_price,"USD"]]
                                writer.writerows(data)
                
                # else:
                #     print("No match found")
                
            if "Total Fees forthis Period" in text:
                break

                # Core logic for amex pdf file processing
                