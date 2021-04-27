#77
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        self.dfs(list(range(1, n+1)), k, [], ret)
        return ret
    
    def dfs(self, nums, k, path, ret):
        print(nums,path,ret)
        if len(path) == k:
            ret.append(path)
            return 
        for i in range(len(nums)):
            print(i)
            #print(nums[i+1:],k,path+[nums[i]],ret)
            self.dfs(nums[i+1:], k, path+[nums[i]], ret)
    # flow of the dfs
    # ([1, 2, 3, 4], [], [])
    # i=0
    # ([2, 3, 4], [1], [])
        # i=0 (inner loops)
        # ([3, 4], [1, 2], [])
        # i=1
        # ([4], [1, 3], [[1, 2]])
        # i=2
        # ([], [1, 4], [[1, 2], [1, 3]])
    # i=1
    # ([3, 4], [2], [[1, 2], [1, 3], [1, 4]])
        # i=0
        # ([4], [2, 3], [[1, 2], [1, 3], [1, 4]])
        # i=1
        # ([], [2, 4], [[1, 2], [1, 3], [1, 4], [2, 3]])
    # i=2
    # ([4], [3], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4]])
        # i=0
        # ([], [3, 4], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4]])
    # i=3
    # ([], [4], [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]])


    
