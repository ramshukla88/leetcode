# Date: 05-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India

nums1 = [1,2]
nums2 = [3,4]
nums1 = nums1 + nums2
nums1.sort()
l1 = len(nums1)
if l1 % 2 == 0:
    mid = int(l1 / 2)
    print((nums1[mid] + nums1[mid-1])/2 )
else:
    print(nums1[int((l1 - 1)/2)])
