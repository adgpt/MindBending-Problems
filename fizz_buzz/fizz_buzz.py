# Ask the user for input: how many numbers they want to check
n = int(input("Enter the number up to which FizzBuzz should run: "))

# Loop through numbers from 1 to n
for i in range(1, n + 1):
    
    # If the number is divisible by both 3 and 5, print "FizzBuzz"
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    
    # If the number is divisible by 3, print "Fizz"
    elif i % 3 == 0:
        print("Fizz")
    
    # If the number is divisible by 5, print "Buzz"
    elif i % 5 == 0:
        print("Buzz")
    
    # If the number is not divisible by 3 or 5, just print the number
    else:
        print(i)
