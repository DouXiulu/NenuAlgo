# AC50%
"""
题目描述
已知某个班有n（1 <= n <= 100）个学生，输入每行为学生姓名（最多20个字符）和其c语言成绩（0~100），请找出最高分和最低分输出，若最高分或最低分多于1个的，按先后顺序输出。
输入
输入有多行，每行表示一个学生的信息，包括姓名和成绩，空格隔开。
输出
输出最高分和最低分，多于1个的按出现的顺序依次输出，格式详见输出样例。
样例输入 复制
Zhangsan 80
Lisi 95
Zhouyi 69
Wangwu 73
Zhaoliu 69
样例输出 复制
Max is 95,name has Lisi
Min is 69,name have Zhouyi,Zhaoliu
"""

import sys


lt = []
for line in sys.stdin:
    dt = {}
    name, score = line.split()
    dt["name"] = name
    dt["score"] = int(score)
    lt.append(dt)

# print(dt)
# print(lt)

new_lt = sorted(lt, key = lambda x:x["score"], reverse = True)

print(new_lt)

max_score = new_lt[0]["score"]
min_score = new_lt[-1]["score"]


print(max_score,min_score)

max_name = []
min_name = []
for dt in new_lt:
    if dt["score"] == max_score:
        max_name.append(dt["name"])
    if dt["score"] == min_score:
        min_name.append(dt["name"])

    
print(f"Max is {max_score},name has {','.join(max_name)}")
print(f"Min is {min_score},name have {','.join(min_name)}")
