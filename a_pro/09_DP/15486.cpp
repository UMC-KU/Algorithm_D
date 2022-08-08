// Baekjoon No. 15486 - 퇴사 2
// Time Complexity O(n)
// 220731~ 220808 Solved!
#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);

    int i, j, n, max_profit = 0, max_res = 0;
    scanf("%d", &n);
    vector<vector<int>> arr(2, vector<int>(n, 0));  // 일정 저장하는 배열
    vector<int> result(n, 0);   // 결과 저장하는 배열

    // 둘째 줄 이하 입력
    for(i = 0; i < n; i++){
        scanf(" %d %d", &arr[0][i], &arr[1][i]);
    }

    // DP
    for(i = 0; i < n; i++){
        // max_res 사용하면 꼭 result[i]가 아닌 이제까지의 최대값 더해주므로
        // 중간에 하루 이상 쉬고 상담하는 경우까지 커버 가능.
        if(arr[0][i] + i <= n && result[arr[0][i] + i - 1] < arr[1][i] + max_res){       // 7일차 넘지 않을때까지만
            result[arr[0][i] + i - 1] = arr[1][i] + max_res;
        }
        // i == 0일때는 어차피 result[0] == 0이므로 max_res if문 다음에 정해줘도 상관없음
        // 현재까지의 최대 결과를 저장.
        max_res = (result[i] > max_res) ? result[i] : max_res;
    }    

    // 최대 수익 선정 부분
    for(i = 0; i < n; i++)
        if(result[i] > max_profit)
            max_profit = result[i];
    // 출력 부분
    printf("%d", max_profit);

    // printf("\nresults\n");
    // for(i = 0; i < n; i++)
    //     printf("%d ", result[i]);
    return 0;
}