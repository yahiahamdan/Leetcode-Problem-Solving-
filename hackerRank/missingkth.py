def missing(nums,target):
    nums.sort()
    res=[]
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]!=1:
            firstnum=nums[i-1]+1
            endnum=nums[i]
            while firstnum<endnum:
                 res.append(firstnum)
                 firstnum+=1
    return res[target-1]
print(missing([4,7,9,10],3)) #8

