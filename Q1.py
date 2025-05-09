class Card:
    def __init__(self, suit, rank):  # magic
        self._suit = suit
        self._rank = rank

    def __str__(self):  # magic
        return f"{self._rank}{self._suit}"

class Deck:
    def shuffle(self):  # regular method
        random.shuffle(self._deck)

class PokerHand:
    def __init__(self, deck):  # magic
        self._cards = [deck.deal() for _ in range(5)]

#__init__: used in all classes to initialize data.

#__str__ and __repr__: allow nice printing like print(Card("♠", "A")) → A♠.

#shuffle() and deal() are regular methods — you call them explicitly.