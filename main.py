from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
LANGUAGE_FILE = "japanese_words_hiragana.csv"
LEARNING_LANGUAGE = "Hiragana"
NATIVE_LANGUAGE = "English"
MAX_INDEX = 17

# _________________________________ CREATE FLASH CARDS --------------------- #
word_file = pandas.read_csv(f"data/{LANGUAGE_FILE}")
word_dictionary = word_file.to_dict()


def generate_word():
    language = LEARNING_LANGUAGE
    word_choice = random.randint(0, len(word_dictionary[LEARNING_LANGUAGE]) - 1)
    language_word = word_dictionary[LEARNING_LANGUAGE][word_choice]

    card_canvas.itemconfig(lang_text, text=f"{language}")
    card_canvas.itemconfig(word_text, text=f"{language_word}")
    pass


# --------------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flash Card Front
front_card_image = PhotoImage(file="images/card_front.png")
card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_canvas.create_image(400, 263, image=front_card_image)
lang_text = card_canvas.create_text(400, 150, text="Language", fill="black", font=(FONT, 40, "italic"))
word_text = card_canvas.create_text(400, 263, text="Word", fill="black", font=(FONT, 60, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2)

generate_word()

# Right Button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=generate_word)
right_button.grid(row=1, column=1)

# Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)

window.mainloop()
