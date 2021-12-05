# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        previous = None
        current = head
        tmp = head
        
        if head == None:
            return head
        
        else:
            while(current != None):
                current = current.next
               # print(current.val)
                tmp.next = previous
                previous = tmp
                tmp = current

            head = previous
            

        return head
        
