// Baekjoon No. 2156 ������ �ý� 220801~
#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n, i, j;
    scanf("%d", &n);
    vector<int>wines(n, 0);
    vector<int>arr(n, 0);
    for(i = 0; i < n; i++)
        scanf(" %d", &wines[i]);
    
    // �ʱ갪�� ���� ����
    arr[0] = wines[0];
    if(n > 1)
        arr[1] = wines[0] + wines[1];
    if(n > 2)
        arr[2] = max(wines[0], wines[1]) + wines[2];
    for(i = 3; i < n; i++){
        arr[i] = max(max(arr[i-3] + wines[i-1] + wines[i], arr[i-2] + wines[i]), arr[i-1]);
    }

    if(n > 1)
        printf("%d", arr[n-1]);  // �������� arr[i-3], arr[i-2]�� Ȯ���ϰ� arr[i-1]�� Ȯ�� ���ϹǷ� �� �������� �ִ��� ���� x
    else
        printf("%d", arr[0]);   // index ���� ����
    return 0;
}
// 100 200 101 201 