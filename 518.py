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
        
       
        m = [[0 for x in range(c)] for y in range(r)] 
        m[0][0] =1 # base case
     
        for i in range(1,r):
            for j in range(c):
                if coins[i] >j :
                    m[i][j] = m[i-1][j]
                else:
                    m[i][j] = m[i-1][j] + m[i][(j-coins[i])]
        return  m[r-1][c-1]
