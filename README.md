# Deck of cards

A very basic python example deck of cards.

Features:
- Unbox a new deck
- Shuffle
- Draw cards (sorted)
- Cards left

Basic usage:

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