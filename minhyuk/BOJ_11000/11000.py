import heapq
n = int(input())
lecture = []

for i in range(n):
    lecture.append(tuple(map(int, input().split())))
lecture.sort()

result = []
heapq.heappush(result, lecture[0][1])

for i in range(1,n):
    if lecture[i][0] >= result[0]:
        heapq.heappop(result)
    
    heapq.heappush(result, lecture[i][1])

print(len(result))