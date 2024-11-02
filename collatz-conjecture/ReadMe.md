# Collatz Conjecture

## Problem Statement

The Collatz Conjecture, sometimes called the `3n + 1` problem, is a famous mathematical problem that deals with sequences generated from positive integers. Given any positive integer:
1. If the number is `even`, divide it by `2`.
2. If the number is `odd`, multiply it by `3` and add `1`.

Repeat these steps until the number reaches 1. The conjecture claims that no matter which positive integer you start with, you will eventually reach 1.

### Objective

Create a Python program that:
- Accepts a positive integer input from the user.
- Generates and displays the sequence of numbers produced according to the Collatz Conjecture.
- Counts and displays the total number of steps taken to reach 1.

## Example

### Sample Input
```bash
Enter a positive integer: 6
```
### Sample Output
```bash
Collatz sequence for 6: 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 Total steps: 8
```

## How It Works
The Collatz Conjecture process is simple:
1. **Start with an integer** - Based on whether it's even or odd, you will perform one of two operations.
2. **Generate the sequence** - Continue applying the even/odd rule to each resulting number until you reach 1.
3. **Count the steps** - Track the number of steps it takes to arrive at 1.


---


### Additional Challenge
- Extending the program to find which integer (within a user-defined range) has the longest Collatz sequence.



### Note
This conjecture is unsolved in mathematics, meaning that while every tested number has eventually reached 1, no proof has been provided that this will happen for all positive integers.