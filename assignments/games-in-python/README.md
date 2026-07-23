
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman word-guessing game using Python string handling, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create the start of the Hangman game by choosing a word and initializing the game state.

#### Requirements
Completed program should:

- Choose a random word from a predefined list of words.
- Initialize the hidden word display using underscores or blanks for each letter.
- Track letters guessed by the player.
- Show the current progress to the player in a readable format, e.g. `_ a _ _ m a n`.

### 🛠️ Guess Handling and Game Flow

#### Description
Allow the player to guess letters, update the game state, and determine when the game ends.

#### Requirements
Completed program should:

- Prompt the player to enter one letter per guess.
- Update the displayed word when correct letters are guessed.
- Track remaining incorrect attempts and reduce them on wrong guesses.
- End the game with a win message when the word is fully guessed.
- End the game with a lose message when the player runs out of attempts.
- Prevent repeated guesses from affecting the remaining attempts.
