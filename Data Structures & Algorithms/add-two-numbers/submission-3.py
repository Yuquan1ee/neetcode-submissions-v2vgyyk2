# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        multiplier = 1
        total_sum = 0
        cur1 = l1
        cur2 = l2
        while(cur1 is not None):
            total_sum += multiplier * cur1.val
            multiplier = multiplier * 10 
            cur1 = cur1.next
        multiplier = 1
        while(cur2 is not None):
            total_sum += multiplier * cur2.val
            multiplier = multiplier * 10 
            cur2 = cur2.next

        num = total_sum % 10
        start_node = ListNode(num)
        total_sum = (total_sum - num)//10
        cur = start_node
    
        while(total_sum!=0):
            num = total_sum % 10
            new_node = ListNode(num)
            cur.next = new_node
          
            cur = cur.next
            total_sum = (total_sum - num)//10




        return start_node
       