#the problem states i should do another array but first with the same array 
def rotatArray1(nums,k):
     anotherArray=[]
     lenght=len(nums)
     anotherArray=[0]*lenght
     for i in range(len(nums)):
            anotherArray[i]=nums[((len(nums)-k+i))%len(nums)]
     return anotherArray
print(rotatArray1([1,2,3,4,5,6,7],3)) 
# so the first approach worked fine now lets try with modifying the array 

def rotateArray2(nums,k):
      k=k%len(nums)
      return nums[-k:]+nums[0:-k]
print(rotateArray2([1,2,3,4,5,6,7],3))

def rotateArray3(nums,k):
        k=k% len(nums)
        left,right=0,len(nums)-1
        while(left<right):
           nums[left],nums[right]=nums[right],nums[left]
           left+=1
           right-=1
        left=0  
        right=k-1
        while(left<right):
           nums[left],nums[right]=nums[right],nums[left]
           left+=1
           right-=1
        left=k  
        right=len(nums)-1
        while(left<right):
           nums[left],nums[right]=nums[right],nums[left]
           left+=1
           right-=1 
