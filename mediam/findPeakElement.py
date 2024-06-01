
"""
binary search problem to find the peak element in the array
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        mid=0
        while (left<right):
            mid=left+(right-left)//2 
            if nums[mid]> nums[mid+1]:
                right=mid
            else:
                left+=1
        return left