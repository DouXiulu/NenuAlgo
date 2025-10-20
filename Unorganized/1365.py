"""
题目描述
有N个非零且各不相同的整数。请你编一个程序求出它们中有多少对相反数（a和-a为一对相反数）。
输入
第一行包含一个正整数 N（1≤N≤500）。第二行为N个用单个空格隔开的非零整数，每个数的绝对值不超过1000，保证这些整数各不相同。
输出
只输出一个整数，即这N个数中包含多少对相反数。
样例输入 复制
5
1 2 3 -1 -2
样例输出 复制
2
"""

# n = int(input())
# lt = list(map(int,input().split()))

# # def fun(n):
# #     if n < 0:
# #         return -n
# #     else:
# #         return n

# d = {}
# for t in lt:
#     d[abs(t)] = d.get(abs(t),0) + 1

# # print(d)

# total = 0

# for value in d.values():
#     if value == 2:
#         total += 1
        
# print(total)