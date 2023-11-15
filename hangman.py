import sys
import requests
import hangman_pics
import warnings


warnings.filterwarnings('ignore')
def main():
    word = get_word()
    guess_count = 0
    guessed = set()
    tries_allowed = 7
    mask = ["*" for _ in word]
    while guess_count < tries_allowed:

        show_guessed = "".join(guessed)
        print(hangman_pics.HANGMAN_PICS[guess_count])
        print(" ".join(mask))
        print(f"Tries left: {tries_allowed - guess_count}")
        print(f"Letters already guessed: {show_guessed}")

        guess, guessed = get_guess(guessed)
        if guess not in word:
            print(f"{guess} is not there.\n")
            guess_count += 1
        print(f"\nMatched {word.count(guess)} x {guess}\n")
        mask = show_word(word, guess, mask)
        mask_show = "".join(mask)
        if mask_show == word:
            sys.exit("Well done! The word was " + word)
    print(f"\nYou did not solve it, the word was {word}")
    return


def show_word(word, guess, mask):
    for pos in range(len(word)):
        char = word[pos]
        if char == guess:
            mask[pos] = char
    return mask


def get_guess(guessed):
    while True:
        guess = input("Guess a letter: ").upper()
        if guess in guessed:
            print("Letter already guessed, please guess again")
        guessed.add(guess)
        return guess, guessed


def get_word():
    response = requests.get("https://random-word-api.herokuapp.com/word?length=6")
    word = input("Enter word to be guessed or press enter for random word: ").upper()
    if len(word) == 0:
        word = "".join(response.json()).upper()
    if not word.isalpha():
        print(f"{word} is invalid, picking random word from list")
        word = "".join(response.json()).upper()
    return word


if __name__ == "__main__":
    main()
