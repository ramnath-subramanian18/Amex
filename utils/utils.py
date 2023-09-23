import pdfplumber
import re

_card_name_pattern = re.compile(r'(Deserve|AmericanExpress|Discover|)', re.IGNORECASE)


# read the first page of the pdf file
# and identify which type of card
def get_card(file):
    with pdfplumber.open(file) as pdf_file:
        text = pdf_file.pages[0].extract_text()
        card_names = _card_name_pattern.findall(text)
        # remove duplicates after filtering
        card_names = list(set([s.lower() for s in card_names if s != ""]))
        return card_names[0]
