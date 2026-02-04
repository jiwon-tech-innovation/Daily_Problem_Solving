import sys
input = sys.stdin.readline

mul_mat = []

mat_A = []
mat_A_row, mat_A_column = map(int, input().split())

for i in range(mat_A_row):
    mat_A.append(list(map(int, input().split())))

mat_B = []
mat_B_row, mat_B_column = map(int, input().split())

for i in range(mat_B_row):
    mat_B.append(list(map(int, input().split())))

for i in range(mat_A_row):
    temp = []
    for j in range(mat_B_column):
        temp_item = 0
        for k in range(mat_A_column):
            temp_item += mat_A[i][k] * mat_B[k][j]
        temp.append(temp_item)
    mul_mat.append(temp)

for row in mul_mat:
    for item in row:
        print(item, end=" ")
    print()