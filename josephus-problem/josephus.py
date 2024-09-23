def josephus(n, k):
    """
    Recursive function to find the position of the last remaining person.
    
    Parameters:
    n: Total number of people in the circle.
    k: Number of people to skip before eliminating one.

    Returns:
    The position of the last remaining person.
    """
    if n == 1:
        return 0  # Base case: If only one person is left, they are in position 0
    else:
        # Recursive case: Find the position in a smaller group, then adjust with the skip number
        return (josephus(n - 1, k) + k) % n

# Input for number of people (n) and the skip number (k)
n = int(input("Enter the number of people: "))
k = int(input("Enter the skip number: "))

# Convert the result to 1-based indexing by adding 1
last_person = josephus(n, k) + 1

# Output the result
print(f"The position of the last remaining person is: {last_person}")
