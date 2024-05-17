      # return maxLength
#by using the sliding window method 
def lengthOfLongestSubstring(s):
        left=0
        checkset=set()
        maxlength=0        
        for right in range(len(s)):
            while s[right] in checkset :
                checkset.remove(s[left])
                left+=1
            checkset.add(s[right])
            maxlength=max(maxlength,right-left+1)
        return maxlength
#by using the brute force method
def hasNorepeats(s):
        return len(s)==len(set(s))
def bruteForce(s):
        if not s :
          return 0
        if len(s)==1:
            return 1
        maxLength=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                substring=s[i:j]
                if  hasNorepeats(substring):
                    maxLength=max(maxLength,j-i)
        return maxLength