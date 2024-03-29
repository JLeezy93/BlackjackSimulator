import collections
import random

deck = [
    'AH', 'AD', 'AS', 'AC',
    'KH', 'KD', 'KS', 'KC',
    'QH', 'QD', 'QS', 'QC',
    'JH', 'JD', 'JS', 'JC',
    '10H', '10D', '10S', '10C',
    '9H', '9D', '9S', '9C',
    '8H', '8D', '8S', '8C',
    '7H', '7D', '7S', '7C',
    '6H', '6D', '6S', '6C',
    '5H', '5D', '5S', '5C',
    '4H', '4D', '4S', '4C',
    '3H', '3D', '3S', '3C',
    '2H', '2D', '2S', '2C'
]

card_values = [11,10,9,8,7,6,5,4,3,2]
aces = ['AH', 'AD', 'AS', 'AC']
face_cards = [
        'KH', 'KD', 'KS', 'KC',
        'QH', 'QD', 'QS', 'QC',
        'JH', 'JD', 'JS', 'JC']
#numeric_card_values
ten_val = ['10H', '10D', '10S', '10C']
nine_val = ['9H', '9D', '9S', '9C']
eight_val = ['8H', '8D', '8S', '8C']
seven_val = ['7H', '7D', '7S', '7C']
six_val = ['6H', '6D', '6S', '6C']
five_val = ['5H', '5D', '5S', '5C]
four_val = ['4H', '4D', '4S', '4C']
three_val = ['3H', '3D', '3S', '3C']
two_val = ['2H', '2D', '2S', '2C']


# Deal hand
player_hand_value = 0
player_hand_total_value = 0
player_hand = random.choices(deck, k=2)


# remove cards dealt from deck
def remove_cards_dealt():
    for cards_in_hand in player_hand:
        for card in deck:
            if card == cards_in_hand:
                deck.remove(card)

    print('Cards in deck: ' + str(len(deck)))


def hit_or_stay():
    input('Would you like to hit or stay?')
    if 'hit':
        player_hand.append(random.choice(deck))
        remove_cards_dealt()
        print(player_hand)
    else:
        # determine if blackjack or bust

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

# def blackjack_or_bust():
#     for cards_in_hand in player_hand:
#         for card in deck:
#             if card == cards_in_hand:



def assign_card_values(cards_in_hand):
    for cards_in_hand in player_hand:
        if card == aces:
            player_hand_value += 11
        elif card == face_cards:
            player_hand_value += 10
        elif card == ten_val:
            player_hand_value += 10
        elif card == nine_val:
            player_hand_value += 9
        elif card == eight_val:
            player_hand_value += 8
        elif card == seven_val:
            player_hand_value += 7
        elif card == six_val:
            player_hand_value += 6
        elif card == five_val:
            player_hand_value += 5
        elif card == four_val:
            player_hand_value += 4
        elif card == three_val:
            player_hand_value += 3
        elif card == two_val:
            player_hand_value += 2
    print(player_hand_value)




# Example usage
# hand = ['A', 'K']
# print(blackjack_odds(hand))
print(player_hand)
print('Cards in deck: ' + str(len(deck)))
remove_cards_dealt()
assign_card_values()
hit_or_stay()
