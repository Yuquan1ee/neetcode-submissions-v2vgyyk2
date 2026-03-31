# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def height(root):
            nonlocal res
            if not root:
                return 0
            left_root_height = height(root.left) 
            right_root_height = height(root.right)
            cur_diameter = left_root_height + right_root_height
            if cur_diameter > res:
                res = cur_diameter
            return max(left_root_height,right_root_height) + 1

        height(root)

        return res