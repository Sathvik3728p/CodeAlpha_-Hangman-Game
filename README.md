# 🕹️ Hangman Game (Python)

## 📌 Overview
This is a simple text‑based Hangman game built in Python. The program randomly selects a word from a predefined list, and the player has 6 chances to guess it correctly before losing.  

## ⚙️ Features
- Predefined list of 5 words (`apple`, `chair`, `water`, `puzzle`, `house`)  
- Random word selection using `random.choice().`  
- Tracks guessed letters and remaining attempts  
- Console‑based input/output — no graphics or audio  
- Clear win/lose messages  

## 🛠️ Concepts Used
- **Random module** → word selection  
- **While loop** → game continues until win/lose  
- **If‑else statements** → check correctness of guesses  
- **Strings & Lists** → represent word state and guesses  

## 🚀 How to Run
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/hangman-game.git
   ```
2. Navigate to the project folder:  
   ```bash
   cd hangman-game
   ```
3. Run the script:  
   ```bash
   python hangman.py
   ```

## 📊 Sample Run
```
------ Welcome to Hangman Game! ------

Word: _ _ _ _ _

Guess a letter: a
❌ Wrong guess, but don't give up!
Attempts left: 5

Word: _ a _ _ _
...
```

## 🎯 Learning Outcomes
- Reinforced understanding of loops and conditionals in Python  
- Learned how to manage game state (letters guessed, attempts left)  
- Practiced building interactive console applications
