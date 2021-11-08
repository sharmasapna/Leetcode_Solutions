#438
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # if length of string is less than the anagram then return blank list
        if len(p) > len(s):
            return []
        # creating dictionaries of anagram and first anagram from the string
        pdic,sdic = {},{}
        for i in range(len(p)):
            pdic[p[i]] = 1 + pdic.get(p[i],0)
            sdic[s[i]] = 1 + sdic.get(s[i],0)
        
        res = [0] if pdic == sdic else []
        # the sliding window has two counters left and right
        left = 0
        for right in range(len(p),len(s)):
            # adding the next right element in sdic
            sdic[s[right]] = 1 + sdic.get(s[right],0)
            
            # removing the left element from sdic
            sdic[s[left]] -= 1
            
            # if the value of removed element is zero, then we remove it from sdic
            if sdic[s[left]] == 0:
                sdic.pop(s[left])
            # increamenting the left counter
            left += 1
            # checking the new window for anagram
            if sdic == pdic:
                res.append(left)
        return res
        
