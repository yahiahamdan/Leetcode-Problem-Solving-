class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
flower  flow flight 
ana h2f an 3nd f fe awl wa7da we hkarn
strs 
        """
        number=strs[0]
        minLength = min(len(s) for s in strs)
        getall=""
        for i in range(minLength):
         current_char=number[i]
         for j in range(1,len(strs)):
           if current_char!=strs[j][i]:
             return getall
         getall+=number[i]
        return getall