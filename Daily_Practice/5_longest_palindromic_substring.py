# Date: 04-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India
# When using in leet code replace print statements with return statements

s = "cbbd"
if len(s) == 0:
    print("")

start = 0
max_length = 1
n = len(s)

for i in range(1, n):
    # Check odd-length palindromes with s[i] as center
    left = i - 1
    right = i + 1
    while left >= 0 and right < n and s[left] == s[right]:
        if right - left + 1 > max_length:
            start = left
            max_length = right - left + 1
        left -= 1
        right += 1

    # Check even-length palindromes with s[i-1] and s[i] as center
    left = i - 1
    right = i
    while left >= 0 and right < n and s[left] == s[right]:
        if right - left + 1 > max_length:
            start = left
            max_length = right - left + 1
        left -= 1
        right += 1

print(s[start:start + max_length])
