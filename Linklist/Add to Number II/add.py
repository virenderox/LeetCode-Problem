# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        if l1 is None:
            return l2
    
        if l2 is None:
            return l1
        
        dummyNode = head = ListNode(-1)
        
        carry = 0
        
        while l1  and l2 :
            
            sumDigit = l1.val + l2.val + carry
            carry = sumDigit // 10
            sumDigit = sumDigit % 10
            newNode = ListNode(sumDigit)
            dummyNode.next = newNode
            dummyNode = dummyNode.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            
            sumDigit = l1.val  + carry
            
            carry = sumDigit // 10
            sumDigit = sumDigit % 10
            newNode = ListNode(sumDigit)
            dummyNode.next = newNode
            dummyNode = dummyNode.next
            l1 = l1.next
            
        while l2:
            
            sumDigit =  l2.val + carry
            carry = sumDigit // 10
            sumDigit = sumDigit % 10
            newNode = ListNode(sumDigit)
            dummyNode.next = newNode
            dummyNode = dummyNode.next
            l2 = l2.next
            
        if carry == 1:
            newNode = ListNode(1)
            dummyNode.next = newNode
            
        return self.reverseList(head.next)
        
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
