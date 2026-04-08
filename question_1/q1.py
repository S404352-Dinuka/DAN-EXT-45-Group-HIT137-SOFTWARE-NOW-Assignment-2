try: 
    with open ('raw_text.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
        print('File is not Found!')

try:
    shift1 = int(input("Enter Shift No 1: "))
    shift2 = int(input("Enter Shift No 2:"))
    print(shift1, shift2)
except ValueError:
     print('Enter a valid number')

def check_letters(letter, shift1, shift2):
    lower_check = False
    first_check = True
    if letter.islower():
        lower_check = True
    elif letter.isupper():
        lower_check = False
    temp_l = letter.lower()
    first = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    second = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(first)):
        if temp_l == first[i]:
            first_check = True
            print(str(i), letter)
        elif temp_l == second[i]:
            print(str(i), letter)
        

def encrypt_file(data, no_one, no_two):
    for n in data:
        if n != " ":
            check_letters(n, no_one, no_two)
    return

encrypt_file(content, shift1, shift2)