# Date: 04-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India
x = -123
s = str(x)
sign =""
if s[0] == "-":
    s = s[1:]
    sign = "-"
res = s[::-1]
s = int(sign+res)
if s >= 2147483647 or s <= -2147483648:
    print(0)
    # return 0
print(s)
# return s