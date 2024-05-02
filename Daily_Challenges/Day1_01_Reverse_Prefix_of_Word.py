# Date: 01-May-2024
# Author: Ram Shukla
# Location: Hyderabad, India
# When using in leet code replace print statements with return statements
word = "abcdefd"
ch = "d"
# If the ch is nto present in word we will return ithe word directly
if ch not in word:
    print(word)
else:
    # Extracting out the first part so that we can reverse it easily
    idx = word.index(ch)
    fp = word[:idx+1]
    print(fp[::-1]+word[idx+1:])