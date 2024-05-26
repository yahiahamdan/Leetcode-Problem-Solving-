class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #ana 3ayz a3ml square le number than a3ml sort 
        for i  in range (len(nums)):
            nums[i]=abs(nums[i]**2)
        nums.sort()
        return nums