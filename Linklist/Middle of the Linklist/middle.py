# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        single = head
        double = head
        tmp = head
        lenHead = 0
        
        
        while tmp.next != None:
            tmp = tmp.next
            lenHead += 1
            
        
        if head.next is None:
            return head
        
        if head.next.next is None:
            return head.next
        
        
        
        if lenHead % 2 == 0:   
            while(double.next != None):
                single = single.next
                double = double.next.next
        else:
             while(double != None):
                single = single.next
                double = double.next.next
            

        return single
        
