"""
题目描述
编写算法，打印具有下面规律的图形。


	


1
5 2
8 6 3
10 9 7 4



输入
输入有多组，每组一行，只有一个整数n（0<n<25）。
输出
按照指定格式输出。每组之间有一个空行。
样例输入 复制
1
4
样例输出 复制
1

1
5 2
8 6 3
10 9 7 4
"""
"""
import sys

def generate_pattern(n):
    # 生成每行的起始数字（每行第一个数）
    start_nums = [1]  # 第一行起始数字固定为1
    for k in range(1, n):
        # 计算第k+1行的起始数字（索引从0开始）
        # 规律：当前行起始值 = 前一行起始值 + (n - 前一行的索引)
        start_nums.append(start_nums[k-1] + (n - (k-1)))
    
    result = []
    # 生成每一行的数字序列
    for k in range(n):  # k表示当前行索引（0-based）
        current = start_nums[k]  # 当前行起始数字
        line = [str(current)]  # 初始化当前行内容
        
        # 生成当前行后续数字的递减规律
        decrement = n - k  # 初始递减步长
        for m in range(1, k+1):  # 每行需要生成k个数字（因为第一个数字已存在）
            current -= decrement  # 按当前步长递减
            line.append(str(current))
            decrement += 1  # 递减步长每次+1
        
        result.append(' '.join(line))  # 将当前行转换为字符串
    return result

# 读取所有输入（自动过滤空行，转换为整数列表）
inputs = [int(line.strip()) for line in sys.stdin if line.strip()]

# 处理并输出结果
for i, n in enumerate(inputs):
    # 生成当前测试用例的图案
    pattern = generate_pattern(n)
    # 输出图案内容
    print('\n'.join(pattern))
    
    # 在最后一个测试用例之后不输出空行
    if i != len(inputs)-1:
        print()  # 用例间用空行分隔
"""

import sys

def generate_pattern(n):
    a = [[0] * n for _ in range(n)]
    k = 1
    
    # 斜对角线填充
    for i in range(n):
        x, y = i, 0
        count = n - i
        while count > 0:
            a[x][y] = k
            x += 1
            y += 1
            k += 1
            count -= 1
    
    # 格式化输出
    result = []
    for i in range(n):
        line = ' '.join(map(str, [a[i][j] for j in range(i+1)]))
        result.append(line)
    return result

# 处理多组输入
inputs = [int(line.strip()) for line in sys.stdin if line.strip()]
for idx, n in enumerate(inputs):
    # 生成图案
    pattern = generate_pattern(n)
    # 输出结果
    print('\n'.join(pattern))
    # 测试用例间添加空行（最后一行不添加）
    if idx != len(inputs)-1:
        print()