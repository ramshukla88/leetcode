# Date: 03-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India
# When using in leet code comment print statements and uncomment return statements

version1 = "1.04.7"
version2 = "1.004.7"
v1 = list(map(int, version1.split(".")))
v2 = list(map(int,version2.split(".")))
len_v1 = len(v1)
len_v2 = len(v2)

print(f"===> Length V1 = {len_v1} V2 = {len_v2}")
while len_v1 > len_v2:
    v2.append(0)
    len_v2=len(v2)
while len_v1 < len_v2:
    v1.append(0)
    len_v1=len(v1)
print(f"===> New Length V1 = {len_v1} V2 = {len_v2}")
print(v1)
print(v2)
found = False
for i in range(len_v1):
    if v1[i] > v2[i]:
        found = True
        print("1")
        # return 1
        break
    elif v1[i] < v2[i]:
        found = True
        print("-1")
        # return -1
        break
    else:
        pass
if not found:
    print("0")
    # return 0
