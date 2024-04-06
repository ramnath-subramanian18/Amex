from card_interface import CardInterface
from PyPDF2 import PdfReader
import re
from dateutil.parser import parse
from utils.csv_utils import csv_write
from database import insert_data
class AppleCard(CardInterface):
    
    def card_type(self):
        return "Apple Card"
    date_pattern_exp = re.compile(r'(\d\d\/\d\d\/\d\d)', re.IGNORECASE)
    def extract_table(self, pdf_file,userid,file_name_pdf):
        data=[]
        # Core logic for amex pdf file processing
        reader = PdfReader(pdf_file)
        for j in range(1,len(reader.pages)):
            page = reader.pages[j]
            text = page.extract_text()
            txt=text.split('\n')
            # sprint(txt)
            for i in range(len(txt)):
                date_patterns = self.date_pattern_exp.finditer(txt[i])
                for dates in date_patterns:
                    
                    if(txt[i+4][0]=='$'):
                    
                        # date=txt[0]
                        lst={"Date":txt[i],"Details":txt[i+1],"Amount":txt[i+4],"Currency":"USD","Userid":userid,"Deleted":0,'FilenameUserId':file_name_pdf}
                        print(lst)
                        # lst=[txt[i],txt[i+1],txt[i+4]]
                        data.append(lst)
        print("date",data[0]['Date'])
        date_lst=data[0]['Date'].split('/')
        print(date_lst)
        file_name = "apple"+date_lst[0]+'_'+date_lst[1]+'_'+date_lst[2]+".csv"
        print(file_name)
        csv_write(file_name,[["Date","Details","amount","Currency"]],'w')
        csv_write(file_name,data,'a')

        print("apple card")
        insert_data(data,file_name_pdf)
        return data
        pass