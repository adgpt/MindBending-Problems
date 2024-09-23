def josephus(n, k):
    """
    Function to simulate the Josephus problem with step-by-step elimination.

    Parameters:
    n: Total number of people in the circle
    k: Number of people to skip before eliminating one.

    Returns:
    The position of the last remaining person.
    """
    people = list(range(1, n + 1))  # Create a list of people numbered from 1 to n
    index = 0  # Starting index

    # Loop until only one person is left
    while len(people) > 1:
        # Find the index of the person to be eliminated
        index = (index + k - 1) % len(people)
        eliminated = people.pop(index)  # Remove the eliminated person
        # Display the current state of the circle after elimination
        print(f"Eliminated: {eliminated}, Remaining people: {people}")

    # Return the last remaining person
    return people[0]

# Input for number of people (n) and the skip number (k)
n = int(input("Enter the number of people: "))
k = int(input("Enter the skip number: "))

# Call the Josephus function and display the result
last_person = josephus(n, k)

# Output the result
print(f"The position of the last remaining person is: {last_person}")
