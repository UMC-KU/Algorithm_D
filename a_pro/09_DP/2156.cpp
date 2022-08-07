// Baekjoon No. 2156 ������ �ý� 220801~ 220807
#include <iostream>
#include <vector>
using namespace std;

int main(){
    int n, i;
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
    if(n > 3)
        arr[3] = max(wines[3] + wines[2] + wines[0], wines[3] + arr[1]);
    // wines[i] + wines[i-1] + arr[i-3], wines[i] + wines[i-1] + arr[i-4], wines[i] + arr[i-2] �̷��� 3�� Ȯ���ؾ���.
    // 5 5 1 1 5 5 ���� �ݷ� ����.
    for(i = 4; i < n; i++){
        arr[i] = max(max(wines[i] + wines[i-1] + arr[i-3], wines[i] + arr[i-2]), wines[i] + wines[i-1] + arr[i-4]);
    }

    if(n > 1)
        printf("%d", max(arr[n-2], arr[n-1]));
    else
        printf("%d", arr[0]);
    return 0;
}