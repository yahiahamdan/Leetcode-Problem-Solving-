class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
         return False  # Early return if the matrix is empty or the rows are empty

        row=len(matrix)
        col=len(matrix[0])
        left=0
        right=(row*col)-1
        while(left <= right):
            mid=(left+right) // 2 
            midValue= matrix[mid // col][mid % col]
            if midValue==target:
             return True
            elif midValue > target:
                right=mid-1
            else :
                left=mid+1
        return False
