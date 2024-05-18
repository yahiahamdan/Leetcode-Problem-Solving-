"""
brute force solution for gettings max lenght substring with 2 occurance
bcbbcba
return bcba  

"""
class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        maxlength=0
        chardict={} 
        left=0
        for right in range(len(s)):
           if s[right] in chardict:
              chardict[s[right]]+=1 
           else:
            chardict[s[right]]=1
          
           while chardict[s[right]]>2:
              chardict[s[left]]-=1
              if chardict[s[left]]==0:
                del chardict[s[left]]
              left+=1
           maxlength=max(maxlength,right-left+1)
        return maxlength
        