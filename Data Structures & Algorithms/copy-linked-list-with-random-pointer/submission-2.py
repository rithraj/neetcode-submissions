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
        mapping = {None:None}

        node = head

        while node:
            copy = Node(node.val)
            mapping[node] = copy
            node = node.next
        
        node = head
        while node:
            copy = mapping[node]
            copy.next = mapping[node.next]
            copy.random = mapping[node.random]
            node = node.next
        
        return mapping[head]

        