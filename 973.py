class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        res = {}
        for i,val in enumerate(points):
            dist = (val[0]*val[0] + val[1]*val[1])**(.5)
            
            res[i] = dist
        res1 = []
        res = sorted(res.items(),key = lambda x:x[1] )
        
        res1 = []
        while K>0:
            res1.append(points[res[K-1][0]])
            K-=1
        return res1
        # A short approach is as follows
        #points.sort(key = lambda P: P[0]**2 + P[1]**2) # no need to take the squareroot
        #return points[:K]
