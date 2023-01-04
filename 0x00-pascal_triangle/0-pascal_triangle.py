#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate a Pascal triangle of n rows.
    
    Args:
    n: int, the number of rows in the triangle.
    
    Returns:
    triangle: list of lists, the Pascal triangle.
    """
    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            row = [1]
            for j in range(i - 1):
                row.append(triangle[i-1][j] + triangle[i-1][j+1])
            row.append(1)
            triangle.append(row)
    return triangle
  
