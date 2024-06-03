   #hashdict={}
        # for i in range(len(nums)):
        #     if nums[i] in hashdict:
        #         hashdict[nums[i]]+=1
        #     else:
        #         hashdict[nums[i]]=1
        # value = [key for key, value in hashdict.items() if value > n/2 ]
        # return value[0]
import random
def majorityElement(nums):  
    while True:
          value=random.choice(nums)
          sumValue=sum(1 for i in nums if value==i)
          if sumValue > len(nums) // 2:
                return value