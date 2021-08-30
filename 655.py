#655 Medium
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        # we define a function to get the height of the tree
        def get_height(node):
            if not node:
                return 0
            else:
                return 1 + max(get_height(node.left),get_height(node.right))
        height = get_height(root)
        width = 2**height - 1
        # creating the matrix that will print the tree
        self.print_bt =[]
        for row in range(height):
            t = []
            for col in range(width):
                t.append("")
            self.print_bt.append(t)
        # the recursive function to travel all nodes and fill the matrix at correct positions
        def print_tree(node,row,left,right):
            if not node:
                return
            mid = (left + right)/2
            if node:
                self.print_bt[row][mid] = str(node.val)
                row +=1
                #print(self.print_bt)
                print_tree(node.left,row,left,mid-1)
                print_tree(node.right,row,mid+1,right)
        # initialize the tree with row = 0, left = 0 and right = width-1
        print_tree(root,0,0,width-1)
        #print(self.print_bt)
        return self.print_bt
