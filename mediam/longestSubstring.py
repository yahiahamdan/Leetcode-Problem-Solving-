def longestSubstring(string):
    left=0
    right =0
    maxLength=0
    checkset=set()
    for right in range(len(string)):
        while string[right]   in checkset:
            checkset.remove(string[left])
            left+=1
        checkset.add(string[right])
        maxLength=max(maxLength,right-left+1)
    return maxLength
print(longestSubstring("abcabcbb"))