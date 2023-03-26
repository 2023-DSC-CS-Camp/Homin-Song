import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

movements = [(1,0),(-1,0),(0,1),(0,-1)]
maze[0][0] = 1
q = deque([(0,0)])

while q:
    x,y = q.popleft()
    for dx,dy in movements:
        new_x,new_y = x+dx,y+dy
        if (0<=new_x<m) and (0<=new_y<n) and (maze[new_y][new_x] == '1'):
            q.append((new_x,new_y))
            maze[new_y][new_x] = maze[y][x] + 1
print(maze[n-1][m-1])