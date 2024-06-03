class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        ans=0
        i=0
        while i < len(chars):
            j=i
            while j <len(chars) and chars[i]==chars[j]:
                j+=1
            chars[ans]=chars[i]
            ans+=1
            if j-i>1:
                stringCount=str(j-i)
                for i in range(len(stringCount)):
                  chars[ans]=stringCount[i]
                  ans+=1
            i=j          
        return ans
                   