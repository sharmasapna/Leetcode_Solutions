# 1762
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ## naive solution gives TLE
        ## time complexity n-squared
        # res = []
        # l = len(heights) - 1
        # for i in range(l):
        #     print(i, heights[i], max(heights[i+1:]))
        #     if heights[i] > max(heights[i+1:]):
        #         res.append(i)
        #         print('result',res)

        # res.append(l)
        # return res

        # ######## Linear iteration
        #     # If the current building is taller, 
        #     # it will block the shorter building's ocean view to its left.
        #     # So we pop all the shorter buildings that have been added before.
        #     # time complexity is n 

        # res = []
        # l = len(heights)
        # for i in range(l):
        #     # compare heights[i],heights[res[-1]] 
        #     while res and heights[i] >= heights[res[-1]]:
        #         # keep on popping if the previous buildings height is less
        #         res.pop()
        #     res.append(i)
        # return res

        # ###### monotonic stack implementation
        # # If the building to the right is smaller, we can pop it, and keep popping the index from the stack till we get a building greater than the current building or stack becomes empty. If the stack becomes empty, it means there is no building to the right that can block the view for the current building
        # # time complexity is n  and space complexity is n

        # res = []
        # l= len(heights)
        # stack = []
        # for i in reversed(range(l)):
        #     while stack and heights[stack[-1]] < heights[i]:
        #         stack.pop()
        #     if not stack: 
        #         res.append(i)
        #     stack.append(i)
        # return res[::-1]

        ## optimizing on space 
        # time complexity n and space complexity O(1)
        l = len(heights)
        res = []
        max_height = -1

        for i in reversed(range(l)):
            if heights[i] > max_height:
                res.append(i)
                max_height = heights[i]
        return (reversed(res))
