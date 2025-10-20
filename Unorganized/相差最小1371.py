"""
题目描述
有一个整数序列，所有元素均不相同，设计一个算法求相差最小的元素对的个数。如序列 4、1、2、3 的相差最小的元素对的个数是 3，其元素对是（1，2），（2，3），（3，4）。
输入
输入有两行，第一行为正整数n（1<n<1000），第二行为n个整数，空格隔开。
输出
输出相差最小的元素对个数。
样例输入 复制
4
4 1 2 3
样例输出 复制
3

"""


try:
    n = int(input())
    
    lt = list(map(int,input().split()))
    
    lt.sort()
    
    
    minx = float("inf")  # 极大值
    count = 0
    
    for i in range(1,len(lt)):
        currentx = lt[i] - lt[i-1]
        if currentx < minx:
            minx = currentx
            count = 1  # 归为1
        elif currentx == minx:
            count += 1
    
    print(count)
    
except Exception as e:
    print(e)