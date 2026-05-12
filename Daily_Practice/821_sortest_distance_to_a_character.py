from typing import List

def shortestToChar(s: str, c: str) -> List[int]:
    n = len(s)
    res = [n] * n  # worst-case distance is len(s)

    prev = float('-inf')
    for i in range(n):
        if s[i] == c:
            prev = i
        res[i] = i - prev

    prev = float('inf')
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            prev = i
        res[i] = min(res[i], prev - i)

    return res

s = "loveleetcode"
c = "e"
print(shortestToChar(s, c))
    