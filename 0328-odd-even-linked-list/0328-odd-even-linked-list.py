# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head is None or head.next is None):
            return head 
        arr=[]
        
        temp=head
        while(temp!=None and temp.next!=None):
            arr.append(temp.val)
            temp=temp.next.next
        #after reaching the end it will not count the element 
        # so check if temp present
        if(temp):
            arr.append(temp.val)
        
        temp=head.next
        while(temp!=None and temp.next!=None ):
            arr.append(temp.val)
            temp=temp.next.next
        if(temp):
            arr.append(temp.val)

        temp=head
        i=0
        while (temp!=None):
            temp.val=arr[i]
            temp=temp.next
            i=i+1
        return head