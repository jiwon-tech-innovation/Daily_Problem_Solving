import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 늘리기

def p(x, y):
    if x < 0 or x >= noodle or y < 0 or y >= noodle or arr[y][x] == '0':
        return 0

    arr[y][x] = '0' # 방문 처리
    cnt = 1 # 현재 내 위치
    
    # 4. 상하좌우에서 찾아온 집의 개수를 모두 더함
    cnt += p(x + 1, y)
    cnt += p(x - 1, y)
    cnt += p(x, y + 1)
    cnt += p(x, y - 1)
    
    return cnt

arr = [] # 정사각형 크기 
result = [] #단지 갯수
noodle = int(input())
for i in range(noodle):
    arr.append(list(input()))

for y in range(noodle):
    for x in range(noodle):
        if arr[y][x] == '1':
            # 여기서 탐색(BFS/DFS) 시작!
            result.append(p(x, y))

print(len(result))
result.sort()
for i in result:
    print(i)