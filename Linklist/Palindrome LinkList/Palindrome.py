# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #approch one by reversing and check
        l2 = head
        l1 = head
        new = None
        flag = True
        while l1:
            newNode = ListNode(l1.val)
            #print(newNode)
            if flag == True:
                new = newNode
                current = new
                flag = False
            else:
               # print("value of new:    " , new)
                current.next = newNode
                current = current.next
            l1 = l1.next
           
            
        #print(new)
        l2 = self.reverseList(l2)
       # print(new)
    
        
        while new  and l2 :
            if new.val != l2.val:
                #print("hy")
                return False
            
            new = new.next
            l2 = l2.next
        
        return True
            
    
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
        
