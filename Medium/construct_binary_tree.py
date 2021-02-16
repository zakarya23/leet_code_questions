# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        if len(preorder) == 0: 
            return None 
        
        root = TreeNode(preorder[0])
        
        smaller = [x for x in preorder[1:] if x < root.val]
        larger = [x for x in preorder[1:] if x > root.val]
        
        root.left = self.bstFromPreorder(smaller)
        root.right = self.bstFromPreorder(larger)
        return root 
        