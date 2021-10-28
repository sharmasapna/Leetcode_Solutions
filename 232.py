#232
class MyQueue:
# We use s1 and s2 arrays to implement queue
# s1 contains the elements of queue at any given time
# s2 is used for pop() operation, where all elements of s1 are transfered to s2
# and the last element of s2 is poped out and again the remaining elements of s2
# are transfered back to s1
# for peek() operation the first element of s1 is returned
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)
        
    def pop(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        val = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return val 

    def peek(self) -> int:
        return self.s1[0]
    
    def empty(self) -> bool:
        return len(self.s1) == 0
