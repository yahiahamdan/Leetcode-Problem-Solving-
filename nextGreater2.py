class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums2=nums*2
        nextGreater=[-1]*len(nums2)
        stack=[]
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
               lastindex= stack.pop()
               nextGreater[lastindex]=nums2[i]
            stack.append(i)
        return nextGreater[0:len(nums)]
        
        