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

# Explanation of the code:
# 1. The function 'josephus' takes two parameters: 'n' (the number of people) and 'k' (the step count).
# 2. It initializes a list 'people' with numbers from 1 to n, representing each person in the circle.
# 3. The variable 'index' is set to 0, indicating the starting position.
# 4. The while loop continues until only one person remains in the list.
# 5. Inside the loop, it calculates the index of the person to eliminate using the formula:
#    (current index + k - 1) % length of people. This handles the circular aspect of the problem.
# 6. The 'pop' method removes the person at the calculated index and returns the eliminated person.
# 7. The current state of the elimination process is printed to show which person was eliminated and who remains.
# 8. Once the loop ends, the last person remaining in the list is returned.
# 9. The user is prompted to input the number of people and the step count.
# 10. The function is called with these inputs, and the position of the last person is printed.
