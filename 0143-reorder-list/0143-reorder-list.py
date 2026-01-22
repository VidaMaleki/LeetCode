# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # Find middle
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # Reverse second half
        prev = None
        current = slow.next
        slow.next = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
    
        # Merge both
        second = prev
        first = head
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
            
            
        