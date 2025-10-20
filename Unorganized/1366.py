"""
题目描述
有一个含 n（n>2）个整数的数组 a，判断其中是否存在出现次数超过所有元素一
半的元素。
输入
输入分两行，第一行为一个正整数n(2<n<10000)。第二行为n个整数，空格隔开。
输出
如果存在出现次数超过所有元素一
半的元素，则输出该元素，否则输出NO。
样例输入 复制
3
1 2 1
样例输出 复制
1

"""

import sys

try:
    lines = [line.strip() for line in sys.stdin if line.strip()]
    
    results = []
    for i in range(0,len(lines),2):
        n = int(lines[i])
        lt = list(map(int,lines[i+1].strip().split()))
    
        d = {}
        for t in lt:
            d[t] = d.get(t,0) + 1
        
        new_d = dict(sorted(d.items(),key = lambda item:item[1],reverse = True))
        # print(new_d)
        flag = 0
        for key,value in new_d.items():
            if value > (n // 2 ):
                results.append(key)
                flag = 1
            if flag == 1:
                break
        if not flag:
            result.append("NO")
    
    for res in results:
        print(res)
    
    
    
except Exception as e:
    info = sys.exc_info()
    print(f"{info[2].tb_lineno}:{e}")