# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        current = head
        
        lenHead = 0
        
        while current != None:
            lenHead += 1
            current = current.next
            
        dec = 0
        
        i = 0
        current = head
        while current != None:
            
            dec += (2 ** (lenHead - i - 1)) * current.val
            #print(dec)
            i += 1
            current = current.next
        
        return dec
        
