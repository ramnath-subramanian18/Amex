from card_interface import CardInterface
from PyPDF2 import PdfReader
import re
from utils.csv_utils import csv_write

def extract_text(text):
    # Define the regular expression
    #pattern = r'Total Payments and Credits\s*(.*?)\s*Total Fees for this Period'

    pattern = r'Total Payments and Credits(.*?)Total Fees for this Period'
    # Search for the pattern
    match = re.search(pattern, text)
    print("matching 1234",match)
    # Return the captured group if found
    return match.group(1).strip() if match else None
class Amex(CardInterface):
    def card_type(self):
        return "American Express"
    date_pattern_exp = re.compile(r'(\d\d\/\d\d\/\d\d)', re.IGNORECASE)
    # dollar_pattern_exp = re.compile(r'.*?\$\d{1,3}(?:,\d{3})*\.\d+', re.IGNORECASE)
    # price_pattern_exp = re.compile(r'.\$\d{1,3}(?:,\d{3})*\.\d+', re.IGNORECASE)
    def extract_table(self, pdf_file,userid,file_name_pdf):
        # print("extract_table")
        whole_text=''
        data=[]
        reader = PdfReader(pdf_file)
        #print(pdf_file.pages[2].extract_text())
        # print(reader)
        # data.append({"year":first_text[match.end():match.end()+year.end()].replace("\n", ""),"card_type":"Amex",'FilenameUserId':file_name_pdf,"Deleted":0})
        for i in range(1,len(reader.pages)):
            page = reader.pages[i]
            #print("page number",i)
            text = page.extract_text()
            whole_text+=text
        with open('output_text1.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(whole_text)
        whole_text = whole_text.replace('\n', ' ').replace('\r', ' ').strip()
        whole_text = re.sub(r'\s{2,}', ' ', whole_text)
        print("text length",len(whole_text))
        
        with open('output_text.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(whole_text)
        result=extract_text(whole_text)
        result=whole_text
        #print(result)
        date_pattern_exp = re.compile(r'(\d\d\/\d\d\/\d\d)', re.IGNORECASE)
        dollar_pattern_exp = re.compile(r'.*?\$\d{1,3}(?:,\d{3})*\.\d+', re.IGNORECASE)
        price_pattern_exp = re.compile(r'.\$\d{1,3}(?:,\d{3})*\.\d+', re.IGNORECASE)
        data=[]
        date_patterns = self.date_pattern_exp.finditer(result)
        #print(date_patterns)
        for date in date_patterns:
            print(date)
            print("next loop")
            end_date = date.end()
            #print(end_date)
            t=result[end_date:]
            match_dollar=dollar_pattern_exp.search(t)
            if match_dollar:
                if '-' not in result[match_dollar.end()+end_date-8:match_dollar.end()+end_date]:
                    #print("into if ")
                    match_dollar=dollar_pattern_exp.search(t)
                    price=price_pattern_exp.findall(match_dollar.group(0))
                    if(price[0].strip()!='$0.00'):
                        price_zero=price[0]
                        final_price=price_zero[1:len(price_zero)]
                        #month, day, year = date.split('/')

                    #print(date.group(0),result[end_date:end_date+match_dollar.end()-6],final_price,"USD")
                        month, day, year = date.group(0).split('/')
                        data.append({"Date":month+'/'+day+'/'+'20'+year,"Amount":'$'+final_price.replace('$', ''),"Details":result[end_date:end_date+match_dollar.end()-6],"Currency":"USD","Userid":userid,"Deleted":0,'FilenameUserId':file_name_pdf})
                    #date_lst=date.split('/') 
        data.append({"year":"1987","card_type":"Amex",'FilenameUserId':file_name_pdf,"Deleted":0})   
        return data