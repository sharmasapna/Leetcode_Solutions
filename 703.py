#703
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        # checking the size of the heap and if more than k, we pop till length = 3
        while len(self.heap) > k :
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        #print(val)
        heapq.heappush(self.heap,val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
