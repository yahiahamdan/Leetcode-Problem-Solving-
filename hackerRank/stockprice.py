def stockPrice(nums,d):
    counter=0
    for i in range(len(nums)):
       for j in range(i+1,len(nums)):
           for k in range(j+1,len(nums)):
                if (nums[i]+nums[j]+nums[k])%d==0:
                     counter+=1
    return counter
print(stockPrice([3,3,4,7,8],5)) 
        
