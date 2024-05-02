# Date: 02-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India
# When using in leet code replace print statements with return statements

nums = [-1,10,6,7,-7,1]
nums.sort()
found = False
for i in range(len(nums)):
    if -(nums[i]) in nums:
        found = True
        print(-nums[i])
        # return (-nums[i])  #Uncomment this when submitting in leet code

if not found:
    print("-1")
    # return -1   #Uncomment this when submitting in leet code