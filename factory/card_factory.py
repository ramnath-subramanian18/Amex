import re
from amex import Amex
from deserve import Deserve
from discover import Discover
from apple_card import AppleCard
import sys
sys.path.append("../utils")

# from ..utils import get_card
# import sys
# sys.path.append("../utils")

# import utils

class CardFactory:
    
    _card_name_pattern = re.compile(r'(Deserve|AmericanExpress|Discover|Apple Card Customer)', re.IGNORECASE)

    def get_card(self, type):
        if type.casefold() == "AmericanExpress".casefold():
            return Amex()
        elif type.casefold() == "Deserve".casefold():
            return Deserve()
        elif type.casefold() == "Discover".casefold():
            return Discover()
        elif type.casefold() == "Apple Card Customer".casefold():
            return AppleCard()
        else:
            None
    
    # read the first page of the pdf file
    # and identify which type of card
    def get_card_type(self, file):
        # if os.path.exists(file) and os.path.isfile(file):
        #     print("inside if")
        #     with pdfplumber.open(file) as pdf_file:
        #         print("into with")
        text = file
        card_names = self._card_name_pattern.findall(text)
        # remove duplicates and empty string after filtering
        card_names = list(set([s.lower() for s in card_names if s != ""]))
        if len(card_names) == 0:
            print("into if loop")
            return 'Unknown card', 400 
        else:
            return card_names[0]
        # else:
        #     print("File does not exist")
        #     return None