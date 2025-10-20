"""
题目描述
例如，28的因子为1、2、4、7，14，而28=1+2+4+7+14。因此28是“完数”。编程判断完数。
输入
输入有多行，每行一个正整数。
输出
对于每行的正整数判断是否是完数，是则输出：Yes，否则输出：No。
样例输入 复制
2
28
样例输出 复制
No
Yes
"""

import sys


def fun(n):
    lt = [1]
    for i in range(2,n):
        if n % i == 0:
            lt.append(i)
    if sum(lt) == n:
        return "Yes"
    else:
        return "No"
    

results = []
for line in sys.stdin:
    results.append(fun(int(line.strip())))
    
print("\n".join(results))