# Naive approach to find prime numbers up to 'n'

# Function to find prime numbers up to 'n'
def naive_prime_check(n):
    primes = []  # Initialize an empty list to store prime numbers
    
    for num in range(2, n + 1):  # Loop through each number from 2 to n
        is_prime = True  # Assume the number is prime
        
        # Check divisibility from 2 up to sqrt(num)
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:  # If num is divisible by i, it's not prime
                is_prime = False
                break  # Exit the loop if we find a divisor
        
        # If the number is prime, add it to the primes list
        if is_prime:
            primes.append(num)
    
    return primes  # Return the list of prime numbers

# Take input from the user
n = int(input("Enter the number up to which you want to find prime numbers: "))
prime_numbers = naive_prime_check(n)  # Call the function
print("Prime numbers up to", n, "are:", prime_numbers)  # Print the result
