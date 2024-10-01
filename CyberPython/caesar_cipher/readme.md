# Caesar Cipher Encryption & Decryption

This is a simple implementation of the **Caesar Cipher** encryption and decryption technique in Python. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

## How it Works

### Encryption:
- Each letter in the message is shifted by a certain number of positions in the alphabet. 
- For example, with a shift of 3, the letter 'A' becomes 'D', 'B' becomes 'E', and so on. 
- Non-alphabet characters (like spaces and punctuation) remain unchanged.

### Decryption:
- The decryption process shifts the letters back by the same number, restoring the original message.

## Steps to Use

1. Enter the message you want to encrypt.
2. Enter the shift value (a number between 1 and 25).
3. The program will output the encrypted message.
4. The same shift value is used to decrypt the message back to its original form.

## Example

- **Input Message**: `Hello, World!`
- **Shift Value**: `3`
- **Encrypted Message**: `Khoor, Zruog!`
- **Decrypted Message**: `Hello, World!`

## How to Run

1. Copy the code below into a Python file.
2. Run the Python file in your Python environment (e.g., IDLE or any IDE).
3. Follow the prompts to encrypt or decrypt your message.

## Code Explanation

The program contains two main parts:
- **Encryption**: Shifts each letter in the message forward by the shift value.
- **Decryption**: Shifts each letter backward to retrieve the original message.

Both processes handle upper and lowercase letters, leaving non-alphabet characters unchanged.
