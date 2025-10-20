import sys
try:
    # 是否为素数
    def fun(m):
        flag = 0
        for i in range(2,m):
            if m % i == 0:
                flag = 1
                break
        if flag:
            return "not prime"
        else:
            return "prime"
    
    results = []
    for line in sys.stdin:
        if line.strip():
            m = int(line.strip())
            results.append(fun(m))
            
    for res in results:
        print(res)
            
except Exception as e:
    info = sys.exc_info()
    print(f"{info[2].tb_lineno}:{e}")