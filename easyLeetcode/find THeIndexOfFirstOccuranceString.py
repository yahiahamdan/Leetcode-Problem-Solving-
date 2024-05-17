class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        index:0  -1  first occurance of string
        ana 3ayz lw p2==len(needle) return p1-len(needle) 
        """
        return haystack.find(needle)
def strStr2(self,haystack,needle):
        for start in range(len(haystack)-len(needle)+1):
            match=True
            for j in range(len(needle)):
             if(haystack[start+j]!=needle[j]):
                match=False
                break
            if(match):
                return start            
        return -1
    
         