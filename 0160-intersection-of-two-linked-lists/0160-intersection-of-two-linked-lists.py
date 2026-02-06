# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # freqMap={}
        # temp1=headA
        # while(temp1!=None):
        #     if temp1 in freqMap:
        #         return temp1
        #     freqMap[temp1]=1
        #     temp1=temp1.next
        # temp2=headB
        # while(temp2!=None):
        #     if temp2 in freqMap:
        #         return temp2
        #     temp2=temp2.next
        # return None

        # compute the length 1
        temp1=headA
        lengthA=0
        while(temp1!=None):
            lengthA=lengthA+1
            temp1=temp1.next
        # computee the length 2
        temp2=headB
        lengthB=0
        while(temp2!=None):
            lengthB=lengthB+1
            temp2=temp2.next
        # move the pointer by length2-length 1 times 
        if(lengthA>lengthB):
            # move the linkedlistA by d times
            temp1=headA
            temp2=headB
            k=lengthA-lengthB
            while(k!=0):
                temp1=temp1.next
                k=k-1
        # move the linkedlistB by d times
        else:
            temp2=headB
            temp1=headA
            k= lengthB-lengthA
            while(k!=0):
                temp2=temp2.next
                k=k-1
        # then move the temp1 and temp2 by one unit each and start comparing if they r same return the pointer 
        while(temp1!=None and temp2!=None):
            if(temp1==temp2):
                return temp1
            temp1=temp1.next
            temp2=temp2.next
        