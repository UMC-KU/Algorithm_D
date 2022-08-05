// Baekjoon No. 11600 구간 합 구하기 5 / 220731~
// DP 문제
// Time Complexity 최대 O(n^2)
#include <iostream>
using namespace std;
int main(){
    int n, m, i, j, sum = 0;
    scanf("%d %d", &n, &m);
    getchar();
    
    int** board = new int*[n];
    for(i = 0; i < n; i++)
        board[i] = new int[n]{0};
    int** coordinates = new int*[m];
    for(i = 0; i < m; i++)
        coordinates[i] = new int[4]{0};
    // board 입력받음
    for(i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            scanf("%d", &board[i][j]);
            getchar();
        }
    }
    for(i = 0; i < m; i++){
        for(j = 0; j < 4; j++){
            scanf("%d", &coordinates[i][j]);
            getchar();
        }
    }

    // 합 구함
    for(int case_num = 0; case_num < m; case_num++){
        sum = 0;
        for(i = coordinates[case_num][0]; i <= coordinates[case_num][2]; i++){
            for(j = coordinates[case_num][1]; j <= coordinates[case_num][3]; j++){
                sum += board[i-1][j-1];
            }
        }
        printf("%d\n", sum);
    }

    for(i = 0; i < n; i++)
        delete[] board[i];
    delete[] board;
    for(i = 0; i < m; i++)
        delete[] coordinates[i];
    delete[] coordinates;
    return 0;
}