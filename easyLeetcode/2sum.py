#first approach to solve this problem using one loop for hash one loop for checking 
def twosum(nums,target):
    hasdict= {nums[i]:i for i in range(len(nums)) }
    for i in range(len(nums)):
           diff=target-nums[i]
           if(diff in hasdict and hasdict[diff]!=i):
            return [i,hasdict[diff]]
    return []
#second approach to solve this problem 
#lets do anothedr approach  using the same hashmap 
def twosum2(nums,target):
    hasdit={}
    for i in range(len(nums)):
      diff=target-nums[i]
      if diff not in hasdit:
          hasdit[nums[i]]=i
      else:
          return [i,hasdit[diff]]
    return []
def twosum3(nums,target):
    listT=[]
    res=[]
    for i in range(len(nums)-1):
        
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                listT.append([i,j])
    res.append(listT)
    return res
print (twosum3([1,2,3,4,5,6,7,8,9],9))
def twosum4(nums, target):
    hasdict = {}
    for i in range(len(nums)):
        hasdict[nums[i]] = i
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hasdict:
            return [i, hasdict[diff]]

print(twosum4([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))