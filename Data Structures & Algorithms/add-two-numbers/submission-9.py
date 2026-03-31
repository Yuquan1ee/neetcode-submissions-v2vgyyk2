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
        prev = None
        while(cur1 is not None or cur2 is not None or carry >0):
            if cur1 is not None and cur2 is not None:
                value = cur1.val+ cur2.val + carry
                cur1.val = value % 10
            elif cur1 is not None and cur2 is None:
                value = (cur1.val + carry)
                cur1.val = value % 10
            elif cur2 is not None and cur1 is None:
                new_node = ListNode()
                value = (cur2.val + carry)
                new_node.val = value % 10
                prev.next = new_node
                cur1 = new_node
            else:
                new_node = ListNode()
                value = carry
                new_node.val = value % 10
                prev.next = new_node
                cur1 = new_node
            carry = (value - cur1.val)//10
            print(cur1.val, carry)
            prev = cur1
            cur1 = cur1.next
            if cur2 is not None:
                cur2 = cur2.next


        return l1

            
            
        
                

                    
            
       