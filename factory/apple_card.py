from card_interface import CardInterface
from PyPDF2 import PdfReader
import re
from dateutil.parser import parse
from utils.csv_utils import csv_write
#from database import insert_data
class AppleCard(CardInterface):
    
    def card_type(self):
        return "Apple Card"
    date_pattern_exp = re.compile(r'(\d\d\/\d\d\/\d\d)', re.IGNORECASE)
    def extract_table(self, pdf_file,userid,file_name_pdf):
        data=[]
        # Core logic for amex pdf file processing
        reader = PdfReader(pdf_file)
        first_page = reader.pages[0]
        first_text = first_page.extract_text()
        match = re.search("Statement", first_text)
        year=re.search(r"\b\d{4}\b", first_text[match.end():len(first_text)])
        print("total content",first_text[match.end():match.end()+year.end()].replace("\n", ""))
        
        for j in range(1,len(reader.pages)):
            page = reader.pages[j]
            text = page.extract_text()
            txt=text.split('\n')
            # sprint(txt)
            for i in range(len(txt)):
                date_patterns = self.date_pattern_exp.finditer(txt[i])
                for dates in date_patterns:
                    
                    if(txt[i+4][0]=='$'):
                        print(txt[i+4])
                        # date=txt[0]
                        lst={"Date":txt[i],"Details":txt[i+1],"Amount":'$'+txt[i+4][1:len(txt[i+4])],"Currency":"USD","Userid":userid,"Deleted":0,'FilenameUserId':file_name_pdf}
                        # lst=[txt[i],txt[i+1],txt[i+4]]
                        data.append(lst)
        

        print("apple card")
        data.append({"year":first_text[match.end():match.end()+year.end()].replace("\n", ""),"card_type":"Apple",'FilenameUserId':file_name_pdf,"Deleted":0})
        #insert_data(data,file_name_pdf)
        return data