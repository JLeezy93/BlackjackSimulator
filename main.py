import collections
import random

deck = [
    'A', 'A', 'A', 'A',
    'K', 'K', 'K', 'K',
    'Q', 'Q', 'Q', 'Q',
    'J', 'J', 'J', 'J',
    '10', '10', '10', '10',
    '9', '9', '9', '9',
    '8', '8', '8', '8',
    '7', '7', '7', '7',
    '6', '6', '6', '6',
    '5', '5', '5', '5',
    '4', '4', '4', '4',
    '3', '3', '3', '3',
    '2', '2', '2', '2'
]

# Function to calculate the odds of a blackjack hand
def blackjack_odds(hand):
    # Create a counter for the hand
    hand_counter = collections.Counter(hand)
    # Initialize variables to keep track of the number of aces and other cards
    num_aces = 0
    num_other_cards = 0
    # Iterate through the counter to count the number of aces and other cards
    for card, count in hand_counter.items():
        if card == 'A':
            num_aces += count
        else:
            num_other_cards += count
    # Initialize variables to keep track of the number of possible hand values
    num_values = 0
    # Add the number of possible values for the non-ace cards
    num_values += num_other_cards
    # Add the number of possible values for the aces
    for i in range(num_aces + 1):
        num_values += i
    # Calculate the odds of getting a blackjack
    odds = (num_values - num_other_cards) / num_values
    # Return the odds
    return odds


# Example usage
hand = ['A', 'K']
print(blackjack_odds(hand))
