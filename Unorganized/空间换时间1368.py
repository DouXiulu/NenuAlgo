"""
题目描述
有一个整数序列，判断其中是否存在两个元素和恰好等于给定的整数 k。
输入
输入有两行，第一行为正整数n（1<n<1000）和整数k，第二行为n个整数。
输出
如果这n个整数中存在两个数的和等于k，则输出Yes，否则输出No。
样例输入 复制
3 5
4 1 5
样例输出 复制
Yes

"""

# import sys

# try:

#     n, k = map(int,input().split())
    
#     lt = list(map(int,input().split()))
    
#     flag = 0
    
#     for i in range(len(lt)):
#         for j in range(i+1,len(lt)):
#             if lt[i] + lt[j] == k:
#                 flag = 1
#                 break
            
#     if flag:
#         print("Yes")
#     else:
#         print("No")
        
# except Exception as e:
#     print(e)


import sys

try:
    n, k = map(int, input().split())
    lt = list(map(int, input().split()))
    
    seen = set()
    flag = 0
    for num in lt:
        if (k - num) in seen:
            flag = 1
            break
        seen.add(num)
    
    print("Yes" if flag else "No")
    
except Exception as e:
    print(e)