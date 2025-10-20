"""
题目描述
又到一年一度的期末考试了，老师最头痛的问题就是从一堆学生中统计不及格的人数，你快来帮忙吧。
输入
有多组测试用例，每组第一行是正整数N（0 < N < 201）,然后是N行数据，每行表示一个学生的学号和成绩，中间空格隔开。
输出
每组测试用例输出不及格（成绩<60）人数。
样例输入 复制
2
CS2015001 88
SW2013002 76
3
EN2014001 59
MA2015002 95
PH2013007 77
样例输出 复制
0
1

"""

import sys
try:
    lines = [line.strip() for line in sys.stdin if line.strip()]
    
    index = 0
    
    while index < len(lines):
        n = int(lines[index])
        total = 0

        index += 1  # !!!!!!!!!!!!
        
        for _ in range(n):
            if index > len(lines):
                break
            score = int(lines[index].split()[1])
            if score < 60:
                total += 1
            index += 1
        
        print(total)
except Exception as e:
    info = sys.exc_info()
    print(f"{info[2].tb_lineno}:{e}")