# Date: 05-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India
# When using in leet code replace print statements with return statements

s = "foo"
t = "baa"
dict1 = {}
dict2 = {}
k = 0
for i, j in zip(s, t):
    if i in dict1:
        dict1[i].append(k)
    else:
        dict1[i] = [k]
    if j in dict2:
        dict2[j].append(k)
    else:
        dict2[j] = [k]
    k += 1
print(list(dict1.values()) == list(dict2.values()) and len(dict1) == len(dict2))
# return list(dict1.values()) == list(dict2.values()) and len(dict1) == len(dict2)
