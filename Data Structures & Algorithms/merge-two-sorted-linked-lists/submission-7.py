# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        if cur1.val<cur2.val:
            head = cur1
            loop_list = cur2
            pointer = cur1
        else:
            head = cur2
            loop_list = cur1
            pointer = cur2
        while(loop_list is not None):
            if pointer.next is not None and pointer.val <=loop_list.val<=pointer.next.val:
                temp = loop_list
                loop_list = loop_list.next
                temp.next = pointer.next
                pointer.next = temp
                pointer = pointer.next
                print(f"inserted:{temp.val}")
            elif pointer.next is not None and loop_list.val > pointer.next.val:
                print("2")
                pointer = pointer.next
            
            else:
                pointer.next = loop_list
                break

        return head


        
    
        

        
        