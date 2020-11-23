#290
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict ={}
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        for a,b in zip(pattern,str):
            if a not in dict :
                if b not in dict.values():
                    dict[a] = b
                else:
                    return False
            if a in dict and dict[a] != b:
                #print dict
                return False
        return True
