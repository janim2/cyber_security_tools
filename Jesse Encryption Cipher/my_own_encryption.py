import string

#REFRENCE NUMBER: 21025611

#A symmetric cipher is one that uses the same key for encryption and decryption
#STEPS

#TODO:Take input string that needs to be encrypted
#TODO:Change all lowercases to uppercases and vice versa. 
#TODO:Calculate location of all the letters in the alphabet
#TODO:Subtract 3 from the positions of only the uppercase letters.
#TODO:Use the new positions to get the corresponding alphabets. 

'''
Example: 
J  e s  s  e
j  E S  S  E
10 5 19 19 5
10 2 16 16 2
j  B P  P  B
'''

lowercase_alphabet_space = string.ascii_lowercase
uppercase_alphabet_space = string.ascii_uppercase

def my_own_encryption_algorithm(plain_text, shift):
    converted_cases = ''
    cipher_text = ''

    for char in plain_text: 
        # print(char)
        if(char.isupper()):
            converted_cases += char.lower()
            position = lowercase_alphabet_space.index(char.lower()) + 1
            cipher_text += converted_cases

        else: 
            converted_cases += char.upper()
            position = uppercase_alphabet_space.index(char.upper()) + 1
            position = position - shift
            cipher_text += uppercase_alphabet_space[position - 1]


    # print(cipher_text)
    return cipher_text
# shifted_alphabets = alphabet_space[shift:] + alphabet_space[:shift]
# cmp_table = str.maketrans(alphabet_space, shifted_alphabets)
# ciphertext = plain_text.translate(cmp_table)
# print(ciphertext)

#OPTIMIZED CODE 
    
def my_own_encryption_algorithm_optimized(plain_text, shift):
    cipher_text = ''

    lowercase_alphabet_space = string.ascii_lowercase
    uppercase_alphabet_space = string.ascii_uppercase

    for char in plain_text:
        if char.isupper():
            # Convert uppercase to lowercase and shift
            position = lowercase_alphabet_space.index(char.lower())
            cipher_text += lowercase_alphabet_space[position]  # Append shifted lowercase char
        else:
            # Convert lowercase to uppercase and shift backwards
            position = uppercase_alphabet_space.index(char.upper())
            new_position = (position - shift) % 26  # Ensure the position wraps around
            cipher_text += uppercase_alphabet_space[new_position]  # Append shifted uppercase char

    # print(f"Cipher text: {cipher_text}")
    return cipher_text


def my_own_decryption_algorithm(cipher_text, shift):
    plain_text = ''

    lowercase_alphabet_space = string.ascii_lowercase
    uppercase_alphabet_space = string.ascii_uppercase

    for char in cipher_text:
        if char.isupper():
            # Convert uppercase to lowercase and shift backwards
            position = lowercase_alphabet_space.index(char.lower())
            new_position = (position - -shift) % 26  # Ensure the position wraps around
            plain_text += lowercase_alphabet_space[new_position]  # Append shifted lowercase char
        else:
            # Convert lowercase to uppercase and shift
            position = uppercase_alphabet_space.index(char.upper())
            plain_text += uppercase_alphabet_space[position]  # Append shifted uppercase char
    print(plain_text)
    # return plain_text

def encrypt_file():
    try:
        with open('file.txt', 'r') as file:
            content = file.read()

        encrypted_content = my_own_encryption_algorithm_optimized(content, 3)
        
        with open('encrypted_file.txt', 'w') as file:
            content = file.write(encrypted_content)

        print("File Encryption complete")
    
    except FileNotFoundError:
        print(f"The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")



# my_own_encryption_algorithm('Jesse', 3)
# my_own_encryption_algorithm_optimized('Jesse', 3)
my_own_decryption_algorithm('jBPPB', 3)
# encrypt_file()