"""
题目描述
一个顾客买了价值x元的商品，并将y元的钱交给售货员。售货员希望用张数最少的钱币找给顾客。
无论买商品的价值x是多大，找给他的钱最多需要以下六种币值：50，20，10，5，2，1。
输入
输入有多组，每组有两个正整数x和y。


输出
每行给出零钱的张数。


样例输入 复制
1 10
21 100
样例输出 复制
5 yuan: 1
2 yuan: 2

50 yuan: 1
20 yuan: 1
5 yuan: 1
2 yuan: 2
"""


# 暴力
import sys

yuan = [50, 20, 10, 5, 2, 1]


results = []
for line in sys.stdin:
    if line.strip():
        x, y = map(int,line.strip().split())
    
    zhaoqian = y - x
    
    res = []
    for qian in yuan:
        if zhaoqian >= qian:
            res.append(f"{qian} yuan: {zhaoqian // qian}")
            zhaoqian %= qian
    results.append(res)

print(results)
for i,res in enumerate(results):
    print("\n".join(res))
    if i != len(results) - 1:
        print()