# Date: 02-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India
# When using in leet code replace print statements with return statements

nums = [-1,0,1,2,-1,-4]
nums.sort()  # Sort the array to easily skip duplicates
res = []
length = len(nums)

for i in range(length - 2):  # Iterate until the third-to-last element
    if i > 0 and nums[i] == nums[i - 1]:
        continue  # Skip duplicates at the outer level

    left = i + 1  # Left pointer
    right = length - 1  # Right pointer

    while left < right:
        total = nums[i] + nums[left] + nums[right]
        if total == 0:
            res.append([nums[i], nums[left], nums[right]])

            # Skip duplicates for left pointer
            while left < right and nums[left] == nums[left + 1]:
                left += 1

            # Skip duplicates for right pointer
            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            left += 1  # Move left pointer to next unique element
            right -= 1  # Move right pointer to next unique element

        elif total < 0:
            left += 1  # Move left pointer to increase sum
        else:
            right -= 1  # Move right pointer to decrease sum

return res