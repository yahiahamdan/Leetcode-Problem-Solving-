class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        lowdigit=len(str(low))
        highdigit=len(str(high))
        string='123456789'
        res=[]
        for i in range(lowdigit,highdigit+1):
            for j in range(len(string)-i+1):
                sub=string[j:j+i]
                if int(sub)>=low and int(sub)<=high:
                    res.append(int(sub))
        return res
        