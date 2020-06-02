#1436
class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        list_s = [] # list with source
        list_d = [] # list with destination
        for val in paths:
            list_s.append(val[0])
            list_d.append(val[1])
        for val in list_d:
            if val not in list_s: # checking if the destination is available in source
                return val
