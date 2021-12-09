# Approch 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        current = head
        lenHead = 0
        
        while current != None:
            lenHead += 1
            current = current.next
        
        current = head
        for i in range(0, lenHead - n - 1):
            current = current.next
            
        if n == lenHead:
            #print(current.val, current.next.val)
            head = current.next
            
        elif current.next.next is None:
            current.next = None
            
        else:
           # print("hy")
            #print(current.val)
            
            current.next = current.next.next
        
        return head
    
