from deckofcards import Deck

deck = Deck()

deck.shuffle()

hands = []
players = 4
for i in range(players):
    hand = deck.draw(13, sorted=True)
    print("Player{0} Hand:".format(i+1))
    print(hand)
    hands.append(hand)