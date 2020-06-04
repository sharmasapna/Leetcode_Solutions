#1029
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key = lambda x:x[0]-x[1]) # sorting by the profit by sending to destination A rather                                                     than B

        l = len(costs)/2
        tot = 0
        for i in range(l):
            tot += costs[i][0] +costs[i+l][1] # sending the first half to A and the next to B
        return tot
