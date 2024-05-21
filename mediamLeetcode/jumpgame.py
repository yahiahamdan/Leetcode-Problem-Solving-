def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        dlwaty ana mmkn amshy 2 
        ana msheet 1 we zwdt 3  wslt 
        
        """
        farthest=0 #the farest index we can reach   
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest=max(farthest,i+nums[i])
            
            if farthest >=len(nums)-1:
                return True
        return False

        
        