# Date: 05-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India
# When using in leet code replace print statements with return statements

s = "0-1"
if not s:
    print(0)
    # return 0

s = s.strip()  # remove leading and trailing whitespace

if not s:
    print(0)
    # return 0

sign = -1 if s[0] == '-' else 1
if s[0] in ['-', '+']:
    s = s[1:]

res = 0
for char in s:
    if not char.isdigit():
        break
    digit = ord(char) - ord('0')
    res = res * 10 + digit
    print(max(-2 ** 31, min(sign * res, 2 ** 31 - 1)))
# return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))
