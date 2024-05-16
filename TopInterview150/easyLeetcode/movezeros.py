class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeropointer=0
        for i in range(len(nums)): 
          if nums[i]!=0:
            nums[zeropointer],nums[i]=nums[i],nums[zeropointer]
            zeropointer+=1
        return nums
