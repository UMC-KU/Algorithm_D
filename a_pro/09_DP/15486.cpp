// Baekjoon No. 15486 - ��� 2
// Time Complexity O(n)
// 220731~ 220808 Solved!
#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);

    int i, j, n, max_profit = 0, max_res = 0;
    scanf("%d", &n);
    vector<vector<int>> arr(2, vector<int>(n, 0));  // ���� �����ϴ� �迭
    vector<int> result(n, 0);   // ��� �����ϴ� �迭

    // ��° �� ���� �Է�
    for(i = 0; i < n; i++){
        scanf(" %d %d", &arr[0][i], &arr[1][i]);
    }

    // DP
    for(i = 0; i < n; i++){
        // max_res ����ϸ� �� result[i]�� �ƴ� ���������� �ִ밪 �����ֹǷ�
        // �߰��� �Ϸ� �̻� ���� ����ϴ� ������ Ŀ�� ����.
        if(arr[0][i] + i <= n && result[arr[0][i] + i - 1] < arr[1][i] + max_res){       // 7���� ���� ������������
            result[arr[0][i] + i - 1] = arr[1][i] + max_res;
        }
        // i == 0�϶��� ������ result[0] == 0�̹Ƿ� max_res if�� ������ �����൵ �������
        // ��������� �ִ� ����� ����.
        max_res = (result[i] > max_res) ? result[i] : max_res;
    }    

    // �ִ� ���� ���� �κ�
    for(i = 0; i < n; i++)
        if(result[i] > max_profit)
            max_profit = result[i];
    // ��� �κ�
    printf("%d", max_profit);

    // printf("\nresults\n");
    // for(i = 0; i < n; i++)
    //     printf("%d ", result[i]);
    return 0;
}