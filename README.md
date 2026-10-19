# 🎯 Number Guessing Game

A simple **Number Guessing Game** built with Python. The computer randomly selects a number between **1 and 100**, and the player tries to guess it. After each guess, the game gives a hint telling you whether your guess is too high or too low.

## 📌 Features

* 🎲 Randomly generates a number between 1 and 100
* ⌨️ Takes guesses from the user
* 🔼 Shows **"Too high!"** when the guess is too large
* 🔽 Shows **"Too low!"** when the guess is too small
* ✅ Displays a success message when the correct number is guessed
* 📊 Counts and displays the number of attempts

## 🛠️ Technologies Used

* **Python 3**
* `random` module

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/safamariyam1902-tech/number-guessing-game.git
```

### 2. Navigate to the project folder

```bash
cd number-guessing-game
```

### 3. Run the Python program

```bash
python number_guessing_game.py
```

## 🎮 How to Play

1. Start the program.
2. The computer chooses a random number between **1 and 100**.
3. Enter your guess when prompted.
4. The game will tell you:

   * **Too low!** → Guess a higher number.
   * **Too high!** → Guess a lower number.
5. Continue guessing until you find the correct number.
6. Your total number of attempts will be displayed.

## 💻 Example

```text
Welcome to the Number Guessing Game!
Guess a number between 1 and 100.

Your guess: 50
Too high! Try again.

Your guess: 25
Too low! Try again.

Your guess: 37
Too high! Try again.

Your guess: 32
Correct! The number was 32.
Attempts: 4
```

## 📂 Project Structure

```text
number-guessing-game/
│
├── number_guessing_game.py
└── README.md
```

## 🌱 Future Improvements

Some possible improvements for future versions:

* Add input validation for non-numeric values
* Add difficulty levels
* Limit the number of attempts
* Allow the player to play multiple rounds
* Add a scoring system
* Add a GUI version

## 👩‍💻 Author

**Safa Mariyam**

Feel free to ⭐ star the repository if you found it useful!

