from tkinter import *
import pandas
import random

# Constants that users may change as they wish
BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
LANGUAGE_FILE = "japanese_words_hiragana.csv"
LEARNING_LANGUAGE = "Hiragana"
NATIVE_LANGUAGE = "English"

# --------------------------------- SAVE DATA ------------------------------ #


def save_data():
    # Save the set to a csv file, then generate a new word.
    new_file = pandas.DataFrame(word_dictionary)
    new_file.to_csv(f"data/{LEARNING_LANGUAGE}_words_to_learn.csv", index=False)
    generate_word()


def remove_correct():
    # If the user hits the check button, remove the current card from the set, then save the set to a csv file.
    word_dictionary.remove(current_card)
    save_data()


# --------------------------------- FLIP CARDS ----------------------------- #


def flip_card():
    # Flip the card to the English equivalent of the word
    global current_card

    card_canvas.itemconfig(canvas_image, image=back_card_image)
    card_canvas.itemconfig(lang_text, text=f"{NATIVE_LANGUAGE}", fill="white")
    card_canvas.itemconfig(word_text, text=f"{current_card[NATIVE_LANGUAGE]}", fill="white")


# _________________________________ CREATE FLASH CARDS --------------------- #
# Read in a csv file.
try:
    word_file = pandas.read_csv(f"data/{LEARNING_LANGUAGE}_words_to_learn.csv")
except FileNotFoundError:
    word_file = pandas.read_csv(f"data/{LANGUAGE_FILE}")

word_dictionary = word_file.to_dict(orient="records")
current_card = {}


def generate_word():
    # Randomly generate a word from the foreign language, and flip card after 3 seconds
    global current_card, timer

    window.after_cancel(timer)

    current_card = random.choice(word_dictionary)
    language_word = current_card[LEARNING_LANGUAGE]

    card_canvas.itemconfig(canvas_image, image=front_card_image)
    card_canvas.itemconfig(lang_text, text=f"{LEARNING_LANGUAGE}", fill="black")
    card_canvas.itemconfig(word_text, text=f"{language_word}", fill="black")

    timer = window.after(3000, flip_card)


# --------------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flash Card
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")

card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = card_canvas.create_image(400, 263, image=front_card_image)

lang_text = card_canvas.create_text(400, 150, text="Language", fill="black", font=(FONT, 30, "italic"))
word_text = card_canvas.create_text(400, 263, text="Word", fill="black", font=(FONT, 40, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2)

# Right Button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_correct)
right_button.grid(row=1, column=1)

# Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=save_data)
wrong_button.grid(row=1, column=0)

# Set the timer to flip the card.
timer = window.after(3000, flip_card)

# Generate a word
generate_word()

# Main loop
window.mainloop()
