import sys
LETTERS = {
            "A":0, "B":1, "C":2, "D":3, "E":4, "F":5, 
            "G":6, "H":7, "I":8, "J":9, "K":0, "L":1, 
            "M":2, "N":3, "O":4, "P":5, "Q":6, "R":7, 
            "S":8, "T":9, "U":0, "V":1, "W":2, "X":3, 
            "Y":4, "Z":5        
}

def main():
    codeword = get_input()
    print(f"{codeword}")
    

def get_input():
    codeword = input("Enter 6 letter word to generate comboination: ").strip().upper()
    if codeword.isalpha() and len(codeword) == 6:
        return codeword
    else:
        sys.exit(f"{codeword} is not a valid 6 letter word, please try again")


if __name__ =="__main__":
    main()
    