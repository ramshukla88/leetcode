# Date: 02-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India
# When using in leet code replace print statements with return statements

str1 = "ABABAB"
str2 = "ABABF"

# Check if 
if str1+str2 != str2+str1:
    print("")
    
len1 = len(str1)
len2 = len(str2)
# Computing GCD for 2 string lengths
while len2!= 0:
    len1, len2 = len2, len1%len2
    
print(str1[:len1])
    
