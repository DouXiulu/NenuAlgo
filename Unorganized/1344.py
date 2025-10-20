"""
题目描述
有两个已排序好的序列A（长度为n1），B（长度为n2），将它们合并为一个有序的序列C（长度为n=n1+n2)。0 < n1,n2 < 1000。
输入
输入有多组测试数据，每组占两行，第一行为A序列（均为正整数），最后为-1，表示结束。第二行为B序列（均为正整数），最后为-1，表示结束。
输出
输出合并后的序列C，每组占一行。
样例输入 复制
1 3 8 9 11 -1
2 5 7 10 13 -1
样例输出 复制
1 2 3 5 7 8 9 10 11 13
"""

# import sys
# try:


# except Exception as e:
#     # 获取错误发生的行号
#     info = sys.exc_info()
#     print(f"{info[2].tb_lineno}: {e}")


# import sys
# try:
    
    
    
    
    
# except Exception as e:
#     info = sys.exc_info
#     print(f"{info[2}.tb_lineno:{e}")


import sys
try:
    def merge(a,b):
        result = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        result += a[i:]
        result += b[j:]
        return result
        
    
    results = []
    lines = [line.strip() for line in sys.stdin if line.strip()]
    for i in range(0,len(lines),2):
        a = list(map(int,lines[i].split()))[:-1]
        b = list(map(int,lines[i+1].split()))[:-1]
        results.append(merge(a,b))
    
    
    for res in results:
        print(" ".join(map(str,res)))
    
 
except Exception as e:
    info = sys.exc_info
    print(f"{info[2].tb_lineno}:{e}")