# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        freqMap={}
        temp1=headA
        while(temp1!=None):
            if temp1 in freqMap:
                return temp1
            freqMap[temp1]=1
            temp1=temp1.next
        temp2=headB
        while(temp2!=None):
            if temp2 in freqMap:
                return temp2
            temp2=temp2.next
        return None
        