class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        if(target>nums[right]):
            return right+1
        if len(nums)==1:
            return 0 if target <=nums[0] else 1
        while left < right:
            mid=(left+right) // 2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target :
              right=mid
            else :
             left=mid+1
        return left
    
