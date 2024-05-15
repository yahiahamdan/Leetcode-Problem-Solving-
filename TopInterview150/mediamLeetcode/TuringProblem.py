"""
find the no of operation to convert  the array to inc order 
as 1,2,3,4    without sorting or changing the place 
"""
def changeorder(arr):
    counter=0
    for i in range(1,len(arr)):
      if arr[i-1]>arr[i]:
         counter+=(arr[i-1]-arr[i])+1
         arr[i]+=(arr[i-1]-arr[i])+1
      else:
         counter=0
    return arr
print(changeorder([1,5,3,2]))
