"""
intervals=[start,end]  
if there is overlap between two intervals, merge them
[1,3],[8,10],[2,6]  => [1,6]

""" 
# def mergeIntervals(interval):
#     res=[]
#     interval.sort(key=lambda x:x[0])
#     for i in range(1,interval):
#        if interval[i-1][1]>=interval[i][0]:
#            interval[i-1][1]=max(interval[i-1][1],interval[i][1])
#            res.append(interval[i-1]) 
#        else:
#               res.append(interval[i-1])
#     return res
#print(mergeIntervals([[1,3],[8,10],[2,6]]))


class Solution(object):
    def merge(self, interval):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        interval.sort(key=lambda x : x[0])
        result=[]
        result.append(interval[0])
        for i in range(1,len(interval)):
            if result[-1][1]>=interval[i][0]:
                #we merge it 
                result[-1][1]=max(result[-1][1],interval[i][1])
            else:
                #no overlapp
                result.append(interval[i])
        return result