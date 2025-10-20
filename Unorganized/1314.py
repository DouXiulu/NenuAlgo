import sys

def fun(n):
    return str(n)

results = []
for line in sys.stdin:
    if line.strip():
        n = int(line.strip())
    results.append(fun(n))
    
for res in results:
    print(" ".join(res))