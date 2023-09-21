from abc import ABC, abstractmethod

class CardInterface(ABC):

    @abstractmethod
    def card_type(self):
        pass

    @abstractmethod
    def extract_table(self, pdf_file):
        pass