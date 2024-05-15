"""
you are given 2d matrix and you want to change
2d matrix  you want to rotate it 
1 2 3      7 4 1
4 5 6   =  8 5 2 
7 8 9      9  6 3 
1) in the answer you should modify the array  
but first lets think of doing another array 
"""
def rotateImage(mat):
 colIndex=0
 columnLength=len(mat[0])-1
 newMatrix=[]
 
 while(colIndex<=columnLength):
    lis=[]
    for i in range (len(mat)-1,-1,-1):
      lis.append(mat[i][colIndex])
    newMatrix.append(lis)
    colIndex+=1
 return newMatrix 

print(rotateImage([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
          