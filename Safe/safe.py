import sys
import requests
'''
To Do
------
add command line args safe -word -random
'''
LETTERS = {
            "A":0, "B":1, "C":2, "D":3, "E":4, "F":5, 
            "G":6, "H":7, "I":8, "J":9, "K":0, "L":1, 
            "M":2, "N":3, "O":4, "P":5, "Q":6, "R":7, 
            "S":8, "T":9, "U":0, "V":1, "W":2, "X":3, 
            "Y":4, "Z":5        
}


def main():
    gen_combo(word = get_input())
    
    print(f"Word: {word}, Combo: COMBO")


def get_input():
    word = input("Enter 6 letter word to generate comboination: ").strip().upper()
    if word.isalpha() and len(word) == 6:
        return word
    else:
        print(f"{word} is not a valid input, generating random combination:")
        return random_word()


def random_word():
    response = requests.get("https://random-word-api.herokuapp.com/word?length=6")
    word = "".join(response.json()).upper()
    return word


def gen_combo(word:str) ->str:
    
    combo = ""
    return combo


if __name__ =="__main__":
    main()
    