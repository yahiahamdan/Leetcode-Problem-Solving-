class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next
def findMostFrequent(head):
   current=head
   freq={}
   while current:
       if current.val in freq:
           freq[current.val]+=1
       else:
            freq[current.val]=1
       current=current.next
   most_frequnet_val=None
   max_freq=0
   for key,value in freq.items():
       if  value>max_freq:
              max_freq=value
              most_frequnet_val=key
   return most_frequnet_val
        
   
           