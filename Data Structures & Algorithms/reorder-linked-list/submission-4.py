# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half IN PLACE
        prev, curr = None, slow.next
        slow.next = None  # sever the two halves
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # prev is now head of reversed second half

        # 3. Merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
                   



        
