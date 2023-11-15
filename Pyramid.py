def main():
    string = get_input()
    tri, row = is_triangular(string)
    if tri == False:
        string = calc_padding(string, row)
    print_pyramid(string)
    return

def is_triangular(string): # Modified from https://www.geeksforgeeks.org/triangular-numbers/
    sum = 0 
    num = 1
    while(sum <= len(string)): 
        sum += num
        if (sum == len(string)):
            return True, num
        num += 1     
    return False, num

def calc_padding(string,row):
    row = int(row * (row - 1) / 2)
    string += "*" * int(row - len(string))
    return string

def get_input():
    string = input("Enter text: ")
    return string

def print_pyramid(string):
    start = 0
    length = 1
    while start < len(string):
        row = string[start: start+length]
        print(row)
        start += length
        length += 1
    return

if __name__ == "__main__":
    main()