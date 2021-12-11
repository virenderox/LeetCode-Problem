"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        dummyNode = Node(-100001)
        runner = dummyNode
        current = head
        dic = {}
        while current is not None:
           # print(current.val)
            newNode = Node(current.val)
            runner.next = newNode
            dic[current] = newNode
            current = current.next
            runner = runner.next
            
        current = head
        runner = dummyNode.next
        
        while current is not None:
            if current.random is not None:
                runner.random = dic[current.random]
                
            runner = runner.next
            current = current.next
                
            
        return dummyNode.next
        
        
