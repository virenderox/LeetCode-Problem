# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        oddPos = True
        
        oddDummyNode = ListNode(-1)
        evenDummyNode = ListNode(-1)
        
        current1 = oddDummyNode
        current2 = evenDummyNode
        
        current = head
        
        while current is not None:
            
            if oddPos is True:
                newNode = ListNode(current.val)
                current1.next = newNode
                current1 = current1.next
                oddPos = False
                
            else:
                newNode = ListNode(current.val)
                current2.next = newNode
                current2 = current2.next
                oddPos = True
                
            current = current.next
            
        current1.next = evenDummyNode.next
        return oddDummyNode.next
                
