#118
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        
        for i in range(1 , numRows-1):
            prev = res[-1]
            new = [1]
            for val in range(i):
                v = prev[val]+prev[val+1]
                new.append(v)
            new.append(1)
            res.append(new)
            print(res)    
                

        return res
## by adding zeros in the starting and end and adding the two to get the new row
##  from [1]
## 0 1   0 1 1  0 1 2 1
## 1 0  +1 1 0  1 2 1 0
## 1 1   1 2 1  1 3 3 1 and so on
        res = [[1]]
        for i in range(1,numRows):
            res += [list(map(lambda x,y: x+y , res[-1]+[0], [0]+res[-1]))]
        #print(res)
        return res
### dp approach
        if numRows   == 0: return []
        elif numRows == 1: return [[1]]
        Tri = [[1]]
        for i in range(1,numRows):
            row = [1]
            for j in range(1,i):
                row.append(Tri[i-1][j-1] + Tri[i-1][j]) 
            row.append(1)
            Tri.append(row)
        return Tri
