// Baekjoon No. 15486 - 퇴사 2
// 
#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);

    int i, j, n, max_profit = 0;
    scanf("%d", &n);
    vector<vector<int>> arr(2, vector<int>(n, 0));  // 일정 저장하는 배열
    vector<int> result(n, 0);   // 결과 저장하는 배열

    // 둘째 줄 이하
    for(i = 0; i < n; i++){
        scanf(" %d %d", &arr[0][i], &arr[1][i]);
    }

    // DP
    for(i = 0; i < n; i++){
        if(arr[0][i] + i <= n && result[arr[0][i] + i - 1] < arr[1][i] + result[i]){       // 7일차 넘지 않을때까지만
            result[arr[0][i] + i - 1] = arr[1][i] + result[i];
        }
    }    

    // 최대 수익 선정 부분
    for(i = 0; i < n+1; i++)
        if(result[i] > max_profit)
            max_profit = result[i];
    // 출력 부분
    printf("%d\n", max_profit);
    for(i = 0; i < n; i++)
        printf("%d ", result[i]);

    return 0;
}