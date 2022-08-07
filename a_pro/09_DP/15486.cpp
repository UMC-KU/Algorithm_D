// Baekjoon No. 15486 - ��� 2
// 
#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);

    int i, j, n, max_profit = 0;
    scanf("%d", &n);
    vector<vector<int>> arr(2, vector<int>(n, 0));  // ���� �����ϴ� �迭
    vector<int> result(n, 0);   // ��� �����ϴ� �迭

    // ��° �� ����
    for(i = 0; i < n; i++){
        scanf(" %d %d", &arr[0][i], &arr[1][i]);
    }

    // DP
    for(i = 0; i < n; i++){
        if(arr[0][i] + i <= n && result[arr[0][i] + i - 1] < arr[1][i] + result[i]){       // 7���� ���� ������������
            result[arr[0][i] + i - 1] = arr[1][i] + result[i];
        }
    }    

    // �ִ� ���� ���� �κ�
    for(i = 0; i < n+1; i++)
        if(result[i] > max_profit)
            max_profit = result[i];
    // ��� �κ�
    printf("%d\n", max_profit);
    for(i = 0; i < n; i++)
        printf("%d ", result[i]);

    return 0;
}