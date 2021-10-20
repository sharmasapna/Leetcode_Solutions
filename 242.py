#242
from collections import defaultdict,Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
## Comparing the sorted strings
        return sorted(s) == sorted(t)
## Comparing two hash maps
        return Counter(s) == Counter(t)
        
## intutive solution         
        dic = {}
        
        for a in s:
            if a in dic:
                dic[a] += 1
            else:
                dic[a] = 1
        for b in t:
            if b in dic:
                dic[b] -= 1
            else:
                dic[b] = -1
        #print(max(dic.values()))
        if max(dic.values()) == 0 and min(dic.values()) == 0:
            return True
## for video pl watch : https://www.youtube.com/watch?v=9UtInBqnCgA
            
