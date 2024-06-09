"""
i have 2 pairs i want to check if pair one can reach to pair final 
i have moves 
(a,b)  =>(a+b,b)  or (a,b+a) so how i can do that
"""
from collections import deque
def isPossible(a,b,x,y):

    queue = deque([(a, b)])
    visited = set([(a, b)])
    while queue:
        current_a, current_b = queue.popleft()
        
        # Check if we've reached the destination
        if (current_a, current_b) == (x, y):
            return True
        
        # Generate the next points
        next_points = [(current_a + current_b, current_b), (current_a, current_b + current_a)]
        
        for next_a, next_b in next_points:
            # Check bounds and if the point has been visited
            if next_a <= x and next_b <= y and (next_a, next_b) not in visited:
                queue.append((next_a, next_b))
                visited.add((next_a, next_b))
    
    return False
 
print(isPossible(2,3,7,1))

    