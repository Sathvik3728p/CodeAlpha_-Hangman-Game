import random

predefined_list = ["apple", "chair", "water", "puzzle", "house"]

attempts = 6

random_word = random.choice(predefined_list)

guessed_letters = []

print("------ Welcome to Hangman Game! ------")

while attempts > 0:

    display_word = ""
    word_complete = True

    for letter in random_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
            word_complete = False

    print(f"\nWord: {display_word}")

    if word_complete:
        print("Congratulations! You guessed the word correctly!")
        break

    guessed_letter = input("Guess a letter: ").lower()[0]

    if guessed_letter in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guessed_letter)

    if guessed_letter in random_word:
        print("Hooray! You guessed correctly.")
    else:
        attempts -= 1
        print("Wrong guess, but don't give up!")
        print(f"Attempts left: {attempts}")

if attempts == 0:
    print("\nYou fought bravely, but the game wins this time.")
    print(f"The word was '{random_word}'.")