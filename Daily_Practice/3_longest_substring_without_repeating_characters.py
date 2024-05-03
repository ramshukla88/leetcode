s = "abcabcbb"
seen = {}  # Dictionary to store the index of characters
max_length = 0
start = 0

for end in range(len(s)):
    # If the character is seen before, update the start index
    if s[end] in seen:
        start = max(start, seen[s[end]] + 1)

    # Update the last seen index of the character
    seen[s[end]] = end

    # Calculate the maximum length
    max_length = max(max_length, end - start + 1)
print(max_length)