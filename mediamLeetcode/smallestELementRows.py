"""
given matrix mat  where every row is sorted in increasing order 
return the smallest common element in all rows
mat= [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
"""
keydict={'x':1,'b':5,'a':3}
sortedKeys=(sorted(keydict))

reversedArray= reversed(list(keydict.items()))
print(sortedKeys)
print(" ==== ")

def smallestElementRows(matrix):
    commenElements=set(matrix[0])
    for row in range(1,len(matrix)):
        commenElements&=set(matrix[row])
    return list(commenElements)[-1]
print(smallestElementRows([[1,2,3,4,5],[2,4,5,8,10],[2,5,4,9,11],[2,3,5,7,4]]))
