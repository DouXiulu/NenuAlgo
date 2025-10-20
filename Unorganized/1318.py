"""
题目描述
有5个人坐在一起，问第5个人多少岁？他说比第4个人大两岁。问第4个人的岁数，他说比第3个人大两岁。问第3个人的岁数，又说比第2个人大两岁。问第2个人的岁数，说比第1个人大两岁。最后问第1个人的岁数，他说是10岁。请问第5个人多少岁？
输入
输入有多行，每行3个整数，依次为m,n,k。m表示一共有几个人，n表示大的岁数，k表示第一个人的岁数。
输出
输出第m个人的岁数，每个一行。
样例输入 复制
5 2 10
样例输出 复制
18
"""


# 递归
def fun(m,n,k):
    if m == 1:
        return k
    else:
        return n + fun(m-1,n,k)

import sys

for line in sys.stdin:
    if line.strip():
        m,n,k = map(int,line.strip().split())
    print(fun(m,n,k))