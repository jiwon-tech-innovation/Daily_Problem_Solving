from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    maze[y][x] = 1
    queue = deque([(x, y)])
    
    while queue:
        cx, cy = queue.popleft()

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            if 0 <= nx < width and 0 <= ny < height:
                if maze[ny][nx] == '1':
                    maze[ny][nx] = int(maze[cy][cx]) + 1
                    queue.append((nx,ny))



height,width = map(int, input().split())
maze = []
for i in range(height):
    maze.append(list(input()))

bfs(0,0)

print(maze[height-1][width-1])
