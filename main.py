from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
LANGUAGE_FILE = "japanese_words_hiragana.csv"
LEARNING_LANGUAGE = "Hiragana"
NATIVE_LANGUAGE = "English"
MAX_INDEX = 17
current_card = {}

# --------------------------------- FLIP CARDS ----------------------------- #


def flip_card():
    global current_card

    card_canvas.itemconfig(canvas_image, image=back_card_image)
    card_canvas.itemconfig(lang_text, text=f"{NATIVE_LANGUAGE}", fill="white")
    card_canvas.itemconfig(word_text, text=f"{current_card[NATIVE_LANGUAGE]}", fill="white")


# _________________________________ CREATE FLASH CARDS --------------------- #
word_file = pandas.read_csv(f"data/{LANGUAGE_FILE}")
word_dictionary = word_file.to_dict(orient="records")


def generate_word():
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

# Flash Card Front
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
card_canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = card_canvas.create_image(400, 263, image=front_card_image)
lang_text = card_canvas.create_text(400, 150, text="Language", fill="black", font=(FONT, 40, "italic"))
word_text = card_canvas.create_text(400, 263, text="Word", fill="black", font=(FONT, 50, "bold"))
card_canvas.grid(row=0, column=0, columnspan=2)

# Right Button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=generate_word)
right_button.grid(row=1, column=1)

# Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)

timer = window.after(3000, flip_card)

generate_word()

window.mainloop()
