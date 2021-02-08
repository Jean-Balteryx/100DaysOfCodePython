from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

# ---------- READ WORDS ---------- #
try:
    to_learn_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = to_learn_data.to_dict(orient="records")


# ---------- GENERATE NEW WORD ---------- #
current_card = {}


def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


# ---------- FLIP CARD ---------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


# ---------- SAVE LEARNED WORDS ---------- #
def word_learned():
    global current_card
    words.remove(current_card)
    data = pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index=False)

    generate_word()


# ---------- UI SETUP ---------- #
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)

# Language label
language_label = Label(text="French", font=("Ariel", 40, "italic"))

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)

language_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Wrong button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(column=0, row=1)

# Right button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=word_learned)
right_button.grid(column=1, row=1)

generate_word()

window.mainloop()
