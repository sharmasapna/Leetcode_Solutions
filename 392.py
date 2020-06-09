#392
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        i,j = 0,0
        l = len(t)
        m=0
        while l>0:
            if s[i] == t[j]:
                i+=1
                j+=1
                l-=1
                m+=1
            else:
                j+=1
                l-=1
            if m == len(s):
                return True
        return False
