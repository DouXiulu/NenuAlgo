# import sys

# # 假设标准输入如下：
# # Hello World
# # This is a test
# # Another line

# # 使用 readline() 读取第一行
# line = sys.stdin.readline()
# print(line.strip())  # 输出: 'Hello WHello Worldorld\n'

# # # # 使用 read() 读取剩余的所有内容
# remaining = sys.stdin.read()
# print(remaining)  # 输出: 'This is a test\nAnother line\n'

# # # 假设重新开始，标准输入同样
# # 使用 readlines() 读取所有行
# lines = sys.stdin.readlines()
# print(lines)  # 输出: ['Hello World\n', 'This is a test\n', 'Another line\n']



max_n = 3

db = [[0] * (max_n+1) for _ in range(max_n+1)]

print(db)