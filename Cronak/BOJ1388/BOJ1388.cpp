#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h> 
#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <cmath>
#include <iomanip>
#include <vector>
#include <array>
#include <queue>
#include <map>
using namespace std;

int main() {
    int N = 0; //바닥의 세로 크기
    int M = 0; //바닥의 가로 크기
    char Tile; //입력 받는 타일
    int Tiles[50][50] = { 0 }; //타일이 놓여있는지 여부 저장 배열 (0: 빈칸, 1: 타일 있음)
    int answer = 0; //타일 총 갯수

    cin >> N >> M;
    
    for(int i = 0; i < N; i++) {
        for(int j = 0; j < M; j++) {

            cin >> Tile;

            if(Tile == '-') {
                Tiles[i][j] = 1; // "-"면 1로 표시
                if(j == 0 || Tiles[i][j-1] != 1) { //전 타일이 "-"이 아니라면 이어진 것이 아니므로 타일 갯수 +1
                    answer++;
                }
            }
            else {
                Tiles[i][j] = 2;
                if(i == 0 || Tiles[i-1][j] != 2) {
                    answer++;
                }
            }
        }
    }
    
    cout << answer << endl;

    return 0;
}