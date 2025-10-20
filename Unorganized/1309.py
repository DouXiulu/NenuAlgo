"""
题目描述
一个矩阵在行上最小而在列上最大的点就是该矩阵的鞍点。
输入
输入有多组，第一行为m,n(1 < m,n < 100 )，表示矩阵的行数和列数，接下来是m行输入，每行n个整数。
输出
分别输出鞍点所在的行号，列号，值，如果没有找到，输出no solution!
样例输入 复制
3 2
1 2
4 3
5 6
3 2
1 2
4 3
2 5
样例输出 复制
3 1 5
no solution!
"""

import sys

results = []

while True:
    header = sys.stdin.readline().strip()
    if header == '':
        break
    m, n = map(int, header.split())

    lt = []
    flag = 0

    for _ in range(m):
        new_lt = list(map(int,sys.stdin.readline().strip().split()))
        lt.append(new_lt)
            
    # print(lt)

    for i in range(m):
        for j in range(n):
            if lt[i][j] == min(lt[i]) and lt[i][j] == max([lt[k][j] for k in range(m)]):
                results.append([i+1, j+1, lt[i][j]])
                flag = 1
                break
        if flag:
            break
            

    if not flag:
        results.append('no solution!')

# print(results)
for res in results:
    if res != "no solution!":
        print(f"{res[0]} {res[1]} {res[2]}")
    else:
        print(res)
        
