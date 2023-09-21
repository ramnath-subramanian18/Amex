from card_interface import CardInterface

class Discover(CardInterface):
    
    def card_type(self):
        return "Discover"
    
    def extract_table(self, pdf_file):
        # Core logic for Discover pdf file processing
        pass