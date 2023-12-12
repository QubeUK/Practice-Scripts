"""Module providing a function to process API calls."""
import requests
# add command line args safe -word -random
LETTERS = {
            "A":0, "B":1, "C":2, "D":3, "E":4, "F":5, 
            "G":6, "H":7, "I":8, "J":9, "K":0, "L":1, 
            "M":2, "N":3, "O":4, "P":5, "Q":6, "R":7, 
            "S":8, "T":9, "U":0, "V":1, "W":2, "X":3, 
            "Y":4, "Z":5        
}


def main():
    """Function main."""
    word = get_input()
    combo = gen_combo(word)
    print(f" Word: {word[0]}{word[1]} {word[2]}{word[3]} {word[4]}{word[5]}")
    print(f"Combo: {combo[0]}{combo[1]} {combo[2]}{combo[3]} {combo[4]}{combo[5]}")


def get_input() -> str:
    """Function getting user input."""
    word = input("Enter 6 letter word to generate comboination: ").strip().upper()
    if word.isalpha() and len(word) == 6:
        return word
    print(f"{word} not a valid input, generating random combination.")
    return random_word()


def random_word() -> str:
    """Function to generate random 6 letter word."""
    response = requests.get("https://random-word-api.herokuapp.com/word?length=6", timeout=5)
    word = "".join(response.json()).upper()
    return word


def gen_combo(word:str) -> str:
    """Function creating combination from word."""
    combo = []
    for _, ele in enumerate(word):
        combo.append(LETTERS[ele])
    return combo


if __name__ =="__main__":
    main()
