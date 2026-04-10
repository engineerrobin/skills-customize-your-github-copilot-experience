
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic Hangman word-guessing game in Python, practicing string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️ Set Up the Word List and Random Selection

#### Description
Create a predefined list of words and write the logic to randomly select one as the secret word for each game session.

#### Requirements
Completed program should:

- Define a list containing at least 10 words
- Use the `random` module to select a word at the start of each game
- Store the chosen word for use throughout the game loop

### 🛠️ Build the Game Loop

#### Description
Implement the main game loop where the player repeatedly guesses letters until they win or run out of attempts.

#### Requirements
Completed program should:

- Display the current word progress using underscores (e.g., `_ _ _ _ _`)
- Reveal correctly guessed letters in their positions
- Accept a single letter as input from the player each turn
- Track and display the number of incorrect guesses remaining (start with 6 attempts)
- Prevent duplicate guesses and notify the player if a letter was already guessed

### 🛠️ Display the Game Outcome

#### Description
Detect when the game ends and display an appropriate win or lose message to the player.

#### Requirements
Completed program should:

- End the game when the full word has been guessed correctly
- End the game when the player runs out of incorrect attempts
- Display a congratulations message and the word when the player wins
- Display a game-over message revealing the secret word when the player loses

Example output (win):

```
_ a _ _ a n
Correct! 
_ a n g m a n
You guessed it! The word was: hangman 🎉
```
