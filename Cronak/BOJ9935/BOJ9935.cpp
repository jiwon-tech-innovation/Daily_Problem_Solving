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
using namespace std;


int main() {

    string str;
    string boom;
    string answer;

    cin >> str >> boom;

    for(int i = 0; i < str.length(); i++) {
        answer.push_back(str[i]);
        bool isBoom = true;
        if(answer.length() >= boom.length()) {
            for(int j = 0; j < boom.length(); j++) {
                if(answer[answer.length() - boom.length() + j] != boom[j]) {
                    isBoom = false;
                    break;
                }
            }
            if(isBoom) {
                for(int k = 0; k < boom.length(); k++) {
                    answer.pop_back();
                }
            }
        }

    }

    if(answer.length() > 0) {
        cout << answer;
    }
    else {
        cout << "FRULA";
    }


    return 0;
}