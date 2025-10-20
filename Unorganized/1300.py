# AC20%
"""
题目描述
按要求输出一个整数的每个位上的数字。
输入
每行只有一个整数a。
输出
对每个a输出一行，按照从低位到高位的顺序依次输出a每位上的数字，数字之间用逗号隔开。
样例输入 复制
1
12345
样例输出 复制
1 has one number,is 1
12345 have five numbers,are 5,4,3,2,1
"""


words = ["two", "three", "four", 
             "five", "six", "seven", "eight", "nine","Ten"]

def print_digits(a):
    # 将整数转换为字符串，方便逐字符处理
    a_str = str(a)
    # 获取数字的位数
    num_length = len(a_str)
    # 从低位到高位获取每位数字
    digits = [a_str[-i] for i in range(1, num_length + 1)]
    # 根据数字的位数选择单复数形式
    if num_length == 1:
        return f"{a} has one number,is {digits[0]}"
    else:
        return f"{a} have {words[num_length-2]} numbers,are {','.join(digits)}"

# 读取输入
inputs = []
# while True:
#     try:
#         line = input().strip()
#         if line:  # 确保不是空行
#             inputs.append(int(line))
#     except EOFError:
#         break

import sys

for line in sys.stdin:
    inputs.append(int(line.strip()))

#处理并输出结果
results = [print_digits(a) for a in inputs]
print('\n'.join(results))