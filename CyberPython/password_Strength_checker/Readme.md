
# Problem: Password Strength Checker

**Difficulty:** Easy/Medium

You are tasked with implementing a function to evaluate the strength of a password based on a set of predefined criteria.

Given a password as a string, implement a function that classifies the password into three categories: "Weak", "Medium", or "Strong". The classification is based on fulfilling several conditions described below:

### A password is considered "Strong" if it satisfies **all** the following conditions:
1. It has at least 8 characters.
2. It contains both lowercase (`a-z`) and uppercase letters (`A-Z`).
3. It contains at least one digit (`0-9`).
4. It contains at least one special character from the set `!@#$%^&*(),.?":{}|<>`.
5. It is not a common weak password from the list `["password", "123456", "qwerty", "abc123", "letmein"]`.

### A password is considered "Medium" if it satisfies **at least three** of the conditions above.

### A password is considered "Weak" if it satisfies **less than three** of the conditions.

### Task:
Write a function `checkPasswordStrength(password: str) -> str` that returns:
- `"Strong"` if the password meets all the conditions.
- `"Medium"` if it meets at least three conditions.
- `"Weak"` if it meets less than three conditions.

### Example 1:
**Input:**
```python
password = "StrongP@ssw0rd"
```
**Output:**
```python
"Strong"
```
**Explanation:**
The password has a length of 13 characters, contains uppercase and lowercase letters, includes digits, and has special characters. It also isn't in the list of common passwords.

### Example 2:
**Input:**
```python
password = "12345"
```
**Output:**
```python
"Weak"
```
**Explanation:**
The password has fewer than 8 characters and does not meet any of the required conditions.

### Example 3:
**Input:**
```python
password = "password123"
```
**Output:**
```python
"Medium"
```
**Explanation:**
The password is longer than 8 characters and contains digits, but it does not have special characters or a mix of uppercase and lowercase letters. However, it is also a common password, which makes it less secure.

### Constraints:
- The password string `password` consists of printable ASCII characters.
- Password length is between `1 <= len(password) <= 1000`.

---

### Notes:
- Your solution should evaluate the password against all the criteria and return the appropriate classification.
- The common passwords are considered inherently weak, even if they meet the other conditions.
