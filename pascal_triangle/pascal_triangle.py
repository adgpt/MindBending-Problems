# Pascal's Triangle Generator in Python with Formatting

# Function to generate Pascal's Triangle up to n rows
def generate_pascals_triangle(num_rows):
    """
    Generate Pascal's Triangle up to the specified number of rows.

    Args:
    num_rows (int): The number of rows of Pascal's Triangle to generate.

    Returns:
    list: A list of lists representing Pascal's Triangle.
    """
    
    # Initialize an empty list to hold the triangle
    triangle = []

    # Loop through each row
    for row_num in range(num_rows):
        # Start each row with 1
        row = [1] * (row_num + 1)

        # Fill in the middle elements (if there are any)
        for j in range(1, row_num):
            # Each element is the sum of the two above it
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        # Append the completed row to the triangle
        triangle.append(row)

    return triangle


# Function to print Pascal's Triangle in a readable format
def print_pascals_triangle(triangle):
    """
    Print Pascal's Triangle in a nicely formatted way.

    Args:
    triangle (list): A list of lists representing Pascal's Triangle.
    """
    num_rows = len(triangle)
    
    # Determine the width of the last row to help center-align the triangle
    max_width = len(" ".join(map(str, triangle[-1])))
    
    for row in triangle:
        row_str = " ".join(map(str, row))
        # Center each row by padding spaces on both sides
        print(row_str.center(max_width))


# Driver code
if __name__ == "__main__":
    # Ask user for number of rows
    num_rows = int(input("Enter the number of rows for Pascal's Triangle: "))

    # Generate Pascal's Triangle
    triangle = generate_pascals_triangle(num_rows)

    # Print the triangle
    print_pascals_triangle(triangle)
