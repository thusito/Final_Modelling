# Poker simulation – Full-House probability
import random
from collections import Counter
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output

# ---------- Card & Deck (no external import needed) ----------
class Card:
    ranks = list(range(2, 15))          # 2-10, J=11, Q=12, K=13, A=14
    suits = '♠♥♦♣'

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        rank_str = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}.get(self.rank, str(self.rank))
        return f'{rank_str}{self.suit}'


class Deck:
    def __init__(self):
        self.cards = [Card(r, s) for r in Card.ranks for s in Card.suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n=5):
        return [self.cards.pop() for _ in range(n)]


# ---------- Helper to detect a Full House ----------
def is_full_house(hand):
    """
    True if hand has three cards of one rank and two of another.
    """
    counts = Counter(card.rank for card in hand).values()
    return sorted(counts) == [2, 3]


# ---------- Simulation core ----------
def run_sim(iterations):
    """
    Run <iterations> five-card deals.
    Returns a list with the running probability (%) after each draw.
    """
    full_house = 0
    probs = []
    for i in range(1, iterations + 1):
        deck = Deck()
        deck.shuffle()
        hand = deck.deal(5)
        if is_full_house(hand):
            full_house += 1
        probs.append(100 * full_house / i)      # running probability %
    return probs


# ---------- Plot & UI ----------
def simulate_and_plot(iterations):
    probs = run_sim(iterations)

    plt.figure(figsize=(8, 5))
    plt.plot(range(1, iterations + 1), probs)
    plt.xlabel('Number of draws')
    plt.ylabel('Full House probability (%)')
    plt.title('Convergence of Full House probability')
    plt.grid(True, alpha=0.3)
    plt.show()

    print(f'Final estimate after {iterations:,} draws: {probs[-1]:.4f}%')


iter_slider = widgets.IntSlider(
    value=1000, min=1000, max=50000, step=100,
    description='Iterations:', continuous_update=False
)

def on_change(change):
    clear_output(wait=True)
    display(iter_slider)
    simulate_and_plot(change['new'])

iter_slider.observe(on_change, names='value')

display(iter_slider)            # show the slider
simulate_and_plot(iter_slider.value)   # initial run
