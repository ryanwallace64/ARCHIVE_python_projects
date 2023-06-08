import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def starting_cards():
    '''Deals two cards to player and dealer'''
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))

def total_score(hand):
    '''Returns total score for all cards in list of input argument'''
    total = 0
    for card in hand:
        total += card
    return total

def deal_card(player):
    '''Deals a new card to input argument'''
    player.append(random.choice(cards))
                  
def blackjack():
    '''Play Blackjack!'''
    starting_cards()
    
    another_card = True
    while another_card:
        player_score = total_score(player_cards)
        dealer_score = total_score(dealer_cards)    
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")
        
        if input("Type 'y' to get another card, type 'n' to pass: ") == "n":
            another_card = False
        else:
            deal_card(player_cards)
            if total_score(player_cards) > 21:
                player_score = total_score(player_cards)
                another_card = False

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    
    if player_score > 21:
        print("You busted. You lose!")
    elif player_score == dealer_score:
        print("Draw!")
    elif player_score > dealer_score:
        print("You win!")
    else:
        print("You lose!")


should_continue = True
while should_continue:
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0
    
    blackjack() 
    
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'n':
        should_continue = False      
        print("Thanks for playing!")