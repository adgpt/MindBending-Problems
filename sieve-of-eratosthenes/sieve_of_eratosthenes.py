# Sieve of Eratosthenes approach to find prime numbers up to 'limit'

# Function to implement the Sieve of Eratosthenes
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)  # Boolean list to track prime status of each number
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    
    current_number = 2  # Start checking from the first prime number (2)
    
    while current_number * current_number <= limit:
        if is_prime[current_number]:  # If current_number is still marked as prime
            # Mark multiples of current_number as not prime
            for multiple in range(current_number * current_number, limit + 1, current_number):
                is_prime[multiple] = False
        current_number += 1  # Move to the next number
    
    # Collect all prime numbers into a list
    prime_numbers = [num for num in range(limit + 1) if is_prime[num]]
    
    return prime_numbers  # Return the list of prime numbers

# Take input from the user
limit = int(input("Enter the number up to which you want to find prime numbers (Sieve of Eratosthenes): "))
prime_numbers = sieve_of_eratosthenes(limit)  # Call the function
print("Prime numbers up to", limit, "are:", prime_numbers)  # Print the result
