#include <stdio.h>

int factorization(int);

int main(){
    unsigned int N;

    scanf("%d", &N);

    if(N>10000000){
        return 0;
    }
    factorization(N);
}

int factorization(int N){
    if(N==1){
        return 1;
    }
    for(int i=2; i<=N; i++){        // N을 나누어 떨어뜨리는 수를 찾는 과정(인수분해)
        if(N%i == 0){
            N = N/i;                // 인수를 찾으면 실제로 N을 나눈 뒤 인수 출력 후 break;
            printf("%d\n", i);
            break;
        }
    }
    return factorization(N);        // 나눠진 N에 대해 recursion
}