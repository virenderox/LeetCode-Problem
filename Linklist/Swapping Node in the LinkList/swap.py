# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        runner = head
        prev = None
        
        for i in range(k):
            prev = runner
            runner = runner.next
            
        follower = head
            
        while runner is not None:
            runner = runner.next
            follower = follower.next
            
        prev.val, follower.val = follower.val , prev.val
        
        return head
            
        
        
        
