class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for val in nums:
            if val in dic:
                dic[val] += 1
            else :
                dic[val] = 1
        s = sorted(dic.keys())
        
        l = len(dic)
        i=0
        max_val =0
        while i <l-1:
            if s[i+1] -s[i] == 1:
                max_val = max(max_val,dic[s[i+1]]+dic[s[i]])
            i+=1
        return max_val
