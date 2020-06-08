#796
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        
        if A == B:
            return True
        l = len(A)
        print l
        while (l > 0):
            temp = A[1:]+A[0]
            if temp == B:
                return True
            A = temp
            l=l-1
        return False
        #A more elegsnt way to do the same is as follows
        return len(A) ==len(B)  and B in A+A # what we did in loop, it is done in 1 line!
