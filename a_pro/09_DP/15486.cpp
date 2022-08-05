#include <iostream>
#define ROWS 2
using namespace std;
void print_arr(int**, int*, int);

int main(){
    int** arr = new int*[2];
    
    int i, j, n, max_profit = 0;
    cin >> n;
    int* result = new int[n+1]{0};
    for(i = 0; i < ROWS; i++){
        arr[i] = new int[n+1]{0};
    }
    // 둘째 줄 이하
    for(i = 0; i < n; i++){
        cin >> arr[0][i] >> arr[1][i];
    }

    // DP
    for(i = 0; i < n; i++){
        if(arr[0][i] + i < n+1 && result[arr[0][i] + i] < arr[1][i] + result[i]){       // 7일차 넘지 않을때까지만
            result[arr[0][i] + i] = arr[1][i] + result[i];
        }
    }    

    print_arr(arr, result, n+1);
    // 최대 수익 선정 부분
    for(i = 0; i < n+1; i++)
        if(result[i] > max_profit)
            max_profit = result[i];

    cout << max_profit;


    for(i = 0; i < ROWS; i++){
        delete[] arr[i];
    }
    delete[] arr;
    delete[] result;
    return 0;
}

void print_arr(int** arr, int* result, int n){
    cout << endl << "arr 출력\n";/
    for(int i = 0; i < n; i++)
        printf("%3d ", i);
    cout << endl;
    for(int i = 0; i < ROWS; i++){
        for(int j = 0; j < n; j++){
            printf("%3d ", arr[i][j]);
        }
        cout << endl;
    }
    cout << endl << "result 출력\n";

    for(int i = 0; i < n; i++){
        printf("%3d ", result[i]);
    }
    cout << endl;
    return;
}