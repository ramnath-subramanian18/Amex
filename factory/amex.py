from card_interface import CardInterface

class Amex(CardInterface):
    
    def card_type(self):
        return "American Express"
    
    def extract_table(self, pdf_file):
        # Core logic for amex pdf file processing
        pass