# Ask the user if they want to encrypt or decrypt
choice = input("Do you want to encrypt or decrypt a message? (E/D): ").strip().upper()

# Ask for the shift value (an integer from 1 to 25)
shift = int(input("Enter the shift value (1-25): "))

# Function to encrypt the message
def encrypt(message, shift):
    """
    Encrypts a given message using Caesar Cipher.

    Parameters:
    message (str): The original message to be encrypted.
    shift (int): The number of positions to shift each letter.

    Returns:
    str: The encrypted message.
    """
    encrypted_message = ""  # Initialize an empty string to store the encrypted message
    
    # Loop through each character in the message
    for char in message:
        # Check if the character is a letter
        if char.isalpha():
            # Determine if the letter is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Perform the shift
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_message += encrypted_char
        else:
            # If it's not a letter (e.g., space, punctuation), keep it unchanged
            encrypted_message += char
    
    return encrypted_message

# Function to decrypt the message
def decrypt(encrypted_message, shift):
    """
    Decrypts a Caesar Cipher encrypted message.

    Parameters:
    encrypted_message (str): The message that was encrypted.
    shift (int): The number of positions the letters were shifted during encryption.

    Returns:
    str: The original message.
    """
    decrypted_message = ""  # Initialize an empty string to store the decrypted message
    
    # Loop through each character in the encrypted message
    for char in encrypted_message:
        # Check if the character is a letter
        if char.isalpha():
            # Determine if the letter is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Reverse the shift to get the original character
            decrypted_char = chr((ord(char) - start - shift) % 26 + start)
            decrypted_message += decrypted_char
        else:
            # If it's not a letter (e.g., space, punctuation), keep it unchanged
            decrypted_message += char
    
    return decrypted_message

# Ask for the message only after determining whether to encrypt or decrypt
message = input("Enter the message: ")

# Perform encryption or decryption based on user choice
if choice == 'E':
    encrypted_message = encrypt(message, shift)
    print("Encrypted message:", encrypted_message)
elif choice == 'D':
    decrypted_message = decrypt(message, shift)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid choice. Please select 'E' for encryption or 'D' for decryption.")
