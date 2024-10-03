# Function to encrypt or decrypt a message using the Atbash Cipher
def atbash_cipher(message):
    """
    Encrypts or decrypts a given message using the Atbash Cipher.

    Parameters:
    message (str): The original message to be encrypted or decrypted.

    Returns:
    str: The encrypted or decrypted message.
    """
    result = ""  # Initialize an empty string to store the result
    
    # Loop through each character in the message
    for char in message:
        if char.isalpha():  # Only change alphabet characters
            if char.isupper():
                # For uppercase letters: A -> Z, B -> Y, ..., Z -> A
                result = result + chr(155 - ord(char))  # 155 is 'A' + 'Z'
            else:
                # For lowercase letters: a -> z, b -> y, ..., z -> a
                result = result + chr(219 - ord(char))  # 219 is 'a' + 'z'
        else:
            # Non-alphabet characters remain the same (e.g., space, punctuation)
            result += char
    
    return result

# Ask the user for a message to encrypt/decrypt
message = input("Enter the message: ")

# Perform encryption/decryption using the Atbash Cipher
encrypted_message = atbash_cipher(message)

# Output the result
print("Cipher text:", encrypted_message)


"""
How It Works:
1. The atbash_cipher function takes a message as input and loops through each character.
2. It checks if the character is an alphabet letter, and if so, it calculates the reverse equivalent (for example, 'A' becomes 'Z', 'B' becomes 'Y').
3. Non-alphabet characters, like spaces and punctuation, remain unchanged.
4. The result is the encrypted (or decrypted, since it's symmetrical) message.
"""
