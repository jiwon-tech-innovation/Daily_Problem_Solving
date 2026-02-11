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
#include <stack>
#include <queue>
#include <list>
using namespace std;




int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int TestCase = 0; //테스트 케이스
    int Number = 0; //확인할 케이스


    cin >> TestCase;

    for(int i = 0; i < TestCase; i++) {
        int Count = 0; //0갯수 카운터
        cin >> Number;
        for(int Base = 2; Base <= Number; Base++) {
            int Temp = Number;
            while(Temp%Base == 0) {
                Count++;
                Temp = Temp / Base;
            }
        }
        cout << Count << "\n";
    }

    return 0;
}