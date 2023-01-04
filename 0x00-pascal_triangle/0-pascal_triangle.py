def pascal_triangle(n):
  triangle = []
  for i in range(n):
    if i == 0:
      triangle.append([1])
    else:
      triangle.append([1] + [triangle[i-1][j] + triangle[i-1][j+1] for j in range(len(triangle[i-1])-1)] + [1])
  return triangle
