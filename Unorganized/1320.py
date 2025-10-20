"""
题目描述
猴子第1天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个。第2天又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半另加一个。到第10天早上想再吃时，就只剩下一个桃子了。求第1天共摘了多少个桃子。
输入
输入第一行为正整数n，为测试数据组数。后面n行为测试数据，每组测试数据包括两个整数m，k，分别表示第m（m>1)天后剩余的桃子数k(k>=0)。
输出
输出猴子第一天摘的桃子数，每组数据占一行。
样例输入 复制
2
2  2
3  0
样例输出 复制
6
6

"""

import sys

def fun(m,k):
    total = 0
    half = k
    for _ in range(m-1):
        half = half+1
        half = half*2
    total = half
    return total
        
    

n = int(input().strip())

results = []
for _ in range(n):
    m, k = map(int,input().strip().split())
    results.append(fun(m,k))
    
for res in results:
    print(res)