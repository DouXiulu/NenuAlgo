"""
题目描述
输入两个非负整数a和b，请编写程序求出他们的最大公约数（要求尝试使用不同的求法来求解）。
输入
第一个数n表示测试数据的个数，接下来的n行每行有两个整数a和b，空格隔开。
输出
输出n行，每行输出对应a，b的最大公约数。
样例输入 复制
3
12 8
25 10
21 63
样例输出 复制
4
5
21

"""

n = int(input())


for _ in range(n):
    a,b = map(int,input().strip().split())
    
    maxn = 1
    if a < b:
        for i in range(2,a+1):
            if a % i == 0 and b % i == 0:
                maxn = i
    else:
        for i in range(2,b+1):
            if b % i == 0 and a % i == 0:
                maxn = i
    print(maxn)
        