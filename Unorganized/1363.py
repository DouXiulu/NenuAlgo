import sys

def fun(string):
    d = {")":"(","]":"[","}":"{"}
    stack = []
    for s in string:
        if s == "(" or s == "[" or s == "{":
            stack.append(s)
        if stack and d.get(s) == stack[-1]:
            stack.pop()
    if not stack:
        return "YES"
    else:
        return "NO"

results = []
for line in sys.stdin:
    string = []
    if line.strip():
        string = line.strip()
    results.append(fun(string))

for res in results:
    print(res)
        
# except Exception as e:
#     print(e)