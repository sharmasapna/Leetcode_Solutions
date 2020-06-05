#344
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l= len(s)-1
        i=0
        while i<l:
            s[i] , s[l] = s[l],s[i] #swap first with last and traverse inwards th elist
            i+=1
            l-=1
