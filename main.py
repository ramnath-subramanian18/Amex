
import csv

# categories = {
#     "travel" : "travel",
#     "hertz" : "travel",
#     "alamo" : "travel",
#     "zipcar" : "travel",
#     "amazon" : "shopping",
#     "amazon.com" : "shopping",
#     "prime": "entertainment",
#     "netflix": "entertainment",
#     "hulu": "entertainment",
#     "walmart" : "groceries",
#     "costco": "groceries",
#     "supermarket": "groceries",
#     "uber": "travel",
#     "lyft": "travel",
#     "concert": "entertainment",
#     "cinemark" : "entertainment",
#     "amc" : "entertainment",
#     "spirit": "flight",
#     "airline": "flight",
    
# }

category_mapping = {
    'Groceries': ['supermarket', 'grocery', 'food', 'market', 'groceries', "walmart", "costco", "patel", "indiabazaar", "target"],
    'Utilities': ['electricity', 'water', 'gas', 'utility', 'bills'],
    'Rent': ['rent', 'landlord', 'apartment', 'lease', 'rental'],
    'Entertainment': ['movie', 'concert', 'streaming', 'entertainment', 'dining', "amc", "cinemark", "prime", 'netflix', 'hulu'],
    'Transportation': ['taxi', 'uber', 'lyft', 'gas station', 'public transport', "zipcar", "travel"],
    'Shopping': ['retail', 'shopping', 'store', 'mall', 'purchase', "amazon"],
    'Dining Out': ['restaurant', 'cafe', 'dining', 'eatery', 'takeout', "starbucks", "uber eats", ""],
    'Travel': ['hotel', 'airline', 'travel', 'lodging', 'vacation', "spirit"],
    'Healthcare': ['doctor', 'hospital', 'pharmacy', 'healthcare', 'medical', "cvs", "walgreens"],
    'Insurance': ['insurance', 'policy', 'coverage', 'premium'],
    'Investments': ['investment', 'brokerage', 'stocks', 'mutual funds', 'IRA'],
    'Income': ['salary', 'wage', 'paycheck', 'income', 'earnings'],
    'Other': ['miscellaneous', 'misc', 'uncategorized', 'other', 'general']
}

def _mapping(data: str):
    if data != None and data != "":
        all_categories = set()
        all_sub_categories = set()
        for key, value in category_mapping.items():
            category = key
            for sub_category in value:
                if sub_category in data:
                    all_categories.add(category)
                    all_sub_categories.add(sub_category)
        return all_categories, all_sub_categories

def _remove_empty_string(items):
    return [item for item in items if item != ""]

if __name__ == "__main__":
    print("Csv parser")
    file_name = "sample.csv"
    with open(file=file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data = row[1].lower()
            output = _mapping(data)
            categories = _remove_empty_string(output[0])
            sub_categories = _remove_empty_string(output[1])
            print(data, _mapping(data))
            
