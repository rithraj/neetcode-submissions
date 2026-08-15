# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head):
            rev, node = None, head

            while node:
                temp = node.next
                node.next = rev
                rev = node
                node = temp
            return rev
        
        reversed_node = reverse(head)
        curr = reversed_node
        count = 1
        prev = None
        for _ in range(n - 1):
            prev, curr = curr, curr.next

        if prev is None:
            reversed_node = curr.next 
        else:
            prev.next = curr.next


        final_head = reverse(reversed_node)

        return final_head
        
        
        