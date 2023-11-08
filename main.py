from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"

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

# Right Button
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)

# Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

window.mainloop()
