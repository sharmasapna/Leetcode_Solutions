#2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# points to rememeber:
#1. carry has to be calculated and the current val has to be taken as the units place value
#2. There may be a possibility the the number of nodes are not equal
#3. There may be a carry in the last addition so we may need to add a new node for carry
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0                          # initially the carry is zero
        while l1 or l2 or carry:           # we have to consider carry as this may occur when both 
                                           # l1 and l2 exhaust
            v1 = l1.val if l1 else 0       # return None if l1 node is not present
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            
            # calculation carry and value to be inserted
            carry = val // 10
            val = val%10
            
            # linking the dummy node to the new node with the value we have just created
            curr.next = ListNode(val)
            
            # incrementing the pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next
        return dummy.next
   
        
