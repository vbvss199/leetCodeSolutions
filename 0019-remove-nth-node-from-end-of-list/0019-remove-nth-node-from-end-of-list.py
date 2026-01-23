# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # lets try this removing from back side
        length =0
        temp=head
        while(temp!=None):
            length=length+1
            temp=temp.next
        if head == None:
            return None
        if n == length:
            return head.next
        else:
            count=0
            temp=head
            prev=None
            while(temp!=None):
                if count == length - n :
                    prev.next = temp.next
                    break
                prev = temp         
                temp = temp.next
                count += 1  
            return head 

