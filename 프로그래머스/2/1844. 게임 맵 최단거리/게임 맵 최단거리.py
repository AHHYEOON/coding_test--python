from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque([(0,0)])
    maps[0][0] = 0
    
    distance = [[0] * m for _ in range(n)]
    distance[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        
        if x == n-1 and y == m-1:
            return distance[x][y]
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = 0
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx,ny))
    return -1