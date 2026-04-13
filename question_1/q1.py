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

def check_letters(letter, shift1, shift2, encrypt):
    lower_check = False
    first_check = True
    final_shift = 0
    if letter.islower():
        lower_check = True
    elif letter.isupper():
        lower_check = False
    temp_l = letter.lower()
    final_shift = 0
    first = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(first)):
        if temp_l == first[i]:
            break
        elif first[i] == 'n':
            first_check = False 
            
    if first_check and lower_check:
        final_shift = shift1 * shift2
    elif first_check and not lower_check:
        final_shift = -(shift1)
    elif not first_check and lower_check:
        final_shift = shift1 + shift2
    elif not first_check and not lower_check:
        final_shift = shift2 ^ 2
    final_value = check_shift(final_shift, first, encrypt, lower_check, i)
    return final_value

def check_shift(shift, first_list, encrypt_check, lower_check, index):
    max_index = len(first_list)
    if encrypt_check == False:
        shift = -(shift - index)
        print("shift", str(shift), "Index", str(index), "Value at Index: " , str(first_list[index]))
    else:
        shift = shift + index
    if shift > max_index:
        shift = shift - max_index
    value = first_list[shift]
    if lower_check == False:
        value = first_list[shift].upper()
    return value

def encrypt_file(data, no_one, no_two):
    shift_list = []
    movement = False
    count = 0
    for n in data:
        new_value = ' '
        if n != " ":
            new_value = check_letters(n, no_one, no_two, True)
            print(new_value)
        shift_list.insert(count, new_value)
        count += 1
    encrypted_text = "".join(shift_list)
    print(encrypted_text)
    return encrypted_text

encrypt_file(content, shift1, shift2)