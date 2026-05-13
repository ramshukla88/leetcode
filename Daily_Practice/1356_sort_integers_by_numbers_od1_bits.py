arr = [0,1,2,3,4,5,6,7,8]
res = {}
for i in arr:
    count = bin(i).count("1")
    res.setdefault(count, []).append(i)
print([x for key in sorted(res) for x in sorted(res[key])])
