# Function to generate the full keyword by repeating it to match the length of the message
def generate_full_keyword(message, keyword):
    keyword = list(keyword)
    if len(message) == len(keyword):
        return keyword
    else:
        for i in range(len(message) - len(keyword)):
            keyword.append(keyword[i % len(keyword)])
    return "".join(keyword)

# Function to encrypt the plaintext using the keyword with step-by-step explanation
def vigenere_encrypt(plaintext, keyword):
    encrypted_text = []
    keyword = generate_full_keyword(plaintext, keyword)
    
    print("\nStep-by-step encryption process:")
    print(f"{'Plaintext':<12}{'Keyword':<12}{'Shift':<6}{'Encrypted Letter':<18}")
    print("-" * 50)
    
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            # Calculate the shift value using the Vigenère cipher formula
            shift = (ord(plaintext[i].upper()) + ord(keyword[i].upper()) - 2 * ord('A')) % 26
            encrypted_letter = chr(shift + ord('A'))
            encrypted_text.append(encrypted_letter)
            
            # Print step-by-step details
            print(f"{plaintext[i]:<12}{keyword[i]:<12}{shift:<6}{encrypted_letter:<18}")
        else:
            encrypted_text.append(plaintext[i])  # Non-alphabetical characters are kept unchanged
    
    return "".join(encrypted_text)

# Function to decrypt the ciphertext using the keyword with step-by-step explanation
def vigenere_decrypt(ciphertext, keyword):
    decrypted_text = []
    keyword = generate_full_keyword(ciphertext, keyword)
    
    print("\nStep-by-step decryption process:")
    print(f"{'Ciphertext':<12}{'Keyword':<12}{'Shift':<6}{'Decrypted Letter':<18}")
    print("-" * 50)

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            # Calculate the shift value for decryption
            shift = (ord(ciphertext[i].upper()) - ord(keyword[i].upper()) + 26) % 26
            decrypted_letter = chr(shift + ord('A'))
            decrypted_text.append(decrypted_letter)

            # Print step-by-step details
            print(f"{ciphertext[i]:<12}{keyword[i]:<12}{shift:<6}{decrypted_letter:<18}")
        else:
            decrypted_text.append(ciphertext[i])
    
    return "".join(decrypted_text)

# User interaction for encryption or decryption
mode = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
message = input("Enter the message: ")
keyword = input("Enter the keyword: ")

# Encrypt or decrypt based on user input
if mode == 'E':
    encrypted_message = vigenere_encrypt(message, keyword)
    print("\nEncrypted message:", encrypted_message)
elif mode == 'D':
    decrypted_message = vigenere_decrypt(message, keyword)
    print("\nDecrypted message:", decrypted_message)
else:
    print("Invalid option! Please choose either E or D.")
