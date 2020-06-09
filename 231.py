#231
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        while (n):
            if n == 1:
                return True
            if n%2 == 0:
                n=n/2
            else:
                return False
