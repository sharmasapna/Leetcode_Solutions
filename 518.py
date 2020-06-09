#518
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        c = amount+1
        r = len(coins)+1
        coins = [0] + coins
        
        # creating a 2-D matrix for storing the results for future use and calculations
        m = [[0 for x in range(c)] for y in range(r)] 
        m[0][0] =1 # base case
     
        for i in range(1,r):
            for j in range(c):
                if coins[i] >j :
                    m[i][j] = m[i-1][j]
                else:
                    m[i][j] = m[i-1][j] + m[i][(j-coins[i])]
        return  m[r-1][c-1]
        # Since we are using the elements just above the and in the same row
        # we can do it in 1-D array as follows
        dp = [0]*(amount) + 1
        dp[0] = 1 # base case
        for i in coins:
            for j in range(i, amount + 1):
                  dp[j] += dp[j - i]
        return dp[amount]
        
        
    
