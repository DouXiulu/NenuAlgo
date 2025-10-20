import sys
try:
    # 杨辉三角
    def fun(n):
        sanjiao = []
        
        for i in range(n):
            hsanjiao = []
            for j in range(i+1):
                if i == j or j == 0:
                    hsanjiao.append(1)
                else:
                    hsanjiao.append(sanjiao[i-1][j]+sanjiao[i-1][j-1])
            
            sanjiao.append(hsanjiao)
        
        return sanjiao
        
    
    results = []
    for line in sys.stdin:
        if line.strip():
            n = int(line.strip())
            results.append(fun(n))
            
    for res in results:
        for hsanjiao in res:
            print(" ".join(map(str,hsanjiao)))
        print()
    
except Exception as e:
    info = sys.exc_info()
    print(f"{info[2].tb_lineno}:{e}")