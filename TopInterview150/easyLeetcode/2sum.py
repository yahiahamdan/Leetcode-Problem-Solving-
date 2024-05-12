def twosum(nums,target):
    hasdict={nums[i]:i for i in range(len(nums))}
    for i in range(len(nums)):
        diff=target-nums[i]
        if(diff  in hasdict):
          return [i,hasdict[diff]]
print(twosum([3,2,4],6))
