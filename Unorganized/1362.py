import sys
try:
    string = input()
    
    d = {"(":")"}
    
    lt = []
    flag = 0
    for s in string:
        if s == "(":
            lt.append(s)
        if s == ")":
            if lt and s == d[lt[-1]]:
                lt.pop()
            else:
                flag = 1
                break
    
    if flag or lt:
        print("NO")
    else:
        print("YES")
                
except Exception as e:
    print(e)