# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        
        if not preorder:
            print("no node")
            return None
        cur_node = TreeNode(preorder[0])
        print(cur_node.val)
    
        
        cur_node.left = self.buildTree(preorder[1:1+inorder.index(cur_node.val)], inorder[:inorder.index(cur_node.val)])
        cur_node.right = self.buildTree(preorder[inorder.index(cur_node.val)+1:], inorder[inorder.index(cur_node.val)+1:])
        return cur_node

        




##### fking difficult question #####must keep doing it again

# The preorder helps to find the root to do the recursive on



