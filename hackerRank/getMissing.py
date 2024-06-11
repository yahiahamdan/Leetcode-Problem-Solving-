def getMissing(nums,k):
    numsSet=set(nums)
    counter=0
    currentNumber=1
    while counter<k:
        if currentNumber not in numsSet:
            counter+=1
        currentNumber+=1
    return currentNumber
print(getMissing([1,3,4,7],2))