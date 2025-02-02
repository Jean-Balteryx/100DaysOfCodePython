import pandas

# Creates a dictionary of NATO alphabet from csv file
nato_alphabet = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


# Creates a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        phonetic_words = [nato_alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_words)


generate_phonetic()
