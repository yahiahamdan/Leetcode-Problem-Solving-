class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        counter=0    
        for i in range(len(s)-2):
           substring=s[i:i+3]
           if len(set(substring))==3:
            counter+=1
        return counter

