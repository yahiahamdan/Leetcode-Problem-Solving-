# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if  not head or k==0:
            return head
        #calculate the length of the list and the tail 
        length=1
        tail=head
        while tail.next:
            length+=1
            tail=tail.next
        #make the list circular to rotate it 
        tail.next=head
        #cacluate the effective rotation needed if k> length so we need modulus 
        k=k%length 
        new_tail_postion=length-k-1
        new_tail=head
        for _ in range(new_tail_postion):
          new_tail=new_tail.next
        new_head=new_tail.next
        new_tail.next=None
        return new_head


        