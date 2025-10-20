import sys
try:
    n = int(input())

    total = 0
    for i in range(1,n+1):
        b = 1
        for j in range(1,j+1):
            b *= j
        total += b
    print(total)


except Exception as e:
    # 获取错误发生的行号
    info = sys.exc_info()
    print(f"{info[2].tb_lineno}: {e}")