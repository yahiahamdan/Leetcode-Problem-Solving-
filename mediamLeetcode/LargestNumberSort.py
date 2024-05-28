from functools import cmp_to_key
class Solution(object):
   
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(num1,num2):
          if num1+num2> num2+num1:
           return -1 
          else :
           return 1 
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        nums.sort(key=cmp_to_key(compare))
        return str(int(''.join(nums)))  

        

                 

        