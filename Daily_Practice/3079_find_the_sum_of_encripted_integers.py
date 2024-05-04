# Date: 05-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India
# When using in leet code replace print statements with return statements

nums = [10,21,31]
l = []
res = 0
for i in nums:
    maximum_digit = int(max(str(i)))
    res += int(str(maximum_digit) * len(str(i)))

print(res)
# return res
