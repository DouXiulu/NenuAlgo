"""
题目描述
设n×n阶矩阵A和B，计算C=A×B。
输入
输入有多组数据，每组数据占3行，第一行为正整数n，1 < n <1000，表示n阶。第二行为A矩阵的nn个整数，第三行还是nn个整数，为B矩阵（先行后列形式存放）。
输出
按行列形式输出矩阵C。两个矩阵用空行隔开。
样例输入 复制
2
1 2 3 4
3 4 1 2
3
1 2 3 4 5 6 7 8 9
2 1 1 3 2 1 1 2 3
样例输出 复制
5 8
13 20

11 11 12
29 26 27
47 41 42
"""

import sys

try:
    outputs = [line.strip() for line in sys.stdin if line.strip()]
    for i in range(0,len(outputs),3):
        if i+1 > len(outputs) or i+2 > len(outputs):
            break
        
        n = int(outputs[i])
        A = list(map(int,outputs[i+1].split()))
        B = list(map(int,outputs[i+2].split()))
        
        new_A = []
        new_B = []

        ltA = []
        for i,a in enumerate(A):
            
            ltA.append(a)
            if (i+1) % n == 0:
                new_A.append(ltA)
                ltA = []

        ltB = []
        for i,b in enumerate(B):
            
            ltB.append(b)
            if (i+1) % n == 0:
                new_B.append(ltB)
                ltB = []
        
        print(new_A)
        print(new_B)




except Exception as e:
    info = sys.exc_info()

    print(f"{info[2].tb_lineno}:{e}")

