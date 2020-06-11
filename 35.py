#35
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l= len(nums)
        i=0
        while(l>0):
            if nums[i] >= target:
                return i
            i+=1
            l-=1
        return len(nums)
        # second method 
        z = []
        for x in nums:
            if x<target:
                z.append(nums)
        return len(z)
        # third method
        if (target in nums):
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
