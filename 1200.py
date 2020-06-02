#1200
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        """
        ## Method I
        arr  = sorted(arr)
        
        dic = {}
        i=0
        l = len(arr)
        while i <l-1:
            diff = arr[i+1] - arr[i]
            if diff in dic:
                dic[diff] = dic[diff]+[[ arr[i], arr[i+1]]]
            else:
                dic[diff] =[ [ arr[i], arr[i+1]]]
            i+=1
        min_val = min(dic)
        return dic[min_val]
        """
        """
        ## Method II
        # a more pythonic way of above
        dic ={}
        arr.sort()
        for a,b in zip(arr,arr[1:]):
            dic.setdefault(abs(a-b),[]).append([a,b])
        return dic[min(dic)]
        """
        # Method III faster than above with 2 pass after sorting
        arr.sort()
        mn = min(b-a for a,b in zip(arr,arr[1:]))
        return [[a,b] for a,b in zip(arr,arr[1:]) if b-a == mn]
