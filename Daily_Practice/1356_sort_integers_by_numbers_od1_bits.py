arr = [0,1,2,3,4,5,6,7,8]
binary = []
res = {}
for i in arr:
    binary.append(str(bin(i)).replace("0b", ""))

for i in binary:
    count = i.count("1")
    if count not in res:
        res[count] = [int(i,2)]
    else:
        res[count].append(int(i,2))
print([x for key in sorted(res) for x in sorted(res[key])])