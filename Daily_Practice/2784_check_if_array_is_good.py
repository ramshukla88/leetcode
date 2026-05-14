nums = [1, 1]

nums.sort()

for i in range(len(nums)-1):
    if (i+1) != nums[i]:
        print("False")
        break
if nums[-1] == len(nums) -1:
    print("True")
else:
    print("False")