"""
given matrix mat  where every row is sorted in increasing order 
return the smallest common element in all rows
mat= [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
"""
def finc_common_elements(matrix):

 common_elements=set(matrix[0])
 for row in matrix[1:]:
   common_elements &=set(row)
   sortedList=sorted(common_elements)
 return (sortedList[0])

print(finc_common_elements([[1,2,3,4,5],[2,3,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]))        

keydict={'x':1,'b':5,'a':3}
sortedKeys=(sorted(keydict))
sortedValues=sorted(keydict,key=keydict.get)
print(sortedKeys)
print(" ==== ")
print(sortedValues)