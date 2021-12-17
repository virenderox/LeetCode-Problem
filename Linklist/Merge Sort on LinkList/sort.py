# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        return self.mergeSort(head)
        
    def mergeSort(self,head):
        
        if head is None or head.next is None:
            return head
        
        slow = head
        fast = head
        
        while fast and fast.next and fast.next.next :
            fast = fast.next.next
            slow = slow.next
        
       # print(head)
        
        l2 = slow.next
        slow.next = None
        l1 = head
        
        left = self.mergeSort(l1)
        #print(left)
        right = self.mergeSort(l2)
        
        return self.mergeTwoLists(left,right)
        
        
        
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
       # if l1 is None:
        #    return l2
       # if l2 is None:
         #   return l1
        
        dummyNode = ListNode(-101)
        head = dummyNode
        
        while l1 is not None and l2 is not None:
            
            if l1.val < l2.val:
                newNode = ListNode(l1.val)
                dummyNode.next = newNode
                l1 = l1.next 
                
            else:
                newNode = ListNode(l2.val)
                dummyNode.next = newNode
                l2 = l2.next
                
            dummyNode = dummyNode.next
            
        if l1 is not None:
            dummyNode.next = l1
        
        if l2 is not None:
            dummyNode.next = l2
            
        return head.next
        
