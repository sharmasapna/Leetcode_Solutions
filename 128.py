# 128 Medium
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_streak = 0
        
        # we create a set as it allows O(1) lookups
        set_num = set(nums)
        
        for num in set_num:
            # we check if the previous number is present or not. If the previous number is present, then there could be a number previous to that in the sequence. So we discard it.
            if num-1 not in set_num:
                current_num = num
                current_streak = 1
            
                while current_num+1 in set_num:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak
                
        
            
        
