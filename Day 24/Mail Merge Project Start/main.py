# Defines the letter part to replace
PLACEHOLDER = "[name]"

# Reads the names to create letters for from the file invited_names.txt
with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

# Reads the letter from the file starting_letter.txt
with open("Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    # Creates the personalized letter for each name
    for name in names:
        # Removes new line character from the name
        name = name.strip()
        # Replaces the placeholder in the letter by the current name
        new_letter = letter_content.replace(PLACEHOLDER, name)
        # Creates the letter as a txt file
        with open(f"Output/ReadyToSend/letter_{name}.txt", mode="w") as file:
            file.write(new_letter)
