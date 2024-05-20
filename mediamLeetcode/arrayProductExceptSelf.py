"""
first write brute force soltuion o(n^2) 
to solve this problem 
the problem is asking get 
 return an array is equal of all the elements of nums
 except nums[i]
"""
def arrayProductExceptSelf(nums):
        answer=[]
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if i!=j:
                    product*=nums[j]
            answer.append(product)
        return answer
"""
now i want to solve it using o(n) time complexity
"""
"""
it give me time limit exceed in this problem but was nice solution so i write it 
"""
def arrayProductExceptSelf2(nums):
        answer=[0]*len(nums)
        leftProduct=1
        rightProduct=1
        for i in range(len(nums)):
          answer[i]=leftProduct
          leftProduct *= nums[i]
          print(answer)
        for j in range(len(nums)-1,-1,-1):
          answer[j]*=rightProduct
          rightProduct*=nums[j]
        return answer