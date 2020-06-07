#406
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        x = sorted(people,key = lambda x :(-x[0],x[1])) # sorting in descending order of height and then by position
        #print x
        res = []
        for val in x:
            res.insert(val[1],val) #inserting the value to the correct position
        return res
