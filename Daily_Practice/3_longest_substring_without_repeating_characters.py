s = " "

prev = 0
next = 0
res = []
high = 0
if len(s) == 1:
    print(1)
for i in range(len(s)-1):
    prev = i
    next = i+1
    if s[prev] not in res:
        res.append(s[prev])
    print(f"Before while===> Previous = {prev} next = {next} res = {res}")
    while len(res) >= 1 and next < (len(s)):
        if s[next] not in res:
            res.append(s[next])
        else:
            if len(res) > high:
                high = len(res)
            res = []
        prev += 1
        next = next + 1
        print(f"End of while===> Previous = {prev} next = {next} res = {res}")

print(high) if high > len(res) else print(len(res))
# print(res)