# Playfair Cipher

The Playfair Cipher is a classical encryption method that encodes messages by dividing them into pairs of letters (called `digraphs`). It uses a `5x5` grid of letters, also known as the key matrix, to perform the encryption. This cipher is more secure than simple substitution ciphers because it encodes two letters at a time, thereby reducing frequency analysis attacks.

## How It Works
### Key Matrix:
* The key matrix is a `5x5` grid of letters used to encrypt or decrypt a message. It's generated from a keyword provided by the user. The keyword is followed by the remaining letters of the alphabet to fill the grid.

* Since there are 26 letters in the alphabet, and the matrix can only hold 25 letters (5x5 = 25), we remove the letter J from the alphabet. In the cipher, `J` is treated as `I`. The key matrix is essential for encoding and decoding the message.

### Text Preparation:
The message is split into pairs of letters. If a pair consists of the same letter, an `X` is inserted between them to ensure each pair is unique. If the message has an odd number of letters, an `X` is appended to the end to make it even.
### Encryption Rules:

* If the two letters in a pair are on the same row of the matrix, each is replaced by the letter to its immediate right (wrapping around to the left if needed).
* If the two letters in a pair are in the same column, they are replaced by the letter immediately below (wrapping around to the top if needed).
* If the two letters form a rectangle, they are replaced by the letters on the opposite corners of the rectangle.
Decryption is the reverse process, where the same key matrix is used to decrypt the message back to its original form.

### Decryption 
Decryption works similarly but in the opposite direction: replacing letters by moving to the left or up instead of right or down.

### Key Matrix Example
The key matrix is constructed using a keyword provided by the user. For example, if the keyword is "SECRET", the key matrix is built as follows:

1. Keyword:
   First, the keyword is written down `without` duplicate letters:
    ```
    S E C R T
    ```
2. Fill with Remaining Letters:
   The remaining letters of the alphabet (except for J) are filled in to complete the 5x5 matrix:
    ```
    S E C R T
    A B D F G
    H I K L M
    N O P Q U
    V W X Y Z
    ```
    ##### Key Matrix Breakdown:
    * The keyword "SECRET" is added to the grid.
    * Letters that repeat in the keyword are skipped.
    * The remaining alphabet is added (excluding 'J', which is treated as 'I') to complete the matrix.

## Step-by-Step Process
1. Generate Key Matrix:
   Create a `5x5` grid with the letters of the keyword and fill in the rest of the alphabet, replacing `J` with `I`.

2. Prepare the Text for Encryption:
   Modify the message by replacing `J` with `I`, splitting the text into pairs, and adding `X` where necessary.

3. Encrypt the Text:
   Apply the Playfair cipher rules to each pair of letters based on their position in the matrix.

4. Display the Key Matrix:
   The key matrix is displayed to help visualize the encryption process.

---

## Example Input and Output
Input:
```
Message: HELLO
Keyword: SECRET
```
Output:
```
Playfair Cipher Key Matrix:
S E C R T
A B D F G
H I K L M
N O P Q U
V W X Y Z

Encrypted Message: IBKKF
```
### Explanation
#### Key Matrix for the Keyword "SECRET"

| **S** | **E** | **C** | **R** | **T** |
|-------|-------|-------|-------|-------|
| A     | **B** | D     | F     | G     |
| **H** | **I** | K     | **L** | M     |
| N     | **O** | P     | **Q** | U     |
| V     | W     | **X** | Y     | Z     |

#### Step-by-Step Encryption

##### Pair 1: **HE**

| Letter | Position in Key Matrix | Replaced with |
|--------|------------------------|---------------|
| **H**  | (3rd row, 1st column)   | **I**         |
| **E**  | (1st row, 2nd column)   | **B**         |

So, **HE** becomes **IB**.

##### Pair 2: **LX**

| Letter | Position in Key Matrix | Replaced with |
|--------|------------------------|---------------|
| **L**  | (3rd row, 4th column)   | **K**         |
| **X**  | (5th row, 3rd column)   | **K**         |

So, **LX** becomes **KK**.

##### Pair 3: **LO**

| Letter | Position in Key Matrix | Replaced with |
|--------|------------------------|---------------|
| **L**  | (3rd row, 4th column)   | **F**         |
| **O**  | (4th row, 2nd column)   | **Q**         |

So, **LO** becomes **FQ**.

#### Final Encrypted Message
After encrypting all pairs:
    HE becomes IB.
    LX becomes KK.
    LO becomes FQ.

Since we're using the first part of the message, The final encrypted message for **HELLO** becomes **IBKKF**.







---
# Additional Challenge:
1. Modify the code to allow decryption as well.
2. Try allowing the user to input custom rules for handling repeated letters in pairs (e.g., allowing custom padding characters).