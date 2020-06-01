# June Challenge day1
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # we use preorder traversal of binary tree and invert at each node
        def preorder_traversal(root): 
            if root:  
                print(root.val)                             # print the data of node
                root.left,root.right = root.right,root.left # invert the child nodes
                preorder_traversal(root.left)               # recur on left child till no node is left
                preorder_traversal(root.right)              # recur on right child 
        preorder_traversal(root)
        return root
