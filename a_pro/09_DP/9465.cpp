// Baekjoon 9465 스티커 / 220730 solved
// 2*n 배열에서 각 칸은 서로 바로 맞닿아있는 칸을 제외한 모든 칸을 선택할 수 있을때,
// 그렇게 선택한 칸들의 최대합 구하기
#include <iostream>
#include <algorithm>
#define MAX 100000
#define ROWS 2
using namespace std;

int main(){
    int t, n, tmp;
    int stickers[ROWS][MAX] = {0};
    
    // 입력
    scanf("%d", &t);
    getchar();
    for(int test_case = 0; test_case < t; test_case++){
        scanf("%d", &n);
        getchar();
        for(int i = 0; i < ROWS; i++){
            for(int j = 0; j < n; j++){
                scanf("%d", &stickers[i][j]);
                getchar();
            }
        }

        // 테스트 케이스마다 스티커 점수 최댓값 출력
        for(int j = 0; j < n; j++){
            for(int i = 0; i < ROWS; i++){
                if(j == 1){
                    stickers[i][j] = stickers[i][j] + stickers[1 - i][0];
                }else if(j > 1){
                    stickers[i][j] = stickers[i][j] + max(stickers[1-i][j-1], stickers[1-i][j-2]);
                }
            }
        }
        printf("%d\n", max(stickers[0][n-1], stickers[1][n-1]));
    }
    return 0;
}