import os
import pdfplumber
import re
from amex import Amex
from deserve import Deserve
from discover import Discover


class CardFactory:
    
    _card_name_pattern = re.compile(r'(Deserve|AmericanExpress|Discover|)', re.IGNORECASE)

    def get_card(self, type):
        if type.casefold() == "AmericanExpress".casefold():
            return Amex()
        elif type.casefold() == "Deserve".casefold():
            return Deserve()
        elif type.casefold() == "Discover".casefold():
            return Discover()
        else:
            None
    
    # read the first page of the pdf file
    # and identify which type of card
    def get_card_type(self, file):
        if os.path.exists(file) and os.path.isfile(file):
            with pdfplumber.open(file) as pdf_file:
                text = pdf_file.pages[0].extract_text()
                card_names = self._card_name_pattern.findall(text)
                # remove duplicates after filtering
                card_names = list(set([s.lower() for s in card_names if s != ""]))
                return card_names[0]
        else:
            print("File does not exist")
            return None
