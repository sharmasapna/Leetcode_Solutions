#1209
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lst = []
 
        for char in s:
            current = (char,1)
            if len(lst)==0:
                lst.append(current)
            else:
                last = lst.pop()
                if last[0] != current[0]:
                    lst.append(last)
                    lst.append(current)
                else:
                    if last[1]+1 < k:
                        lst.append((char,last[1]+1))
        res =''
        for a,b in lst:
            res += a*b
        return res
