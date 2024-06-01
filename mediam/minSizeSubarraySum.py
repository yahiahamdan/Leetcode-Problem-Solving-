class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        #sliding window
        minValue=float('inf')
        counter=0
        Sum=0 
        left=0
        for right in range(len(nums)):
            Sum+=nums[right]
            counter+=1
            while(Sum>=target):
                print(Sum)
                minValue=min(minValue,right-left+1)
                Sum-=nums[left]
                left+=1
 
        return minValue if minValue !=float('inf') else  0 