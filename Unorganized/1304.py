"""
题目描述
已知e=1/0!+1/1!+1/2!+…+1/n!，给定n就可以求出e。
输入
输入有多行，每行是一个整数n（n<10000）。
输出
输出对应的e，要求保留小数点7位。
样例输入 复制
1
2
样例输出 复制
2.0000000
2.5000000
"""

import sys

#求e
def fun(n):
    e = 0.0
    f = 1
    for i in range(n+1):
        if i > 0:
            f *= i
        e += 1/f
    return e


results = []

for line in sys.stdin:
    n = int(line.strip())
    results.append(fun(n))
    
for res in results:
    print(f"{res:.7f}")