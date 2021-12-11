# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.reverseLinkedListInKGroup(head,k)
    
    def reverseLinkedListInKGroup(self,head,k):
        
        if head is None:
            return head
        
        current = head
        currentLength = 1
        
        while current.next is not None and currentLength < k:
            current = current.next
            currentLength += 1
            
        if currentLength < k:
            return head
        
        tempNode = current.next
        current.next = None
        
        prev = None
        current = head
        
        
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        tempList = self.reverseLinkedListInKGroup(tempNode,k)
        head.next = tempList
        
        return prev
            
