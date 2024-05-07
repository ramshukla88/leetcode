# Date: 07-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India

num1 = "123"
num2 = "456"
# Reverse the strings to start from the least significant digit
num1 = num1[::-1]
num2 = num2[::-1]

# Initialize the result list with 0s
result = [0] * (len(num1) + len(num2))
print(result)
# Multiply each digit and sum up the results
for i in range(len(num1)):
    for j in range(len(num2)):
        result[i + j] += int(num1[i]) * int(num2[j])
        result[i + j + 1] += result[i + j] // 10
        result[i + j] %= 10

# Remove leading zeros and convert the result to string
while len(result) > 1 and result[-1] == 0:
    result.pop()

print(''.join(map(str, result[::-1])))
# return ''.join(map(str, result[::-1]))
