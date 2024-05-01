# Date: 01-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India
# When using in leet code comment/uncomment print statements with return statements
# Time Complexity is O(n^2)

nums = [3,2,4]
target = 6
for i in range(len(nums)):
    idx1 = i
    for j in range(i+1,len(nums)):
        idx2 = j
        if nums[idx1] + nums[idx2] == target:
            print(f"Index1 = {idx1} index2 = {idx2}") 
            # return [idx1, idx2]
    
