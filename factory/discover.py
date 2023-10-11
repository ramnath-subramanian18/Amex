from card_interface import CardInterface
from PyPDF2 import PdfReader
import datefinder
import re
from dateutil.parser import parse
from utils.csv_utils import csv_write
from card_interface import CardInterface
import csv
class Discover(CardInterface):
    
    def card_type(self):
        return "Discover"
    year_detect_pattern=re.compile(r'.*AS OF.*',re.IGNORECASE)
    date_pattern_exp = re.compile(r'\d\d/\d\d(?!/\d\d\d\d)', re.IGNORECASE)
    dollar_pattern_exp = re.compile(r'.*.\$\d{1,3}(?:,\d{3})*\.\d+', re.IGNORECASE)
    price_pattern_exp = re.compile(r'.\$\d{1,3}(?:,\d{3})*\.\d+', re.IGNORECASE)
    
    def extract_table(self, pdf_file):
        reader = PdfReader(pdf_file)
        page = reader.pages[0]
        text = page.extract_text()
        match=self.year_detect_pattern.search(text)
        start_year=(match.group(0))[len(match.group(0))-17:len(match.group(0))-13]
        end_year=(match.group(0))[len(match.group(0))-4:len(match.group(0))]
        page = reader.pages[2]
        text = page.extract_text()
        data=[]
        date_patterns = self.date_pattern_exp.finditer(text)
        for dates in date_patterns:
            end_date_pos=dates.end()
            new_text=text[end_date_pos:len(text)]
            date=dates.group(0)
            match_dollar=self.dollar_pattern_exp.search(new_text)
            if match_dollar:
                start_pos = end_date_pos+match_dollar.end()
                matched_text = match_dollar.group(0)
                detailed_text=(text[end_date_pos:start_pos])
                price=self.price_pattern_exp.search(matched_text)
                detailed_text1=(text[end_date_pos:end_date_pos+price.start()])
                final_price=(price.group(0))
                if(start_year==end_year):
                    data.append([date+'/'+start_year,detailed_text1.split('\n')[0],final_price,"USD"])
                else:
                    if(date[0:2]=='01'):
                        data.append([date+'/'+end_year,detailed_text1.split('\n')[0],final_price,"USD"])
                    else:
                        data.append([date+'/'+start_year,detailed_text1.split('\n')[0],final_price,"USD"])
        date_lst=date.split('/') 
        file_name = "discover"+date_lst[0]+'_'+date_lst[1]+'_'+start_year+".csv"
        csv_write(file_name,[["Date","Details","amount","Currency"]],'w')
        csv_write(file_name,data,'a')