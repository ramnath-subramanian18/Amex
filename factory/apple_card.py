from card_interface import CardInterface

class AppleCard(CardInterface):
    
    def card_type(self):
        return "Apple Card"
    
    def extract_table(self, pdf_file):
        # Core logic for amex pdf file processing
        pass