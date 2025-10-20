import math

flag = 0
for i in range(10000,int(math.sqrt(987654321))):
    if len(str(int(math.pow(i,2)))) == len(set(str(int(math.pow(i,2))))):
        # print(set(str(int(math.pow(i,2)))))
        flag += 1
        print(f"No.{flag}：x={i}, x2={int(math.pow(i,2))}")
# print(math.sqrt(987654321))

# print(100**2)
# print(math.pow(100,2))
# print(pow(100,2))
# print(math.sqrt(100))