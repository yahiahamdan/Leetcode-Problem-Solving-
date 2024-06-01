"""
this problem want to find the longest sequence in problem 
so lets define it
[100,4,200,1,3,2] 
"""
def longestConsective1(nums):
    if not nums:
        return 0 
    nums.sort()
    longest_streak=1
    current_streak=1
    for i in range(1,len(nums)):
        if(nums[i]!=nums[i-1]):
             if nums[i]== nums[i-1]+1:
                 current_streak+=1
             else:
                 current_streak=1
        longest_streak=max(longest_streak,current_streak)
    return longest_streak

print(longestConsective1([100,4,200,1,3,2]))

def longestConsective2(nums):
    longestStreak=0
    newset=set(nums)
    for num in nums:
        current_num=num
        if num-1 not in newset:
            currentStreak=1
            while current_num+1 in newset:
                current_num+=1
                currentStreak+=1
            longestStreak=max(longestStreak,currentStreak)
    return longestStreak
print(longestConsective2([100,4,200,1,3,2]))

         
            
