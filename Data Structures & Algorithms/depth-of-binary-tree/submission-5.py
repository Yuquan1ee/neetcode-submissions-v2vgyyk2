# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        if not root:
            return max_depth
        
        holding_list = [(root,1)]
        max_depth = 1
        while(len(holding_list)):
            cur_node,cur_depth = holding_list.pop(0)
            if cur_node.left:
                holding_list.append((cur_node.left,cur_depth+1))
                if cur_depth + 1 >max_depth:
                    max_depth = cur_depth + 1
            if cur_node.right:
                holding_list.append((cur_node.right,cur_depth+1))
                if cur_depth +1 > max_depth:
                    max_depth = cur_depth + 1

        return max_depth