# 题目
"""
题目描述
斐波那契（Fibonacci，意大利数学家，1170年-1240年）数列，又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、……。这个数列从第三项开始，每一项都等于前两项之和。在现代物理、准晶体结构、化学等领域，斐波纳契数列都有直接的应用。
已知斐波那契数列第n项的计算公式如下。在计算时有两种算法：递归和非递归，请给出其中一种算法。
当n=0时，Fib(n)=0，当n=1时，Fib(n)=1，当n>1时，Fib(n)= Fib(n-1)+ Fib(n-2)。
输入
第一行是测试数据的组数m，后面跟着m行输入。每行包括一个项数n和一个正整数a。（m，n，a均大于0，且均小于10000000）。
输出
输出包含m行，每行对应一个输入，若a不大于Fib(n)，则输出Yes，否则输出No（中间没有空行）。
样例输入 复制
3
1 3
10 50
24 20000
样例输出 复制
No
Yes
Yes
"""



# 斐波那契数列
def fun(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

m = int(input())
results = []

for _ in range(m):
    n, a = map(int, input().split())
    fib_n = fun(n)
    results.append("Yes" if a <= fib_n else "No")

for res in results:
    print(res)