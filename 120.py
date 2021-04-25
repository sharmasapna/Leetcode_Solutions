#120
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
       
        #bottom up approach
        l = len(triangle) - 2
        
        while l >= 0:
            for i in range(len(triangle[l])):
                triangle[l][i] += min(triangle[l+1][i],triangle[l+1][i+1])
                #print(triangle)
            l -= 1
        return triangle[0][0]
