# Using breadth first search
# Time complexity - O(2^n)
# Space complexity - O(2^n) worst case
# Did this code run on leetcode? - no (TLE)
from collections import deque
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        queue = deque()
        queue.append((X, 0)) # begin by adding X and step = 0 to the queue.
        
        while queue:         # traverse till the queue is not empty
            X, step = queue.popleft()
            if X==Y:    
                return step
            
            # go to the next multiplication step only if target is greater than the value.
            if X < Y: 
                queue.append((X*2, step+1)) 
            queue.append((X-1, step+1))
    
        return -1


# Turning the problem other way around and using division, and addition to go from Y->X
# Time complexity - O(log Y) problem is divided into half at every step with division
# Space complexity - O(1)
# Did this code run on leetcode? - no (TLE)
from collections import deque
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        step = 0
        
        while Y>X:
            step += 1
            if Y%2==0:
                Y//=2
            else:
                Y+=1
        
        return step + (X-Y)