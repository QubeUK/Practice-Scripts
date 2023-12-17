"""Modules used for Operating system access and command line arguments"""
import os
import sys


def main():
    """Function for main"""
    if len(sys.argv) == 3:
        match sys.argv[1]:
            case "-c":
                byte_count = byte(sys.argv[2])
                print(f"{byte_count} {sys.argv[2]}")
            case "-l":
                line_count = line(sys.argv[2])
                print(f"{line_count} {sys.argv[2]}")
            case "-w":
                word_count = word(sys.argv[2])
                print(f"{word_count} {sys.argv[2]}")
            case "-m":
                char_count = char(sys.argv[2])
                print(f"{char_count} {sys.argv[2]}")        

    elif len(sys.argv) == 2:
        byte_count = byte(sys.argv[1])
        word_count = word(sys.argv[1])
        line_count = line(sys.argv[1])
        char_count = char(sys.argv[1])        
        print(f"{line_count} {word_count} {byte_count} {sys.argv[1]}")
    else:
        sys.exit("Invalid Usage")


def word(arg:str) -> int:
    """Function for returning word count"""
    word_count = 0
    with open(arg, "r", encoding="utf-8") as file:
        word_count += len(file.read().split())
    return word_count


def line(arg:str) -> int:
    """Function for returning line count"""
    with open(arg, "r", encoding="utf-8") as file:
        line_count = len(file.readlines())
    return line_count


def char(arg:str) -> int:
    """Function for returning char count"""
    with open(arg, "r", encoding="utf-8") as file:
        char_count = len(file.read())        
    return char_count


def byte(arg:str) -> int:
    """Function for returning filesize in bytes"""
    file_size = os.path.getsize(arg)
    return file_size


if __name__ == "__main__":
    main()
