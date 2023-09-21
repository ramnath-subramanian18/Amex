import sys
sys.path.append("./factory")
from factory.card_factory import CardFactory

if __name__ == "__main__":

    file="example2.pdf"
    factory = CardFactory()
    card_type=factory.get_card_type(file)
    if card_type is not None:
        card = factory.get_card(card_type)
        if card is not None:
            print("Processing for Card type : ", card.card_type())
        else:
            print("Card type is not supported.")
            sys.exit(-1)
