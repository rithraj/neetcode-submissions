# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        dummy = node = ListNode()
        l1,l2 = head, prev
        l1_count, l2_count = 0,0
        while l1 and l2:
            if l1_count <= l2_count:
                node.next = l1
                l1 = l1.next
                l1_count += 1
            else:
                node.next = l2
                l2 = l2.next
                l2_count += 1
            node = node.next
        node.next = l1 if l1 else l2








        