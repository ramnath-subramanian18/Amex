import sys
sys.path.append("./factory")
from factory.card_factory import CardFactory

if __name__ == "__main__":

    file="example3.pdf"
    factory = CardFactory()
    card_type=factory.get_card_type(file)
    print(card_type)
    if card_type is not None:
        card = factory.get_card(card_type)
        if card is not None:
            print("Processing for Card type : %s " %(card.card_type()))
        else:
            print("Card type %s is not supported.", card.card_type())
            sys.exit(-1)
        card.extract_table(file)
    #csv_extract_table=factory.get_extract_table(file)

