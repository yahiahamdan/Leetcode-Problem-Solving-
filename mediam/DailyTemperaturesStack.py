"""
this is monotonic stack problem want to get  
how many days to get warmer temperatures 
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
"""

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack=[]

        result=[0 for i in range(len(T))]
        for i in range(len(T)):
            while stack and T[i]> T[stack[-1]]:
                lastIndex=stack.pop()
                result[lastIndex]=i-lastIndex
            stack.append(i)
        return result