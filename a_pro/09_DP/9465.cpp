// Baekjoon 9465 ��ƼĿ / 220730 solved
// 2*n �迭���� �� ĭ�� ���� �ٷ� �´���ִ� ĭ�� ������ ��� ĭ�� ������ �� ������,
// �׷��� ������ ĭ���� �ִ��� ���ϱ�
#include <iostream>
#include <algorithm>
#define MAX 100000
#define ROWS 2
using namespace std;

int main(){
    int t, n, tmp;
    int stickers[ROWS][MAX] = {0};
    
    // �Է�
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

        // �׽�Ʈ ���̽����� ��ƼĿ ���� �ִ� ���
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