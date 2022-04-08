#include <stdio.h>

int N;
int count = 0;
int new = -1;

void recursionNum(int, int);

int main(){

    scanf("%d", &N);

    if(N>99 || N<0){
        return 0;
    }

    recursionNum(N/10, N%10);

    printf("%d", count);
}

void recursionNum(int a, int b){    // a : 10의 자리 숫자,   b : 1의 자리 숫자
    if(new == N){   // terminate condition (생성된 숫자와 기존의 숫자가 같을 때)
        return;
    }
    new = b*10 + (a+b)%10;  // 새로운 숫자 생성하는 식
    count++;    // 시행횟수 count
    recursionNum(b, (a+b)%10);  // recursion
}