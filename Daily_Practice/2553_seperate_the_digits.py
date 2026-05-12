nums = [13,25,83,77]

numstr = str(nums)
numstr = numstr.replace(",", "").replace(" ", "").replace("[", "").replace("]", "")
print(numstr)

digits = [int(d) for d in numstr]
print(digits)