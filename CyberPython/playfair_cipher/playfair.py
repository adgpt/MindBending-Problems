# Step 1: Create a key matrix using the keyword
def generate_key_matrix(keyword):
    keyword = keyword.replace('J', 'I').upper()  # Replace 'J' with 'I'
    key_matrix = []
    used_letters = set()

    # Add letters from the keyword first
    for letter in keyword:
        if letter not in used_letters and letter.isalpha():
            key_matrix.append(letter)
            used_letters.add(letter)

    # Fill the rest of the matrix with other letters from the alphabet (excluding 'J')
    for letter in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':  # No 'J' in Playfair cipher
        if letter not in used_letters:
            key_matrix.append(letter)

    # Create a 5x5 grid
    matrix_5x5 = [key_matrix[i:i + 5] for i in range(0, 25, 5)]
    return matrix_5x5

# Step 2: Display the matrix for the user
def display_matrix(matrix):
    print("Playfair Cipher Key Matrix:")
    for row in matrix:
        print(" ".join(row))
    print("\n")

# Step 3: Prepare the message for encryption (pair the letters)
def prepare_text(message):
    message = message.replace('J', 'I').upper()
    prepared_text = []
    i = 0
    while i < len(message):
        a = message[i]
        if i + 1 < len(message):
            b = message[i + 1]
        else:
            b = 'X'  # Add 'X' if there's no pair

        if a == b:
            prepared_text.append(a + 'X')
            i += 1
        else:
            prepared_text.append(a + b)
            i += 2

    if len(prepared_text[-1]) == 1:
        prepared_text[-1] += 'X'  # Padding if odd number of characters
    return prepared_text

# Step 4: Find position of each letter in the matrix
def find_position(letter, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col

# Step 5: Encrypt the pairs using Playfair rules
def encrypt_pair(pair, matrix):
    row1, col1 = find_position(pair[0], matrix)
    row2, col2 = find_position(pair[1], matrix)

    # Case 1: Same row
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    
    # Case 2: Same column
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]

    # Case 3: Rectangle swap
    else:
        return matrix[row1][col2] + matrix[row2][col1]

# Step 6: Encrypt the message
def encrypt_message(message, keyword):
    matrix = generate_key_matrix(keyword)
    display_matrix(matrix)
    prepared_text = prepare_text(message)
    encrypted_message = ""

    for pair in prepared_text:
        encrypted_message += encrypt_pair(pair, matrix)

    return encrypted_message

# Example usage
message = input("Enter the message to encrypt: ")
keyword = input("Enter the keyword: ")

encrypted_message = encrypt_message(message, keyword)
print("Encrypted Message:", encrypted_message)
