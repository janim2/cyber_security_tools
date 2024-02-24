import string
import tkinter as tk
from tkinter import filedialog
TK_SILENCE_DEPRECATION=1

def encrypt_button():
    plain_text_field_value = plain_text_field.get(1.0, "end-1c")
    if(plain_text_field_value == ""):
        result_text["text"] = "Enter plain text"
    else:
        result_text["text"] = f"Encrypted text: {encrypt(plain_text_field_value, 3)}"
        
def decrypt_button():
    cipher_text_field_value = cipher_text_field.get(1.0, "end-1c")
    if(cipher_text_field_value == ""):
        result_text["text"] = "Enter cipher text"
    else:
        result_text["text"] =  f"Decrypted text: {decrypt(cipher_text_field_value, 3)}"

def encrypt(plain_text, shift):
    result_text["text"] = "Encrypting..."
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
    plain_text_field.delete('1.0', "end-1c")
    return cipher_text

def decrypt(cipher_text, shift):
    result_text["text"] = "Decrypting..."
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
    cipher_text_field.delete('1.0', "end-1c")
    return plain_text

def UploadAction():
    filename = filedialog.askopenfilename()
    file_name_field["text"] = filename
    result_text["text"] = encrypt_file(filename)
    file_name_field["text"] = ""
    # print('Selected:', filename)

def encrypt_file(file_location):
    try:
        with open(file_location, 'r') as file:
            content = file.read()

        encrypted_content = encrypt(content, 3)
        
        with open(file_location, 'w') as file:
            content = file.write(encrypted_content)

        return "File Encryption complete"
    
    except FileNotFoundError:
        return f"The file was not found."
    except Exception as e:
        return f"An error occurred: {e}"

window = tk.Tk()
window.geometry('500x500')

frame1 = tk.Frame(window, padx=10, pady=50, height=5)
frame2 = tk.Frame(window, padx=10, width=50)
frame3 = tk.Frame(window, padx=10, pady=50, width=50)
frameBottom = tk.Frame(window, padx=10, pady=50, width=50)

greeting = tk.Label(text="Jesse Encryption Tool", font=("Helvetica", 20))
greeting.pack()

ref_no_text = tk.Label(text="21025611", font=("Helvetica", 20))
ref_no_text.pack()
##PLAIN TEXT
plain_text_instruction = tk.Label(frame1, text="Enter Plain text")
plain_text_instruction.pack(side=tk.LEFT)

plain_text_field = tk.Text(frame1, height=1.4, width=20, font=("Helvetica", 15))
plain_text_field.pack(side=tk.LEFT)

plain_text_field_button = tk.Button(frame1, height=1, width=10, font=("Helvetica", 15), text='Encrypt', command=encrypt_button)
plain_text_field_button.pack(side=tk.LEFT)
##PLAIN TEXT ENDS HERE

##CIPHER TEXT STARTS HERE
cipher_greeting = tk.Label(frame2, text="Enter Cipher text")
cipher_greeting.pack(side=tk.LEFT)

cipher_text_field = tk.Text(frame2, height=1.4, width=20, font=("Helvetica", 15))
cipher_text_field.pack(side=tk.LEFT)

cipher_text_field_button = tk.Button(frame2, height=1, width=10, font=("Helvetica", 15), fg='black', text='Decrypt', command=decrypt_button)
cipher_text_field_button.pack(side=tk.LEFT)
##CIPHER TEXT ENDS HERE

file_name_field = tk.Label(frame3, font=("Helvetica", 15))
file_name_field.pack(side=tk.TOP)

choose_file_button = tk.Button(frame3, text='Select File', command=UploadAction)
choose_file_button.pack(side=tk.LEFT)

encrypt_file_button = tk.Button(frame3, text='Encrypt File')
encrypt_file_button.pack(side=tk.LEFT)

##RESULT FRAME
result_text = tk.Label(frameBottom, height=1, width=20, text="", font=('Arial', 20))
result_text.pack(side=tk.LEFT)
#RESULT FRAME ENDS HERE

frame1.pack()
frame2.pack()
frame3.pack(side=tk.TOP)
frameBottom.pack(side=tk.BOTTOM)

window.mainloop()