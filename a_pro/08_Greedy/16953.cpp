#include <iostream>
using namespace std;
int main(){
    long long a, b;
    scanf("%lld %lld", &a, &b);
    // int *arr = new int[b+1] {0, };
    int arr[1000000000];
    arr[a] = 1;
    for(int i = a; i < b; i ++){
        if(arr[i] && i*2 <= b && (!arr[i*2] || arr[i*2] > arr[i] + 1))
            arr[i*2] = arr[i] + 1;
        if(arr[i] && i*10+1 <= b && (!arr[i*10+1] || arr[i*10+1] > arr[i]+1))
            arr[i*10+1] = arr[i] + 1;
    }

    if(arr[b])
        printf("%d", arr[b]);
    else
        printf("%d", -1);

    // delete[] arr;
    return 0;
}