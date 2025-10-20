n = int(input().strip())

def C(m,n):
    if n == 1:
        return m
    elif m < 0 or n < 0 or m < n:
        return 0
    elif m == n:
        return 1
    else:
        return C(m-1,n)+C(m-1,n-1)

results = []
for _ in range(n):
    m,n = map(int,input().strip().split())
    results.append(C(m,n))
    

for res in results:
    print(res)