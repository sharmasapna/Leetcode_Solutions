#474
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n : int
        :rtype: int
        """
        # we follow the dp approach
        # m is the number of zeros
        # n is the number of ones
        # we create a 2d dp with total m+1 rows and n+1 columns 
        
        dp = []
        for i in range(n+1):
            r = []
            for j in range(m+1):
                r.append(0)
            dp.append(r)
        #print(dp)
        # we will reduce the number of zeros and ones 
        #from max count as is  available in the current string till difference is zero
        # so for "0001"  zeros = 3 and ones = 1 we iterate from m to 3 and n to n
        # since we are iterating in reverse order, we set the limits to m-1 and n-1
        # to include m and n
        def p(matrix):
            for row in matrix:
                print(row)
        for s in strs:
            ones = s.count("1")
            zeros = s.count("0")
            for i in range(n,ones-1,-1):
                for j in range(m,zeros-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-ones][j-zeros]+1)
                    #print(s)
                    #p(dp)
                    #print("--")
        return dp[n][m]
            
        
        
        
        
        
        ## recursive approach goves time limit exceeded
#         ret = []
#         self.dfs(strs,m,n,[],ret)
#         maxlen = 0
#         for i in ret:
#             if len(i)>maxlen: 
#                 maxlen = len(i)
#         return (maxlen)

#     def dfs(self, strs, m,n, path,ret):
#         #print(strs,m,n,path,ret)
#         if  "".join(path).count("0") <= m and "".join(path).count("1") <= n:
#             ret.append(path)
#             #return
#         for i in range(len(strs)):
#             #print (i)
#             self.dfs(strs[i+1:], m,n, path+[strs[i]],ret)
   
        
