"""
题目描述
一次考试共考了语文、数学和英语三科。每个班最多有100人（学号从1开始），老师提供了考后各科及格名单，请编写算法找出三科全及格的学生的学号。
输入
输入有多组，每组有三行，第一行为语文及格的学号，空格隔开。第二行为数学及格的学号，第三行为英语及格的学号。每行的最后是-1，表示结束。
输出
输出三科都及格的学号，从小到大输出，每个学号后有个空格。
样例输入 复制
1 9 6 8 4 3 7 -1
5 2 9 1 3 7 -1
8 1 6 7 3 5 4 9 -1
样例输出 复制
1 3 7 9 
"""

# import sys

# outputs = [line.strip() for line in sys.stdin if line.strip()]

# for i in range(0,len(outputs),3):
#     if i+1 >= len(outputs) or i+2 >= len(outputs):
#         break
#     a = outputs[i].split()
#     a.pop()
#     b = outputs[i+1].split()
#     b.pop()
#     c = outputs[i+2].split()
#     c.pop()
    
    
#     d = {}
    
#     for i in a:
#         d[i] = d.get(i,0) + 1
#     for j in b:
#         d[j] = d.get(j,0) + 1
#     for k in c:
#         d[k] = d.get(k,0) + 1
    
#     # print(d)
    
#     res = []
#     for key,values in d.items():
#         if values == 3:
#            res.append(key)
           
#     res = sorted(map(int,res))
    
#     for r in res:
#         print(r,end = " ")

# ... 前面导入和输入处理不变 ...

for i in range(0, len(outputs), 3):  # 修改1：步长改为3，正确分组
    if i+2 >= len(outputs):
        break
    
    # 修改2：添加转换为整数的步骤，并验证格式
    a = list(map(int, outputs[i].split()[:-1]))
    b = list(map(int, outputs[i+1].split()[:-1]))
    c = list(map(int, outputs[i+2].split()[:-1]))
    
    # 修改3：使用集合求交集更高效
    set_a = set(a)
    set_b = set(b)
    set_c = set(c)
    common = set_a & set_b & set_c
    
    # 修改4：转换为整数排序，并正确格式化输出
    res = sorted(map(int, common))
    print(' '.join(map(str, res)) + ' ')  # 确保结尾有空格