class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic = {}
        for val in arr:
            if val in dic:
                dic[val] +=1
            else:
                dic[val] = 1
        """
        res = []
        for key,val in dic.items():
            res.append(val)
        return (len(res) == len(set(res)))
        """
        # the above code can be replaced as follows:
        return (len(dic) == len(set(dic.values())))
