#21
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = res = ListNode()
        
        while l1 or l2:
            temp = ListNode()
            if not l1:
                res.next = l2
                break
            if not l2:
                res.next= l1
                break
            
            if l1.val < l2.val:
                res.next = ListNode(l1.val)
                l1 = l1.next
            else:
                res.next = ListNode(l2.val)
                l2 = l2.next
            res = res.next
            #print(res)
        #print(r.next)
        return r.next
                    
        
