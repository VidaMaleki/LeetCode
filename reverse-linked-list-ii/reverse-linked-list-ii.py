# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left-1):
            prev = current # 1
            current = current.next # 2
            
        for _ in range(left, right):
            # if current is None or current.next is None: 
            #     break
            next_node = current.next # 3
            current.next = next_node.next # Remove the next_node from the list #4
            next_node.next = prev.next # Insert next_node after prev #2
            prev.next = next_node # 3
        return dummy.next         
            