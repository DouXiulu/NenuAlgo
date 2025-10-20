import sys

def fun(n):
    str_lt = []
    for i in range(n):
        string = " " * (n-(i+1)) + "*" * (((i+1)*2)-1)
        str_lt.append(string)
    return str_lt
    

results = []
for line in sys.stdin:
    if line.strip():
        n = int(line.strip())
    results.append(fun(n))
    
for idx,values in enumerate(results):
    print("\n".join(values))
    if idx != len(results) - 1:
        print()