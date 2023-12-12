import sys
from tabulate import tabulate


def main() -> None:
    selection = menu()
    print()
    words = get_inputs()
    show_story(selection, words)
    

def menu() -> str:
    menu_data = [["Key","Option"],
            ["[ 1 ]","Story 1"],
            ["[ 2 ]","Story 2"],
            ["[ 3 ]","Story 3"],
            ["[ 4 ]","Story 4"],
            ["[ Q ]","Quit"]]

    print(tabulate(menu_data,headers="firstrow",tablefmt="fancy_outline"))
    option = input("Make selection: ")
    if option =="q" or option == "Q":sys.exit()
    return option


def get_inputs() -> dict[str,str]:
    print("-----------------------------------------\nEnter the following to complete the story\n-----------------------------------------")
    words = {"noun": "", "adj": "", "verb": "", "adverb": "", "interject": ""}
    words["noun"] = input("Noun: Person, Place or Thing (the President, living room, cup): ")
    words["adj"] = input("Adjective: A word that describes a noun (smelly, green, alive): ")
    words["verb"] = input("Verb: A word that shows an action (run, jump, play): ")
    words["adverb"] = input("Adverb: a word that describes how you do an action (quickly, gracefully, badly): ")
    words["interject"] = input("Interjection: a short word or phrase that expresses emotion (Hey! Oh! WTF?!?): ")      
    return words


def show_story(selection, words) -> None: 
    match selection:
        case "1":
            print(
                f'Once upon a time, there was a {words["noun"]} that lived in a {words["adj"]} castle. The {words["adj"]} castle was '
                f'home to a grumpy old man that liked to {words["verb"]} with small animals until one day this ended {words["adverb"]} ' 
                f'the old man shouted {words["interject"]}'
                )
        case _:
            print(
                f'Once upon a time, there was a {words["noun"]} that lived in a {words["adj"]} castle. The {words["adj"]} castle was '
                f'home to a grumpy old man that liked to {words["verb"]} with small animals until one day this ended {words["adverb"]} ' 
                f'the old man shouted {words["interject"]}'
                )
               

if __name__ == "__main__":
    main()
