class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        it lan empty li
        """
        res=set()
        for i in range(9):
          for j in range(9):
            element=board[i][j]
            if element != '.':
                if (i,element) in res or (element,j) in res or (i//3,j//3,element) in res :
                   return False
#(element,j) to ovoid overlapping 
                res.add((i,element))
                res.add((element,j))
                res.add((i//3,j//3,element))
        return True

        