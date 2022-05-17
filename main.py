import random
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# Checking if file "words_to_learn" exists
try:
    df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv('./data/french_words.csv')

# Storing data in list
listOfWords = (df.to_dict(orient="records"))

# Generate random word from list
current_word = random.choice(listOfWords)


# If the user clicks the green button on the screen, this function is starting and deletes current word from the list
def known_word():
    listOfWords.remove(current_word)
    dataFrame = pd.DataFrame(listOfWords)
    dataFrame.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# This function shows French side of the card, and after 3 seconds call another function...
def next_card():
    global current_word, timer
    window.after_cancel(timer)
    current_word = random.choice(listOfWords)
    french_word = current_word["French"]
    canvas.itemconfig(image, image=french_image)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(text, text=french_word, fill="black")
    timer = window.after(3000, flip_card)


# This one shows English side of the card. It's called by "next_card" function.
def flip_card():
    english_word = current_word["English"]
    canvas.itemconfig(image, image=english_image)
    canvas.itemconfig(text, fill="white", text=english_word)
    canvas.itemconfig(title, fill="white", text="English")


# Making GUI
window = Tk()

window.title("FlashCard")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(3000, flip_card)

# Defining specs for canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
french_image = PhotoImage(file="./images/card_front.png")
english_image = PhotoImage(file="./images/card_back.png")
image = canvas.create_image(400, 263, image=french_image)
title = canvas.create_text(400, 150, font="Times 30 italic", text="")
text = canvas.create_text(400, 263, font="Times 40 bold", text="")
canvas.grid(row=0, column=0, columnspan=2)

wrongImg = PhotoImage(file="./images/wrong.png")
Button(window, image=wrongImg, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card).grid(row=1, column=0)
rightImg = PhotoImage(file="./images/right.png")
Button(window, image=rightImg, bg=BACKGROUND_COLOR, highlightthickness=0, command=known_word).grid(row=1, column=1)

next_card()

window.mainloop()
