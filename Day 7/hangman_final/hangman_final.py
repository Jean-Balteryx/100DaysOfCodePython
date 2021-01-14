#Imports necessary modules
import random
import hangman_words
import hangman_art

#Picka random word from the list in the module hangman_words
chosen_word = random.choice(hangman_words.word_list)

#Retrieves length of the chosen word
word_length = len(chosen_word)

#Initializes the variable indicating when the game is over
end_of_game = False

#Initializes the counter of lives
lives = 6

#Prints the hangman logo
print(hangman_art.logo)

#Initializes the display
display = []

#Adds as many underscores as there are letters in the chosen word to the display
for _ in range(word_length):
    display += "_"

#Loops until either the player guesses the word or loses all his lives
while not end_of_game:
    #Stores the letter input by the player
    guess = input("Guess a letter: ").lower()

    #Tests if the player already guessed that letter
    if guess in display:
      print(f"You already guessed {guess}.")
    else:
      #The player didn't already guess the letter
      #Go through the letters of the chosen word to test if one of them equals the guess of the player
      for position in range(word_length):
          #Retrieves the letter at the current position in the chosen word
          letter = chosen_word[position]

          #Tests if the letter equals the guess
          if letter == guess:
              #Adds the letter to the display at the right position
              display[position] = letter

      #Tests if player is wrong
      if guess not in chosen_word:
          #Prints a message indicating the player lost a life
          print(f"You guessed {guess}, that's not in the word. You lose a life.")
          
          #Subtracts one life to the player's lives counter
          lives -= 1

          #Tests if the player has remaining lives
          if lives == 0:
              #The player has no more lives -> game ended
              end_of_game = True

              #Prints to the player that he lost
              print("You lose.")

    #Prints the display
    print(f"{' '.join(display)}")

    #Tests if player guessed all letters
    if "_" not in display:
        #Player guessed all letters -> game ended
        end_of_game = True

        #Prints to the player that he won
        print("You win.")

    #Prints the hangman matching the number of lives remaining
    print(hangman_art.stages[lives])

    