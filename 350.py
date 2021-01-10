#350
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            nums1,nums2 = nums2,nums1
        from collections import Counter
        dic = Counter(nums2)
        res = []
        for val in nums1:
            if dic[val] > 0:
                res.append(val)
                dic[val]-=1
        return res
