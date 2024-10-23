# Sieve of Eratosthenes

## Problem Statement:
Find all prime numbers up to a given number `n`. A prime number is a number greater than `1` that has no divisors other than `1` and itself. The goal is to efficiently generate all prime numbers up to `n`.

## Understanding the Sieve of Eratosthenes:
The Sieve of Eratosthenes is a classic algorithm for finding prime numbers. It works by marking the multiples of each prime starting from 2, which helps eliminate non-prime numbers efficiently.

### How It Works:
1. We can start by creating a list where all numbers are marked as `True`, indicating they are potentially `prime`.
2. Starting with the number `2` (the first prime) we can mark all its multiples as `False` because they cannot be `prime`.
3. Then move to the next unmarked number, and repeat the process.
4. Stop when we reach the `square root of n`—by then, all non-prime numbers have been marked.
5. Finally, the numbers that remain marked as `True` are the primes.

## Implementation Logic
### Approach 1: The Naive Method 
1. The simplest way to find prime numbers is by checking whether each number is divisible by any number less than itself. If it is, it’s not prime. 
2. This method is slow but helps in understanding how prime-checking works.

### Approach 2: Sieve of Eratosthenes (Efficient Solution)
1. Create a boolean list where each index represents whether a number is `prime` (`True` means `prime`. Simple.)
2. Mark `0` and `1` as `False` since they are not prime.
3. Start from the first prime (`2`), and mark all its multiples as `False`.
4. Move to the next number in the list and repeat until the `square root of n`.
5. Collect all numbers still marked as `True`, which are our prime numbers.

---
## Example Input and Output:
Input:
```
n = 30
```

Output:
```
Prime numbers up to 30 are: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```
---
## Future Modifications:
* Modify the algorithm to find prime numbers between two numbers, a and b.
* Implementing a segmented version of the Sieve of Eratosthenes, which can handle larger numbers more efficiently.