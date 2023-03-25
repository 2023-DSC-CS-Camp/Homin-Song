import queue

n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(input()))

# 미로 탐색
def solve(maze, n, m):
    count = 1
    end_idx = 0
    start_point = [0, 0]
    passed_paths = []
    queue_investigation = queue.Queue()
    queue_investigation.put(start_point)
    
    # 1번의 while마다 1칸씩 이동
    while(1):
        # print("순환중")
        if(end_idx == 1):
            break
        count += 1
        # 특정 지점에서 이동 가능한 경로들에 대한 진행
        for _ in range(queue_investigation.qsize()):
            x, y = queue_investigation.get()
            print(x, y)
            # 이미 지나간 경로면 패스
            if [x, y] in passed_paths:
                print("이미 지나간 경로면 패스")
                continue
            else:
                print("경로 추가")
                passed_paths.append([x, y])
            # 목표 지점에 도착하면 종료
            if(x == m-1 and y == n-1):
                end_idx = 1
                break
            # 이동 가능한 경우만 탐색
            if(maze[x][y] == '1'):
                possible_directions = investigate_surrounding(maze, x, y, n, m, passed_paths)
                print(possible_directions)
                if possible_directions:
                    queue_investigation.put(possible_directions[0])
        print()
    return count
        
# 동서남북 순으로 탐색
def investigate_surrounding(maze, x, y, n, m, passed_paths):
    possible_direction = []
    
    if(x+1 < m & [x, y] not in passed_paths):
        if(maze[x+1][y] == '1'):
            possible_direction.append([x+1, y])
    if(x-1 >= 0 & [x, y] not in passed_paths):        
        if(maze[x-1][y] == '1'):
            possible_direction.append([x-1, y])
    if(y+1 < n & [x, y] not in passed_paths):        
        if(maze[x][y+1] == '1'):
            possible_direction.append([x, y+1])
    if(y-1 >= 0 & [x, y] not in passed_paths):        
        if(maze[x][y-1] == '1'):
            possible_direction.append([x, y-1])
            
    return possible_direction

if __name__ == "__main__":
    print(solve(maze, n, m))