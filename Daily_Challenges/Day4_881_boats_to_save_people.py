# Date: 04-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India
# When using in leet code replace print statements with return statements

people = [1,2]
limit = 3
people.sort()
first = 0
res = 0
last = len(people) - 1
while first <= last:
    if people[last] == limit:
        res +=1
    elif people[last] < limit:
        if people[first] + people[last] <= limit:
            res += 1
            first += 1
        else:
            res += 1
    last -= 1
print(res)
# return res