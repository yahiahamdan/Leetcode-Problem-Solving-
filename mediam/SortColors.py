#hwa 3ayzny a sort 3ady [0,0,1,1,2]
#selection sort 
def selectionSort(nums):
    for i in range(len(nums)):
        minIndex=i
        for j in range(i+1,len(nums)):
            if nums[minIndex] >= nums[j]:
                minIndex=j
        #swap
        nums[minIndex],nums[i]=nums[i],nums[minIndex]
    return nums
print(selectionSort([2,0,2,1,1,0]))
#bubble sort 
#bykarn adjacent number m3 b3d y3ny 
def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums
print(bubbleSort([2,0,2,1,1,0]))
#insertion sort 

def countingSort(nums):
      maxNumber=max(nums)
      minNumber=min(nums)
      length_count=(maxNumber-minNumber)+1
      count=[0]*length_count

      for num in nums:
            count[num-minNumber] += 1

      for i in range(1,len(count)):
            count[i] += count[i-1]
      print(count) 

      output=[0] * len(nums)
        #nums.reverse()

      for num in reversed(nums):
          output[count[num-minNumber]-1] =num
          count[num-minNumber] -=1
      return output
print(countingSort([2,0,2,1,1,0]))