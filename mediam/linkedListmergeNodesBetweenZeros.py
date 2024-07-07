# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        tail=dummy
        current=head
        while current:
            if current.val==0:
                current=current.next
                sum_val=0
                while current and current.val!=0:
                    sum_val+=current.val
                    current=current.next
                if current:
                    new_node=ListNode(sum_val)
                    tail.next=new_node
                    tail=tail.next
        return dummy.next
                
        