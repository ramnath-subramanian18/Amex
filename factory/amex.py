from card_interface import CardInterface
from PyPDF2 import PdfReader
import datefinder
import re
from dateutil.parser import parse
from utils.csv_utils import csv_write
import csv
class Amex(CardInterface):
    def card_type(self):
        return "American Express"
    date_pattern_exp = re.compile(r'(\d\d\/\d\d\/\d\d)', re.IGNORECASE)
    dollar_pattern_exp = re.compile(r'.*.\$\d{1,3}(?:,\d{3})*\.\d+', re.IGNORECASE)
    price_pattern_exp = re.compile(r'.\$\d{1,3}(?:,\d{3})*\.\d+', re.IGNORECASE)
    def extract_table(self, pdf_file):
        data=[]
        reader = PdfReader(pdf_file)
        for i in range(1,len(reader.pages)):
            page = reader.pages[i]
            text = page.extract_text()
            date_patterns = self.date_pattern_exp.finditer(text)
            for dates in date_patterns:
                date=dates.group(0)
                end_date = dates.end()
                t=text[end_date:]
                match_dollar=self.dollar_pattern_exp.search(t)
                if match_dollar:
                    start_pos = end_date+match_dollar.start()
                    matched_text = match_dollar.group(0)
                    detailed_text=(text[end_date:start_pos])
                    price=self.price_pattern_exp.findall(match_dollar.group(0))
                    if(price[0].strip()!='$0.00'):
                        if price[0].strip()[0]== '-':
                            final_price = price[0]
                        else:
                            price_zero=price[0]
                            final_price=price_zero[1:len(price_zero)]
                        print(f"Date: {date}, Detailed_text: {detailed_text}, Price: {final_price}")
                        if(detailed_text!=''):
                            data.append([date,detailed_text.replace("\n",""),final_price,"USD"])
            if "Total Fees forthis Period" in text:
                break
        date_lst=date.split('/')        
        file_name = "amex"+date_lst[0]+'_'+date_lst[1]+'_'+date_lst[2]+".csv"
        print(type(file_name))
        print(file_name)
        csv_write(file_name,[["Date","Details","amount","Currency"]],'w')
        csv_write(file_name,data,'a')
                