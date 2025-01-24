# Vigenère Cipher Encryption & Decryption

## Problem Description
The **Vigenère Cipher** is a method of encrypting alphabetic text using a simple form of polyalphabetic substitution. It uses a keyword to shift each letter of the plaintext forward by the position of the corresponding letter in the keyword. Decryption is the reverse process, shifting letters backward by the corresponding keyword letter.

### Encryption Example:
**Plaintext**: `HELLO`  
**Keyword**: `KEY`  
1. Extend the keyword to match the length of the plaintext: `KEYKE`
2. Encrypt the text:
   - `H` shifted by `K` becomes `R`
   - `E` shifted by `E` becomes `I`
   - `L` shifted by `Y` becomes `J`
   - `L` shifted by `K` becomes `V`
   - `O` shifted by `E` becomes `S`

**Ciphertext**: `RIJVS`

### Decryption Example:
**Ciphertext**: `RIJVS`  
**Keyword**: `KEY`
1. Use the same keyword for decryption:
   - `R` shifted back by `K` becomes `H`
   - `I` shifted back by `E` becomes `E`
   - `J` shifted back by `Y` becomes `L`
   - `V` shifted back by `K` becomes `L`
   - `S` shifted back by `E` becomes `O`

**Plaintext**: `HELLO`

## Prerequisites:
- Python 3.x installed
---

### Sample Input and Output:
Encrypt:
```
Do you want to (E)ncrypt or (D)ecrypt? E
Enter the message: HELLO
Enter the keyword: KEY
Encrypted message: RIJVS
```
Decrypt:
```
Do you want to (E)ncrypt or (D)ecrypt? D
Enter the message: RIJVS
Enter the keyword: KEY
Decrypted message: HELLO
```

---

## Additional Challenge:
Modify the program to handle case sensitivity, spaces, and special characters while preserving the original format.