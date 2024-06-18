class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reorderList(self,head):
    slow,fast=head,head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    #revers the secnod half
    prev,curr=None,slow.next
    slow.next=None
    while curr:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
    #merge the two halves
    first,second=head,prev
    while second:
        next_node=first.next
        first.next=second
        first=second
        second=next_node
    return head
