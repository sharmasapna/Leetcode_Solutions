#167
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i,val in enumerate(numbers):
            #print(val,dic)
            diff = target - val
            
            if diff in dic:
                #print("ji")
                return [dic[diff]+1,i+1]
                #return sorted([dic.index(val)+1,i+1])
            else:
                dic[val] = i
                
