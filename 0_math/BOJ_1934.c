#include <stdio.h>
#include <stdlib.h>

int findGCD(int, int);

int main(){
    signed int T;
    
    scanf("%d", &T);    // 시행횟수 입력
    if(T>1000){
        return 0;
    }

    // 시행횟수를 기반으로 입력받을 숫자 이차원배열 동적할당
    int** numArr = (int**)malloc(T*sizeof(int*));
    for(int i=0; i<T; i++){
        numArr[i] = (int*)malloc(2*sizeof(int));
        for(int j=0; j<2; j++){
            scanf("%d", &numArr[i][j]);
        }
    }

    // 최대공약수를 찾는 함수를 바탕으로 최소공배수 생성, 출력
    for(int i=0; i<T; i++){
        int lcm = (numArr[i][0])*(numArr[i][1])/findGCD(numArr[i][0], numArr[i][1]);
        printf("%d\n", lcm);
    }
    
}


int findGCD(int a, int b){
    if(b==0) {
        return a;
    }
    return findGCD(b, a%b);    // recursion (최대공약수 구하기)
}