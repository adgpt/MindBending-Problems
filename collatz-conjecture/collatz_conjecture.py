# Collatz Conjecture Program
# This program calculates and displays the Collatz sequence for a given positive integer
# It also counts the total number of steps taken to reach 1

# Get user input and ensure it's a positive integer
number = int(input("Enter a positive integer: "))

# Initialize variables
current_number = number
step_count = 0  # to count the number of steps
sequence = []  # list to store the sequence

# Generate the Collatz sequence
while current_number != 1:
    sequence.append(current_number)  # add the current number to the sequence
    
    # Apply the Collatz rule
    if current_number % 2 == 0:  # if current number is even
        current_number //= 2
    else:  # if current number is odd
        current_number = current_number * 3 + 1
    
    # Increment step count
    step_count += 1

# Add the final 1 to the sequence
sequence.append(1)

# Display the results
print("\nCollatz sequence for {}:".format(number))

# Manually create the formatted sequence string without using map()
formatted_sequence = ""
for i in range(len(sequence)):
    formatted_sequence += str(sequence[i])
    if i < len(sequence) - 1:  # add arrow only between numbers, not after the last number
        formatted_sequence += " → "

print(formatted_sequence)
print("Total steps:", step_count)
