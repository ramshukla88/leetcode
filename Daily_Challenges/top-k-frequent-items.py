nums = [1,1,1,2,2,3]
k = 2
# from collections import Counter
# def topKFrequent(nums, k):
#     count = Counter(nums)
#     return [item for item, freq in count.most_common(k)]
# print(topKFrequent(nums, k))

count = {}
for n in nums:
    count[n] = 1 + count.get(n, 0)

freq = [[] for i in range(len(nums) + 1)]
for n, c in count.items():
    freq[c].append(n)

res = []
for i in range(len(freq) - 1, 0, -1):
    for n in freq[i]:
        res.append(n)
        if len(res) == k:
            print(res)
            break
