"""
题目描述
已知n，求 1/1!-1/3!+1/5!-1/7!+…+(-1)^(n+1)/(2n-1)! 的值。
输入
输入有多组整数n（0 < n <11），每行只有一个n。
输出
输出相应的值，每个一行，保留小数点5位。
样例输入 复制
1
2
样例输出 复制
1.00000
0.83333


"""


# 循环与递归
def fun(n):
    f = -1
    num = 0.0
    for i in range(1,2*n-1+1,2):
        flag = -1
        f *= i
        # print(f"qian{f}")
        # print(f"test{f*flag}")
        f *= flag
        # print(f"hou{f}")
        num += 1/f
    return num
        
    
    

import sys

results = []
for line in sys.stdin:
    n = int(line.strip())
    results.append(fun(n))
    
for res in results:
    print(f"{res:.5f}")
    