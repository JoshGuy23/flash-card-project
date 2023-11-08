# Flash Card Project

## Introduction

A flash card project for studying foreign languages.

## Instructions

### Setup

Before beginning, it is recommended to create a .csv file with the first column having words of the language being studied, and the second column having their English equivalents (or whatever the user's native language is).

Be sure to put this file in the data folder.

Change the constants in the program to fit the user's particular needs. The constants that may be changed are:

BACKGROUND_COLOR - The background color of the app.

FONT - The font the text is displayed in.

LANGUAGE_FILE - The file the words will be retrieved from.

LEARNING_LANGUAGE - The language the user is studying.

NATIVE_LANGUAGE - The native language of the user.

### Using the Program

After starting the program, a random word from the language being studied is generated from the .csv file.

The user has 3 seconds to guess the meaning of the word before the card is flipped.

If the user guessed correctly, they may press the green checkmark button to remove the word from the list of words to study and generate a new word.

If the user guessed incorrectly, they may press the red X/cross button to continue studying words.

After every guess, every word that the user has yet to guess correctly is added to a "[language]_words_to_learn.csv" file for later studying.

Upon restarting the program, the program will draw words from this file until the user decides to remove it.

## Requirements

Running main.py requires:

Every image in the images folder (and the folder itself),

The data folder containing a .csv file of the words being studied (and optionally, a .csv file of words the user has yet to guess correctly),

And the Pandas package.
