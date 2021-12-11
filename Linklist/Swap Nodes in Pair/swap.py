# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.pairSwap(head)
    
    def pairSwap(self, head):
        
        if head is None or head.next is None:  ## base condition for recursive call
            return head 
        
        firstNode = head
        secondNode = head.next
        
        tempList = self.pairSwap(head.next.next)
        
        firstNode.next = tempList
        secondNode.next = firstNode
        
        return secondNode
        
