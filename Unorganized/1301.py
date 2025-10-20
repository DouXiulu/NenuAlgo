# 最大公约数
def fun(a, b):
    # 找出较小的数
    smaller = min(a, b)
    
    # 从较小的数开始往下找，找到的第一个公约数就是最大公约数
    for i in range(smaller, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

results = []

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    results.append(fun(a, b))

for res in results:
    print(res)