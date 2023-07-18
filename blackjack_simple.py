import random

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = 0
    has_ace = False
    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            value += 11
            has_ace = True
        else:
            value += int(card)
    
    if has_ace and value > 21:
        value -= 10
    
    return value

def deal_card():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def play_game():
    print("Welcome to Blackjack!")
    
    # Deal initial cards
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    
    # Print player's hand and dealer's upcard
    print("Your hand:", player_hand)
    print("Dealer's upcard:", dealer_hand[0])
    
    # Player's turn
    while True:
        choice = input("Do you want to hit or stand? ")
        if choice.lower() == 'hit':
            player_hand.append(deal_card())
            print("Your hand:", player_hand)
            if calculate_hand_value(player_hand) > 21:
                print("Bust! You lose.")
                return
        elif choice.lower() == 'stand':
            break
    
    # Dealer's turn
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card())
    print("Dealer's hand:", dealer_hand)
    
    # Determine the winner
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    if dealer_value > 21:
        print("Dealer busts! You win.")
    elif player_value > dealer_value:
        print("You win.")
    elif player_value < dealer_value:
        print("You lose.")
    else:
        print("It's a tie.")
    
    # Play again?
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() == 'yes':
        play_game()
    else:
        print("Thank you for playing!")

# Start the game
play_game()
