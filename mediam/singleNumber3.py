[1,2,1,3,2,5]
"""
fl problem deh  ana 3ndy rkmeen unique 
3ayz agbhom btrea2a 2 pointer approach 
"""

def singleNumber(nums):
 res=[0,0]
 index=0
 for i in range(len(nums)):
    found=False
    for j in range(len(nums)):
      if i !=j and nums[i]==nums[j]:
        found=True
        break
    if not found:
      res[index]=nums[i]
      index+=1
      if index==2:
        break
 return res 

print(singleNumber([1,2,1,3,2,5]))
    
