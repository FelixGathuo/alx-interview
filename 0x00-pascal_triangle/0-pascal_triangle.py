#!/usr/bin/python3
def pascal_triangle(n):
  '''A function that creates a list of lists of integers
    in the Pascal's triangle of an integer n.
    '''
  triangle = []
  for i in range(n):
    if i == 0:
      triangle.append([1])
    else:
      triangle.append([1] + [triangle[i-1][j] + triangle[i-1][j+1] for j in range(len(triangle[i-1])-1)] + [1])
  return triangle
