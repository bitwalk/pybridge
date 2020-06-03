from deckofcards import Deck

deck = Deck()
deck.shuffle()

print(deck.draw(5, sorted=True))
