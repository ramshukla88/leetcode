# Rotate string and check if the target string can be achieved by rotating the initial string

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:]+s[:i] == goal:
                return True
        return False
