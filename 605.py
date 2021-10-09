#605
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # when we do not want to plot any flower
        if n==0:
            return True
        # adding zeros in front and end of the array to make computations easy
        new = [0] + flowerbed + [0]
        
        # checking for 3 consequtive zeros
        for i in range(len(new)-2):
            if new[i] == new[i+1] == new[i+2] == 0:
                new[i+1] = 1
                # subtracting from the count
                n-=1
                # as soon as the count becomes zero we need to return True as the condition is met
                if n == 0:
                    return True
             
