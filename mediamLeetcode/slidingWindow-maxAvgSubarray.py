# i solved by this problem it accepted but give time limit exceed error
#this is the brute force solution as every time it calculates the sum of the subarray
def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxresult=float('-inf')
        for i in range(len(nums)-k+1):
            substring=nums[i:i+k]
            print(substring)
            average=sum(substring) / float(k)
            print(average)
            maxresult=max(maxresult,average)
        return maxresult
# This is the optimized solution by calculating the sum of the first subarray 
#then procedding in by chekcing the max and remove the first element by adding the next element

def findMaxAverageSum(nums,k):
 current_sum=sum(nums[:k])
 maxsum=current_sum
 for i in range(k,len(nums)):
            current_sum += nums[i] - nums[i-k] 
            maxsum=max(maxsum,current_sum)
 return maxsum / float(k)