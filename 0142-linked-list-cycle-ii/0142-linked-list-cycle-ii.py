# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # naive approach
        temp=head
        freqMap={}
        while(temp!=None):
            if temp in freqMap:
                return temp
            else:
                freqMap[temp]=1
            temp=temp.next
        # ok if cycle exists then we need to return the point where the cycle is starting not the meeting point 
        # it is not necessarily they should meet at the same point always 