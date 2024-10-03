# Atbash Cipher - Encryption/Decryption Program

##  Description
The Atbash Cipher is a simple substitution cipher that reverses the letters of the alphabet. This means that:

* 'A' is replaced with 'Z'
* 'B' is replaced with 'Y'
* 'C' is replaced with 'X'
And so on...

It is a type of symmetrical cipher, which means that the same algorithm is used for both encryption and decryption. If you encrypt a message using the Atbash Cipher, running the cipher on the encrypted message will give you back the original message.

This program takes a message as input from the user and automatically encrypts (or decrypts) it using the Atbash Cipher.

## How the Cipher Works
For each letter in the message:
* If it’s an uppercase letter (A-Z), it is replaced by its reverse counterpart ('A' becomes 'Z', 'B' becomes 'Y', etc.).
* If it’s a lowercase letter (a-z), it is similarly replaced ('a' becomes 'z', 'b' becomes 'y', etc.).
* Non-alphabet characters (like spaces, punctuation, numbers) remain unchanged.

This is a very simple cipher, yet it introduces the concept of letter substitution, which is useful for beginners learning about cryptography.

---

## Example

Here’s an example of how the Atbash Cipher works:

Input:
```
Hello, World!
```
Output:
```
Svool, Dliow!
```

As you can see, each letter of the original message is replaced with its reverse counterpart in the alphabet, and the spaces and punctuation remain unchanged.

---
