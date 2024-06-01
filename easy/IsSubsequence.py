class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t_pointer=0
        s_pointer=0
        while(t_pointer<len(t)):
            if(s_pointer<len(s) and s[s_pointer]==t[t_pointer]):
                s_pointer+=1
            t_pointer+=1
        if(s_pointer==len(s)):
            return True
        else: 
            return False