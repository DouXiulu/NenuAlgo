# import sys

# def fun(n):
#     jihe = set()
#     for i in range(1, n+1):
#         j = n - i
#         if j > 0:
#             pair = tuple(sorted((i, j)))  # 使用元组且排序来消除重复

#             # # 把较小的数放前面，避免重复（如2+3和3+2视为相同）
#             # pair = (min(i, j), max(i, j))
#             jihe.add(pair)
#     return len(jihe)

# results = []
# for line in sys.stdin:
#     if line.strip():
#         n = int(line.strip())
#         results.append(fun(n))

# for res in results:
#     print(res)


"""
题目描述
对于一个正整数n的分划就是把n写成一系列正整数之和的表达式。例如，对于正整数n=6，它可以分划为：

6 5+1 4+2, 4+1+1 3+3, 3+2+1, 3+1+1+1 2+2+2, 2+2+1+1, 2+1+1+1+1 1+1+1+1+1+1，一共有11种，其中5+1和1+5被认为是同样的。

输入
输入有多组数据，每行为一个正整数n(n < 50)。
输出
对于每组输入，输出有多少种整数划分的方法。
样例输入 复制
1
6
样例输出 复制
1
11

"""

# max_n = 2
# dp = [[0] * (max_n + 1) for _ in range(max_n + 1)]

# print(dp)


import sys

max_n = 50

db = [[0] * (max_n+1) for _ in range(max_n+1)]

# 0....49
for j in range(max_n):
    db[0][j] = 1  # 拆0就1种情况
    
for num in range(1,max_n+1):  # num is 要拆的数
    for max_use in range(1,num+1):
        db[num][max_use] = db[num][max_use-1] + db[num-max_use][max_use]
    for max_use in range(num+1,max_n+1):
        db[num][max_use] = db[num][num]

results = []
for line in sys.stdin:
    if line.strip():
        n = int(line.strip())
    results.append(db[n][n])

for res in results:
    print(res)
        