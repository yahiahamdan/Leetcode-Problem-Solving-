"""'
ana endy fucntion matrix i[student,examj]  
k is the index of the exam   
a sort the row 
3ayz a sort student by thier kth order 
"""
class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        score.sort(key=lambda x: x[k] ,reverse=True)
        return score