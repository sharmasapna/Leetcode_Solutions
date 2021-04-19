#509
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        fib_dict = {0:0,
                    1:1}
        for i in range(2,n+1):
                fib_dict[i] = fib_dict[i-1] + fib_dict[i-2]
    
        
        return fib_dict[n]
