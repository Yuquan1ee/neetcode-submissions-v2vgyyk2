# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        hash_map =set()
        while(node is not None):
            print(node)
            if node in hash_map:

                return True
            else:
                hash_map.add(node)
                print(hash_map)
                node = node.next

        return False