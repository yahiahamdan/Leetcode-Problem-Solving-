def containsDuplicate2(nums,k):
    dictnums={}
    for i in range(len(nums)):
            if nums[i] in dictnums and abs(dictnums[nums[i]]-i) <=k:
                return True
            else:
                dictnums[nums[i]]=i
    return False
        