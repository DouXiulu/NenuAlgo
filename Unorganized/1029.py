"""
题目描述
求素数的和。
输入
输入文件有很多行，每行包含一些正整数（零或负数表示结束），要求统计其中的素数的和。
输出
每行输出一个和。
样例输入 复制
2 3 4 5 10 0
4 2 5 14 6 7 -3
样例输出 复制
10
14

"""


import sys

try:

    results = []
    for line in sys.stdin:
        lt = []
        total = 0
        if line.strip():
            lt = list(map(int,line.strip().split()))
            
        
        for t in lt:
            flag = 0
            if t <= 0:
                break
            if t == 1:
                continue
            else:
                for i in range(2,int(t**0.5)+1):
                    if t % i == 0:
                        flag = 1
                        break
                    
            if not flag:
                total += t
        results.append(total)
        
    for res in results:
        print(res)
        
except Exception as e:
    print(e)
            
                    
    
                        
