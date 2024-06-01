class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500, 
        "M":1000,
            }
        res=0
        for i in range(0,len(s)-1):

         if(s[i] in dic):
             if(dic[s[i]] < dic[s[i+1]]):
                res -= (dic[s[i]])
             else:
               res += (dic[s[i]])
        res += dic[s[-1]]
        return res             
     