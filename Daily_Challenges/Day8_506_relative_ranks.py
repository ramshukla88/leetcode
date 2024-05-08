# Date: 08-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India

score = [10,3,8,9,4]
backup = score.copy()

score.sort(reverse=True)

for i in range(len(score)):
    j = backup.index(score[i])
    if i == 0:
        backup[j] = "Gold Medal"
    elif i ==1:
        backup[j] = "Silver Medal"
    elif i == 2:
        backup[j] = "Bronze Medal"
    else:
        backup[j] = str(i+1)
        #
    # print(i)
print(backup)
