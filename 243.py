#243
class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        :type wordsDict: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #initialize the minimum distance to the maximum possible distance between two words
        min_dist = len(wordsDict)
        # initializing the indexes to -1 as we the minimum index starts from 0
        w1 = -1
        w2 = -1
        # traversing the list of words to find indices of word1 and word2
        for i,word in enumerate(wordsDict):
            if word == word1:
                w1 = i
            if word == word2:
                w2 = i
            # we have to ensure that indices of both words have been updated otherwise the minimum value will never be updated and we will get incorrect answer
            if w1 != -1 and w2 != -1:
                min_dist = min(min_dist, abs(w1 - w2))
        return min_dist
            
