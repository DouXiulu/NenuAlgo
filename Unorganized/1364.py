"""
题目描述
判断字符串str中每个字符是否唯一。
输入
输入为一行字符串，里面只有字母和数字。
输出
判断里面所有的字母是否唯一，如果唯一输出true，否则输出false。
样例输入 复制
abc
样例输出 复制
true
"""

# def is_unique(s):
#     s = set(s)
#     if len(s) == len(s):
#         return True
#     else:
#         return False



import sys
try:
    lines = [line.strip() for line in sys.stdin if line.strip()]
    
    results = []
    for i in range(0,len(lines),2):
        if (i+1) >= len(lines):
            break
        n = lines[i]
        lt = list(map(int,lines[i+1].split()))
        
        s = set(lt)
        
        if n == len(s):
            results.append("true")
        else:
            results.append("false")
            
    print("\n".join(results))
    
except Exception as e:
    info = sys.exc_info()
    print(f"{info[2].tb_lineno}:{e}")        
