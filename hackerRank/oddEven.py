def evenodd(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j]%2==0:
                nums[j]=nums[j]-3
            else:
                nums[j]=nums[j]+3
    return nums

print(evenodd([3,4,9])) 
