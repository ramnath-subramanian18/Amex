from card_interface import CardInterface
from PyPDF2 import PdfReader
import re
from dateutil.parser import parse
from utils.csv_utils import csv_write
class AppleCard(CardInterface):
    
    def card_type(self):
        return "Apple Card"
    date_pattern_exp = re.compile(r'(\d\d\/\d\d\/\d\d)', re.IGNORECASE)
    def extract_table(self, pdf_file):
        data=[]
        # Core logic for amex pdf file processing
        reader = PdfReader(pdf_file)
        for j in range(1,len(reader.pages)):
            page = reader.pages[j]
            text = page.extract_text()
            txt=text.split('\n')
            for i in range(len(txt)):
                date_patterns = self.date_pattern_exp.finditer(txt[i])
                for dates in date_patterns:
                    if(txt[i+4][0]=='$'):
                        lst=[txt[i],txt[i+1],txt[i+4]]
                        data.append(lst)
        date_lst=data[0][0].split('/')
        file_name = "apple"+date_lst[0]+'_'+date_lst[1]+'_'+date_lst[2]+".csv"
        csv_write(file_name,[["Date","Details","amount","Currency"]],'w')
        csv_write(file_name,data,'a')


        pass