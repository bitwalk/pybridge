import random

_cardValues = {
    "A" : 14,
    "K" : 13,
    "Q" : 12,
    "J" : 11,
    "T" : 10,
    "9" : 9,
    "8" : 8,
    "7" : 7,
    "6" : 6,
    "5" : 5,
    "4" : 4,
    "3" : 3,
    "2" : 2,
}

_colors = [
    "♤",
    "♡",
    "♧",
    "♢"
]

def cardValueFromCard(card):
    return card[1:]

def filterCardsOnColor(cards, color):
    # x[:1] is actually returning "♤" given "♤A"
    return list(filter(lambda x: x[:1] == color, cards))

def sortCardsByValue(cards):
    # x[1:] is actually returning "A" given "♤A"
    cards.sort(key=lambda x: _cardValues[x[1:]], reverse=True)
    return cards

class Deck:
    def __init__(self):
        self._deck = []
        self.unbox()
    
    def unbox(self):
        for color in _colors:
            for cardValue in _cardValues:
                self._deck.append("{0}{1}".format(color, cardValue))

    def shuffle(self):
        random.shuffle(self._deck)

    def cardColors(self):
        return _colors

    def cards(self):
        return self._deck

    def cardsLeft(self):
        return len(self._deck)

    def sort(self, cards):
        sortedCards = []
        for color in _colors:
            currentColor = filterCardsOnColor(cards, color)
            currentCardsSorted = sortCardsByValue(currentColor)
            if len(currentCardsSorted) > 0:
                sortedCards.extend(currentCardsSorted)
        return sortedCards

    def draw(self, amount, sorted=False):
        cardsDrawn = []
        
        cardsToDraw = amount
        if cardsToDraw > self.cardsLeft():
            cardsToDraw = self.cardsLeft()

        for i in range(cardsToDraw):
            cardsDrawn.append(self._deck.pop(0))

        if sorted:
            cardsDrawn = self.sort(cardsDrawn)

        return cardsDrawn