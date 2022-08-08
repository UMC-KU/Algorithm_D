// Baekjoon No. 11600 ���� �� ���ϱ� 5 / 220731~ 220808
// DP ����
// Time Complexity O(n)
#include <iostream>
#include <vector>
using namespace std;
int main(){
    ios::sync_with_stdio(false);

    int n, m, i, j, sum = 0, tmp;
    int x1, x2, y1, y2;
    scanf("%d %d", &n, &m);
    
    vector<vector<int>> board(n, vector<int>(n, 0));
    vector<vector<int>> coordinates(m, vector<int>(4, 0));
    
    // board �Է¹���
    for(i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            if(j == 0)
                scanf(" %d", &board[i][j]);
            else{
                scanf(" %d", &tmp);
                board[i][j] = board[i][j-1] + tmp;
            }
        }
    }
    // coordinates �Է�
    for(i = 0; i < m; i++){
        for(j = 0; j < 4; j++){
            scanf(" %d", &coordinates[i][j]);
        }
    }

    // �� ����
    for(int case_num = 0; case_num < m; case_num++){
        sum = 0;
        // x�� ��, y�� ����. ���������� (x, y)�� x�� y��. �ݴ�.
        y1 = coordinates[case_num][0] - 1;
        x1 = coordinates[case_num][1] - 1;
        y2 = coordinates[case_num][2] - 1;
        x2 = coordinates[case_num][3] - 1;

        if(x1 == 0)
            for(i = y1; i <= y2; i++)
                sum += board[i][x2];
        else
            for(i = y1; i <= y2; i++)
                sum += board[i][x2] - board[i][x1 - 1];
        printf("%d\n", sum);
    }
    return 0;
}