# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
         
        def sameTree(root,subroot):
            if not root and not subroot :
                return True
            
            elif root and subroot:
                if root.val == subroot.val:
                    return sameTree(root.left, subroot.left) and sameTree(root.right,subroot.right)
                else:
                    return False
            else:
                return False

        queue = deque([root])
        while(queue):
            root = queue.popleft()
            if sameTree(root,subRoot):
                return True
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)

        return False

            