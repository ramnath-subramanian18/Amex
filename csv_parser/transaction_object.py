class Transaction:

    def __init__(self, row_no, date, full_details, amount, currency) -> None:
        self.row_no = row_no
        self.date = date
        self.full_details = full_details
        self.amount = amount
        self.currency = currency
        self.category = set()
        self.sub_category = set()
    
    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_full_details(self):
        return self._full_details

    def set_full_details(self, full_details):
        self._full_details = full_details

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount

    def get_currency(self):
        return self._currency

    def set_currency(self, currency):
        self._currency = currency

    def get_category(self):
        return self._category

    def set_category(self, category):
        self._category = category
    
    def get_sub_category(self):
        return self.sub_category

    def set_sub_category(self, sub_category):
        self.sub_category = sub_category