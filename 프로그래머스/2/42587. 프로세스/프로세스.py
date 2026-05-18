from collections import deque

def solution(priorities, location):
    
    dq = deque(enumerate(priorities))
    
    count = 0
    while dq:
        current = dq.popleft()
        
        if any(item[1] > current[1] for item in dq):
            dq.append(current)
        else:
            count += 1
            if current[0] == location:
                return count
        