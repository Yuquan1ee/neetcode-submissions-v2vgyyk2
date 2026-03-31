# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val<=root.val <=q.val or p.val>=root.val>=q.val:
            return root
        elif p.val >root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return self.lowestCommonAncestor(root.left,p,q)




# initial solution of using BFS to find LCA works for general question where there is no BST property. 
# This solution works only cause it is a BST