#first approach to solve this 0(n)
def twosumSorted(nums,target):
    left=0
    right=len(nums)-1
    while(left<right):
        sum=nums[left]+nums[right]
        if sum==target:
            return [left,right]
        elif sum<target:
            left+=1
        else :
            right-=1

    return []
print(twosumSorted([2,7,11,15],9))
