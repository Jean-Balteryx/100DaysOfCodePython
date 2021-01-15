#Imports the ASCII logo from the module art
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Defines the function caesar() that encodes or decodes a text
def caesar(start_text, shift, cipher_direction):

  #Initializes the result text
  end_text = ""

  #Negates the shift if it's a decoding
  if cipher_direction == "decode":
    shift *= -1

  #Goes through the letters of the text and transforms them
  for char in start_text:
    #Tests if the current character is a letter
    if char in alphabet:
      #The current character is a letter

      #Gets the position in the alphabet of the current letter
      position = alphabet.index(char)

      #Applies the shift to the position to get the position of the new letter
      new_position = (position + shift) % 26

      #Adds the new letter to the transformed text
      end_text += alphabet[new_position]
    else:
      #The current character is not a letter so no transformation
      end_text += char
    
  #Prints the result
  print(f"Here's the {cipher_direction}d result: {end_text}")

#Defines the function start() that starts the program and run it again if the user want to do so
def start():

  #Asks the user the direction of the program (cipher, decipher), the text to transform and the shift
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #Calls the caesar() function with user's inputs as arguments
  caesar(start_text = text, shift = shift, cipher_direction = direction)

  #Asks the user if he want to run the program again
  again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

  #Tests whether the user wants to run the program again
  if again == 'yes':
    #The user wants to run the program again

    #Calls the function itself
    start()
  else:
    #The user doesn't want to run the program again
    print("Goodbye!")


#Prints the logo
print(logo) 

#Calls the function start
start()

