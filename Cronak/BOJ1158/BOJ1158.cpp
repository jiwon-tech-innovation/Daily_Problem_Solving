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
using namespace std;


int main() {
    int People = 0; //사람의 수 
    int KillNumber = 0; //죽일 사람의 번호

    queue<int> LivingPeople; //살아있는 사람들을 담은 큐
    queue<int> KilledPeople; //죽은 사람들을 담은 큐

    cin >> People >> KillNumber;

    for(int i = 1; i <= People; i++) {
        LivingPeople.push(i);
    }
    
    while(LivingPeople.size() > 1) {
        for(int i = 0; i < KillNumber - 1; i++) {
            LivingPeople.push(LivingPeople.front());
            LivingPeople.pop();
        }
        KilledPeople.push(LivingPeople.front());
        LivingPeople.pop();
    }
    KilledPeople.push(LivingPeople.front());
    LivingPeople.pop();

    //출력 부분
    //////////////////////////////////////////////////////////////////////////////// 
    cout << "<";

    while (!KilledPeople.empty()) {
        cout << KilledPeople.front(); 
        KilledPeople.pop(); 

        if (!KilledPeople.empty()) {
            cout << ", ";
        }
    }

    cout << ">";


    return 0;
}