############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

##################### Program #####################
import random
from replit import clear
from art import logo

player_hand = []
computer_hand = []

def empty_hands():
  global player_hand
  global computer_hand

  player_hand = []
  computer_hand = []

def deal_card(hand):
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  hand.append(random.choice(cards))

def compute_score(hand):
  if 11 in hand:
    card = 0
    while sum(hand) > 21:
      if hand[card] == 11:
        hand[card] = 1
      
      card += 1
 
  return sum(hand)

def game():
  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

  if play == 'y':
    empty_hands()
    clear()
    print(logo)

    deal_card(player_hand)
    deal_card(player_hand)

    deal_card(computer_hand)
    deal_card(computer_hand)

    player_score = compute_score(player_hand)
    computer_score = compute_score(computer_hand)

    if player_score != 21 and computer_score != 21:
      another_card = True

      while another_card:
        player_score = compute_score(player_hand)
        
        print(f"Your cards: {player_hand}, your score: {player_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if player_score <= 21 and input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            deal_card(player_hand)
        else:
          another_card = False

      while computer_score < 17:
        deal_card(computer_hand)
        computer_score = compute_score(computer_hand)

      print(f"Your final hand: {player_hand}, final score: {player_score}")
      print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

      if player_score > 21:
        print("You went over. You lose 😤")
      elif computer_score > 21:
        print("Opponent went over. You win 😁")
      elif player_score > computer_score:
        print("You win 😃")
      elif player_score < computer_score:
        print("You lose 😤")
      else:
        print("Draw 🙃")

    else:
      while computer_score < 17:
        deal_card(computer_hand)
        computer_score = compute_score(computer_hand)

      print(f"Your final hand: {player_hand}, final score: {player_score}")
      print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

      if player_score == 21:
        print("Win, you have Blackjack 😱")
      elif computer_score == 21:
        print("Lose, opponent has Blackjack 😱")
    
    game()
    
game()