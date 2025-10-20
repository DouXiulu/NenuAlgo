import sys

def fun(n):
    num = str(n)
    return num[::-1]
    
    
    
    
results = []
for line in sys.stdin:
    if line.strip():
        n = int(line.strip())
    results.append(fun(n))

for res in results:
    print(" ".join(res))