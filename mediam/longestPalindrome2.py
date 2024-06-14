def longestPalindrome(self, s):
        if len(s)==1:
            return 1 
        hasdict={}
        count=0
        oddFound=False
        for i in range(len(s)):
           if s[i] in hasdict:
              hasdict[s[i]]+=1
           else:
              hasdict[s[i]]=1
        for key,value in hasdict.items():
            if value>=2:
                count+=(value //2)*2
            if value%2==1 :
                oddFound=True
        if oddFound :
            count+=1
        return count 
