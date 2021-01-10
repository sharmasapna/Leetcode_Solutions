#141
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        if head.next == None:
            return False
        dic = {}
        n = head.next
        while n != None:
            n = head.next
            if n in dic:
                return True
            dic[n] = 1
            head = n
        return False
