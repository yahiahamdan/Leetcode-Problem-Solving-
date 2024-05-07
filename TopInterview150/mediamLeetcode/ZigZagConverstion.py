class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        ana 3ayz atb3ha kzigzag order 
        """
        if numRows == 1 or numRows >= len(s):
            return s  # Return early if no zigzag is possible or needed

        listoflist=[[] for i in range(numRows)]
        index=0
        going_down=False
        for i in range(len(s)):
            listoflist[index].append(s[i]) 
            if(index==0 or index==numRows-1):
             going_down = not going_down

            index += 1 if going_down else  -1

        result =''.join([''.join(row) for row in listoflist])
        return result
        