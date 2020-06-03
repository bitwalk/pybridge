
from deckofcards import Deck

# Unbox a new deck
deck = Deck()

print("Unboxed deck:")
print(deck.cards())

# Shuffle the deck
deck.shuffle()

print("Shuffled deck:")
print(deck.cards())

# Check how many cards are in deck
print("Cards in deck:")
print(deck.cardsLeft())

# Draw first bridge player hand (sorted)
hand1 = deck.draw(13, sorted=True)

print("First hand:")
print(hand1)

# Draw second bridge player hand (sorted)
hand2 = deck.draw(13, sorted=True)

print("Second hand:")
print(hand2)

# Draw third bridge player hand (sorted)
hand3 = deck.draw(13, sorted=True)

print("Third hand:")
print(hand3)

# Draw 4th bridge player hand (sorted)
hand4 = deck.draw(13, sorted=True)

print("4th hand:")
print(hand4)

# Sanity check the deck is now empty
print("Cards in deck:")
print(deck.cardsLeft())
