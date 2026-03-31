# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        carry = 0
        dummy = ListNode()
        cur = dummy
        while(cur1 != None or cur2 != None or carry != 0):
            first = cur1.val if cur1 is not None else 0
            second = cur2.val if cur2 is not None else 0
            value = carry + first + second
            num = value % 10
            carry = 0 if value < 10 else (value - num)//10
            new_node = ListNode(num)
            cur.next = new_node
            cur = cur.next
            if cur1 != None:
                cur1 = cur1.next
            if cur2 != None:
                cur2 = cur2.next
        return dummy.next

                