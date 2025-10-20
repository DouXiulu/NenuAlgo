"""
题目描述
给定个n，要求输出n行号，号的个数与行号相同。
输入
每行有一个整数n（1<=n<=100),一直到文件尾。
输出
对于每个整数n，要求输出n行*号，具体样式见输出样例。
样例输入 复制
3
1
样例输出 复制
*
**
***

*

"""


import sys
def fun(n):
    str_lt = []
    for i in range(n):
        str_lt.append(((i+1)*"*"))
    return str_lt
    


results = []
for line in sys.stdin:
    if line.strip():
        n = int(line.strip())
    results.append(fun(n))


# print(results)
for idx,res in enumerate(results):
    print("\n".join(res))
    if idx != len(results) - 1:
        print()
