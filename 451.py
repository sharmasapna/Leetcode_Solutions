class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        c = Counter(s)
        """
        # You can run the code below to understand how the  single line code works
        print c.items() # see what is in variable c
        print sorted(c.items()) # got sorted on first element
        print sorted(c.items(),key = lambda x:x[1]) # we want to sort on frequency i. second element
        print sorted(c.items(),key = lambda x:x[1],reverse = True) # we want revrse sorting 
        for a,b in sorted(c.items(),key = lambda x:x[1],reverse = True):
            print a,b 
        for a,b in sorted(c.items(),key = lambda x:x[1],reverse = True):
            print a*b # we want to repeat the letter as per its frequency
        #joining the result obtained in a single line
        print ''.join(a*b for a,b in  sorted(c.items(),key = lambda x: x[1],reverse = True))
        """
        return ''.join(a*b for a,b in  sorted(c.items(),key = lambda x: x[1],reverse = True))
            
        ## for lamba functions refer https://www.youtube.com/watch?v=25ovCm9jKfA&feature=youtu.be
