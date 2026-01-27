# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev=None
        # curr=head
        # while curr:
        #     nxt=curr.next #save next
        #     curr.next=prev  #reverse the pointers 
        #     prev=curr #move previous pointer
        #     curr=nxt #move curr pointer 
        # return prev

        # naive approach using stack lifo principle
        stack=[]
        temp=head
        while(temp!=None):
            stack.append(temp.val)
            temp=temp.next
        temp=head
        while(temp!=None):
            temp.val=stack.pop()
            temp=temp.next
        return head