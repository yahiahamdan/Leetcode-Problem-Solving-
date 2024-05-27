class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack=[]
        nextgreater=[-1]*len(nums2)
        hashmap={}
        res=[]
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
              lastIndex= stack.pop()
              nextgreater[lastIndex]=nums2[i]
            stack.append(i)
        for i in range(len(nums2)):
          hashmap[nums2[i]]=nextgreater[i]
        for i in range(len(nums1)):
           if nums1[i] in hashmap:
            res.append(hashmap[nums1[i]])
        return res 
    