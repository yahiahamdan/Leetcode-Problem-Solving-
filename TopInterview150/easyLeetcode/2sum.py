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