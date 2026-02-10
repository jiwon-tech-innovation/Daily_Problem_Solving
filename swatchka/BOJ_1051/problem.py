N, M = map(int, input().split())

square = []
for i in range(N):
    square.append(list(map(int, list(input()))))

max_size = min(N, M)

for s in range(max_size, 0, -1):
    find = False
    for i in range(N - s + 1):
        for j in range(M - s + 1):
            if square[i][j] == square[i][j+s-1] == square[i+s-1][j] == square[i+s-1][j+s-1]:
                print(s * s)
                find = True
                break
        if find:
            break
    if find:
        break
