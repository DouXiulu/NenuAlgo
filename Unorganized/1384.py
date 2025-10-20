# 1384

import sys
try:
    lines = [line.strip() for line in sys.stdin if line.strip()]
    

    for i in range(0,len(lines),2):
        if i+1 >= len(lines):
            break
        
        n = int(lines[i])
        lt = list(map(int,lines[i+1].split()))
        print(n,lt)
        
        number = 0
        n1 = lt[0]
        flag = 0
        for i in range(1,len(lt)):
            if n1 == lt[i] and not flag:
                n1 = lt[i]
            else:
                flag = 1
                number += 1
                n1 = lt[i]
        print(number)
        
except Exception as e:
    print(f"{e}")