## What's the Josephus Problem?
The **Josephus Problem** is a famous puzzle that comes up in math and computer science. Imagine a group of people standing in a circle, and every `k`th person is eliminated until only one remains. The challenge is to figure out where to stand to be the last person left.

The story behind the problem dates back to the **Jewish-Roman War**, where a group of soldiers used a similar method to avoid being captured. It’s a quirky, old problem that still teaches us a lot about **modular arithmetic** and how to break complex problems into smaller chunks.

### What is Recursion?
At its core, **recursion** is a way of solving problems by having a function call itself. It’s like breaking a big task into smaller tasks. When one small task is done, the solution to the big one naturally follows. This approach is perfect for problems like Josephus, where you can reduce the number of people step by step until you're left with one.

Think of recursion like peeling an onion—each layer you peel brings you closer to the core, which is the solution.

---

## 2. Python-Based Solution
* Refer to the attached Python Files. 
---

## 3. Algorithm

### Step 1: Base Case (n = 1)
The smallest group is when only 1 person remains. In this case, that person is naturally the last one left. So if `n == 1`, we return position `0`. This is the core of our recursive function.

### Step 2: Recursive Step
When there is more than one person (`n > 1`), we call the function again with `n-1` people and adjust the result using the skip number `k`. This part is key. The position in the reduced group needs to be adjusted to reflect the elimination order in the original group. This adjustment is done using the formula:

```
(josephus(n-1, k) + k) % n
```

This ensures we always get the correct position of the last person remaining.

### Step 3: Adjust for 1-Based Indexing
Python uses **0-based indexing**, but in real-world problems like Josephus, people often use **1-based indexing** (counting from 1). So, after solving the problem with 0-based indexing, we simply add 1 to get a more human-friendly answer.

### Step 4: Display the Result
Once the calculation is complete, we print the position of the last remaining person.

---

## 4. Sample Input, Output, and Processing

### Sample Input:
```
Enter the number of people: 5
Enter the skip number: 2
```

### Sample Output:
```
The position of the last remaining person is: 3
```

### How it Works (Processing):
- **Initial group**: 5 people (labeled 1, 2, 3, 4, 5).
- **Skip number**: Every 2nd person is eliminated.
- **Elimination order**: The people are eliminated in this order: 2, 4, 1, 5.
- **Last person remaining**: Person 3 is the last one left standing.

---

### References
- [Josephus Problem on Wikipedia](https://en.wikipedia.org/wiki/Josephus_problem)
- Recursion basics explained in [GeeksforGeeks Recursion Tutorial](https://www.geeksforgeeks.org/recursion/)
