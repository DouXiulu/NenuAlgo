def convert_to_matrix(numbers_str, n):
    # 将输入的数字串分割成列表
    numbers_list = numbers_str.split()
    
    # 将字符串列表转换为整数列表
    numbers_int = [int(num) for num in numbers_list]
    
    # 将整数列表转换为n x n的矩阵
    matrix = [numbers_int[i * n:(i + 1) * n] for i in range(n)]
    
    return matrix

# 示例使用
n = 2  # 假设矩阵维度为2x2
numbers_str = "1 2 3 4"  # 输入的数字串
matrix = convert_to_matrix(numbers_str, n)
print(matrix)
for row in matrix:
    print(row)
