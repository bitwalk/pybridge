# Deck of cards

A very basic python example deck of cards.

Features:
- Unbox a new deck
- Shuffle
- Draw cards (sorted)
- Cards left

## Basic usage (sample1.py): 

```python
from deckofcards import Deck

deck = Deck()
deck.shuffle()

print(deck.draw(5, sorted=True))
```

Output:
```bash
['♤J', '♡Q', '♡5', '♧T', '♢3']
```

## Bridge usage (sample2.py):

```python
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
```

Output:
```bash
Player1 Hand:
['♤K', '♤2', '♡A', '♡Q', '♡9', '♡6', '♧9', '♧8', '♧7', '♧6', '♧4', '♢Q', '♢9']
Player2 Hand:
['♤J', '♤T', '♤9', '♤5', '♤4', '♤3', '♡K', '♡J', '♡T', '♡7', '♧A', '♢T', '♢6']
Player3 Hand:
['♡8', '♡3', '♡2', '♧J', '♧T', '♧5', '♧3', '♧2', '♢K', '♢J', '♢8', '♢7', '♢3']
Player4 Hand:
['♤A', '♤Q', '♤8', '♤7', '♤6', '♡5', '♡4', '♧K', '♧Q', '♢A', '♢5', '♢4', '♢2']
```