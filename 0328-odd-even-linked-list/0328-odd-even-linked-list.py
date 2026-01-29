# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if(head is None or head.next is None):
        #     return head 
        # arr=[]
        
        # temp=head
        # while(temp!=None and temp.next!=None):
        #     arr.append(temp.val)
        #     temp=temp.next.next
        # #after reaching the end it will not count the element 
        # # so check if temp present
        # if(temp):
        #     arr.append(temp.val)
        
        # temp=head.next
        # while(temp!=None and temp.next!=None ):
        #     arr.append(temp.val)
        #     temp=temp.next.next
        # if(temp):
        #     arr.append(temp.val)

        # temp=head
        # i=0
        # while (temp!=None):
        #     temp.val=arr[i]
        #     temp=temp.next
        #     i=i+1
        # return head
        # idk why the naive solution did pass even after using the O(n) space complexity where the quesiton prompted to do within O(1)
        if (head is None or head.next is None):
            return head 
        odd=head
        even=head.next
        temp=head
        even_head=head.next # this one used for connecting the odd indices to even indices 
        #will i write for odd or even or both , the main condition is to check on the even_node 
        while( even!=None and even.next!=None):
            odd.next=odd.next.next
            even.next=even.next.next 

#the moment odd is pointing to 1 so the list becomes odd → 2 → 1 → 4 → 5 → 6 so here the odd is till pointing to 2 so move odd again
            odd=odd.next
            even=even.next
        odd.next=even_head
        return head 

            
             