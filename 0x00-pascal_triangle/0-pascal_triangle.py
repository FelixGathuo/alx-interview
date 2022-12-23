#!/usr/bin/python3
def pascal_triangle(n):
	result_list = []
	if n <= 0:
		return []

	for i in range(n):
		result_list.append(str(11**i))

	return (result_list)
