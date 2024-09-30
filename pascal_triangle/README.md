
# Pascal’s Triangle

## Problem Description
Pascal’s Triangle is a triangular array where each entry is the sum of the two directly above it. It starts with a single 1 at the top, and each subsequent row contains one more element than the previous. Each number is the sum of the two numbers directly above it in the triangle.

### Formula:
The value of a cell in Pascal’s Triangle can be computed using the formula:

\[ \text{Pascal}(n, k) = \frac{n!}{k!(n-k)!} \]

Where:
- \(n\) is the row number
- \(k\) is the column index (starting from 0)

### Example:
```
Input: 5
Output:
    1    
   1 1   
  1 2 1  
 1 3 3 1 
1 4 6 4 1
```

## Concepts
- **Recursion**: Pascal’s Triangle can be constructed recursively by building the rows based on the previous ones.
- **Combinatorics**: Each element in Pascal’s Triangle represents the binomial coefficient.

---

## Pascal's Triangle Implementation

In this repository, we provide a Python-based solution for generating Pascal's Triangle for a given number of rows.

---

## References
- Pascal's Triangle: [Wikipedia](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
- Python Docs: [Python Recursion](https://docs.python.org/3/tutorial/datastructures.html#recursion)
