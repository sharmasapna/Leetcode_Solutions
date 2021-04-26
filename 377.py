#377
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        #         1 => [1]
        #         2 => [1 1] [2]
        #         3 => [1 1 1] [1 2] [1 2] [3]
        #         4 => [1 1 1 1] [1 1 2] [1 2 1] [2 1 1] [2 2] [1 3] [3 1]

        #         dp =[1, 2, 3, 7]
        #         nums = [1,2,3]
        
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1,len(dp)):
            for num in nums:
                if num-i <=0:
                    dp[i] +=dp[i-num]
        return dp[-1]
