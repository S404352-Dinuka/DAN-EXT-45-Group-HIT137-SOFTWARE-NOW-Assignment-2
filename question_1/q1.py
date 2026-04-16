#Try catch block to check if the file is present
try: 
    with open ('raw_text.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
        print('File is not Found!')
#Try catch block to see if user entered values are valid 
try:
    shift1 = int(input("Enter Shift No 1: "))
    shift2 = int(input("Enter Shift No 2:"))
    print(shift1, shift2)
except ValueError:
     print('Enter a valid number')
#Check letters method checks if the letter is lowercase, if the letter is present in the first section of the alphabet and calculates the correct shift and return the shifted value from the list with the correct style (Upper or Lower)
def check_letters(letter, shift1, shift2, keys, index):
    lower_check = False
    first_check = True
    final_shift = 0
    if letter.islower():
        lower_check = True
    elif letter.isupper():
        lower_check = False
    temp_l = letter.lower()
    first_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(first_list)):
        if temp_l == first_list[i]:
            break
        elif first_list[i] == 'n':
            first_check = False 
    if first_check and lower_check:
        final_shift = shift1 * shift2
    elif first_check and not lower_check:
        final_shift = -(shift1)
    elif not first_check and lower_check:
        final_shift = - (shift1 + shift2)
    elif not first_check and not lower_check:
        final_shift = shift2 ** 2
    final_shift = (final_shift + i) % 26
    value = first_list[final_shift]
    if lower_check == False:
        value = first_list[final_shift].upper()
    #Stores the key value pairs of the intial value and shifted value in a dictionary depending on their position in the alphabet.
    keys['first_check'][index] = first_check
    if first_check == True:
        keys['first'][letter] = value
    else:
        keys['second'][letter] = value 
    return value
        
#Encrypt function takes user shifts and passes it to check_letters method to get the value, switched it with the shift value and stores it in a list.
def encrypt_file(data, no_one, no_two, dict):
    shift_list = []
    count = 0
    for n in data:
        new_value = n
        if n.isalpha():
            new_value = check_letters(n, no_one, no_two, dict, count)
            print(new_value)
        shift_list.insert(count, new_value)
        count += 1
    #Joins the final list and creates a new file and stores it in the file.
    encrypted_text = "".join(shift_list)
    with open('encrypted_text.txt', 'w', encoding='utf-8') as file:
        file.write(encrypted_text)
    return encrypted_text
    
#Decrypts the encrypted file by using a dictionary to check the location of the alphabet and get the original value.
def decrypt_file(keys):
    try: 
        #Encryptd file is opened and read the content here
        with open ('encrypted_text.txt', 'r') as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print('File is not Found!') # If the file is not found, function is stopping. 
    shift_list = []  # List to store decrypted characters
    count = 0 # Keep a count for tracking the positions
   # Through each character in the encrypted data one by one (Looping)
    for n in data:
        new_value = n # The encrypted data will keep the value by default
        # Check only alphabetic characters
        if n.isalpha():
           
            if keys['first_check'][count]:
                for key, val in keys['first'].items():
                    if val == n:
                        new_value = key
            
            else:
                for key, val in keys['second'].items():
                    if val == n:
                        new_value = key
                print(new_value)
        shift_list.insert(count, new_value)
        count += 1
    # Join all characters into one string
    decrypted_text = "".join(shift_list)
    
    with open('decrypted_text.txt', 'w', encoding='utf-8') as file:
        file.write(decrypted_text)
        
encrypt_keys = {
    'first': {},
    'second': {},
    'first_check': {}
}
new_txt = encrypt_file(content, shift1, shift2, encrypt_keys)
print(encrypt_keys)

decrypt_file(encrypt_keys)