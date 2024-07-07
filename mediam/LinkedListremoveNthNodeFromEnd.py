# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #length of the list  
        counter=0
        curr=head
        while curr:
            counter+=1
            curr=curr.next
        removeIndex=counter-n
        if removeIndex==0:
            return head.next
        curr=head
        for _ in range(removeIndex-1):
            curr=curr.next
        if curr.next:
            curr.next=curr.next.next
        return head
        