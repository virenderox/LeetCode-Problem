# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        return self.solve_1(head)
        return self.solve_2(head)
    
    
    
    
    #Approch 1 Brute force 
    def solve_1(self,head):
        
        current = head
        dic = {}
        
        while current is not None:
            
            if current in dic:
                return True
            else:
                dic[current] = True
                
            current = current.next
        return False
    
    
    
    #Approch 2 fast and Slow Pointer
    def solve_2(self,head):
            
        
        if head is None or head.next is None:
            return False
        
            
        fast = head.next
        slow = head
        
        if fast.next is None:
            return False
        else:
        
            while slow is not None:
                if fast is None or fast.next is None:
                    return False
                #print(slow.val)
                if fast is slow:
                   # print("hy")
                    return True
                else:
                    slow = slow.next
                    fast = fast.next.next

            
        return False
        
