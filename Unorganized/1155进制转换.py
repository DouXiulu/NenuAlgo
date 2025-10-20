try:
    n = int(input())
    
    inputs = []
    for _ in range(n):
        inputs.append(int(input(),2))
    
    outputs = []
    for t in inputs:
        outputs.append(hex(t).upper()[2:])
    
    for res in outputs:
        print(res)

except Exception as e:
    print(e)