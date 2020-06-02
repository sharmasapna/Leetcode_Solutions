# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # original linked list
        #ListNode{val: 4, next: ListNode{val: 5, next: ListNode{val: 1, next: ListNode{val: 9, next: None}}}}

        # strucure of the node to be deleted
        # ListNode{val: 5, next: ListNode{val: 1, next: ListNode{val: 9, next: None}}}
        
        node.val = node.next.val # replacing the vaue of the current node with the value of the next node
        node.next = node.next.next # replacing the current "next" pointer with  the next's next pointer
        
        # final linked list after deleting the node given
        # ListNode{val: 4, next: ListNode{val: 1, next: ListNode{val: 9, next: None}}}
