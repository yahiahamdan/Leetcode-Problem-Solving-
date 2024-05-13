#brute force solutation o(npow3)
def threesum(nums):
    nums.sort()
    listofnumbers=[]
    result=[]
    for i in range(len(nums)):
        if i>0 and nums[i] ==nums[i-1]:
            continue
        for j in range(i+1,len(nums)):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            for k in range(j+1,len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:  # Skip the same element to avoid duplicates
                    continue
            
                
                if(nums[i]+nums[j]+nums[k]==0):
                    result.append([nums[i],nums[j],nums[k]])

    return result
list=[-1,0,1,2,-1,-4]
print(threesum(list))
#most efficent solution two pointers 
"""
sort the array  then iterate through each element 
using another two pointer approahc  
"""

def threeSum2(nums):
    nums.sort()
    result=[]
    for i in range(len(nums)-2):
        if nums[i]>0 :
            break
        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=len(nums)-1
        while(left<right):
            current_sum=nums[i]+nums[left]+nums[right]
            if(current_sum <0):
                left+=1
            elif(current_sum >0):
                right-=1
            else:
              result.append([nums[i],nums[left],nums[right]])
              while left<right and nums[left]==nums[left+1]:
                 left+=1
              while left < right and nums[right]==nums[right-1]:
                right-=1
            left+=1
            right-=1
    return result
print(threeSum2(list))