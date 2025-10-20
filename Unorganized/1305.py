"""
题目描述
给定一个整数N(0 ≤ N ≤ 10000)，要求计算N的阶乘。
输入
每个N占一行，直到文件尾。
输出
对于每个N，输出N的阶乘，占一行。
样例输入 复制
1
2
3
样例输出 复制
1
2
6
"""


import sys

#求N的阶乘
def fun(n):
    if n == 0:
        return 0
    else:
        num = 1
        for i in range(1,n+1):
            num *= i
        return num
        

results = []
for line in sys.stdin:
    n = int(line.strip())
    results.append(fun(n))

for res in results:
    print(res)