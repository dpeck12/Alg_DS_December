matrix = [
    [112, 42, 83, 119], 
    [56, 125, 56, 49], \
    [15, 78, 101, 43], 
    [62, 98, 114, 108]
]

n = len(matrix)

half = n // 2

# Rows 
for i in range(n):
    left_quad_sum = sum(matrix[i][:half])
    reversed_left_quad_sum = sum(matrix[i][::-1][:half])

    if reversed_left_quad_sum > left_quad_sum:
        matrix[i].reverse()

# Columns 
for j in range(n):
    left_quad_sum = sum(matrix[i][j] for i in range(half))
    reversed_left_quad_sum = sum(matrix[i][j] for i in range(n-1, n-1-half, -1))

    if reversed_left_quad_sum > left_quad_sum:
        for i in range(half):
            matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]

return sum(matrix[:half][:half]) 