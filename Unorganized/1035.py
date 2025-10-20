# import sys

# # 读取所有输入行
# lines = [line.strip() for line in sys.stdin if line.strip()]
# # print(lines)
# idx = 0
# first_case = True  # 用于控制空行输出

# while idx < len(lines):
#     # 读取当前测试用例
#     n = int(lines[idx])
#     idx += 1
    
#     students = []
#     for _ in range(n):
#         students.append(lines[idx].split())
#         idx +=1
    
#     # 排序处理
#     sort_students = sorted(students, key=lambda x: int(x[2]), reverse=True)
#     # results = [sort_students[0], sort_students[-1]]
    
#     # 控制空行输出
#     if not first_case:
#         print()
#     first_case = False

#     # 输出结果
#     print(" ".join(sort_students[0]))
#     print(" ".join(sort_students[-1]))


"""
题目描述
又到一年一度的期末考试了，老师最头痛的问题就是从一堆学生中找最高分和最低分，你快来帮忙吧。


输入
测试数据有多组，每组首先是一个正整数n（0 < n < 31），接下来是n行数据，每行数据代表一个学生的成绩，分部为学生的姓名、学号、成绩。其中姓名和学号均为不超过10个字符的字符串，成绩为0到100之间的一个整数，这里保证在一组测试用例中没有两个学生的成绩是相同的。


输出
每组分两行输出成绩最高和成绩最低学生的姓名、学号和成绩，字符串间有1空格，两组之间用空行隔开。


样例输入 复制
3
Joe Math990112 89
Mike CS991301 100
Mary EE990830 95
2
Zhangsan SW9801 70
Lisi EN9801 59
样例输出 复制
Mike CS991301 100
Joe Math990112 89

Zhangsan SW9801 70
Lisi EN9801 59

"""

import sys

lines = [line.strip() for line in sys.stdin if line.strip()]

idx = 0

flag = 1

while idx < len(lines):
    n = int(lines[idx])
    idx += 1
    
    students = []
    for _ in range(n):
        students.append(lines[idx].split())
        idx += 1
    
    print(students)

    sort_students = sorted(students, key = lambda x:int(x[2]), reverse = True)
    
    print(sort_students)

    if not flag:
        print()
    flag = 0
    
    print(" ".join(sort_students[0]))
    print(" ".join(sort_students[-1]))