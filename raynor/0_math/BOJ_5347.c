#include <stdio.h>
#include <stdlib.h>

int findGCD(int, int);

int main(){
    unsigned int n;

    scanf("%d", &n);

    int** numArr = (int**)malloc(n*sizeof(int*));
    for(int i=0; i<n; i++){
        numArr[i] = (unsigned int*)malloc(2*sizeof(unsigned int));
        for(int j=0; j<2; j++){
            scanf("%u", *(numArr+i)+j);
            if(numArr[i][j]>1000000 || numArr[i][j]<1){
                return 0;
            }
        }
    }

    for(int i=0; i<n; i++){
        unsigned long long ab = (numArr[i][0])*(numArr[i][1]);
        printf("gcd : %d\n", findGCD(numArr[i][0], numArr[i][1]));  // 디버깅 위해서 써놓은 부분인데 이상한점
        printf("ab : %llu\n", ab);                                  // 46000~47000사이 부근의 숫자를 입력하면 곱연산이 제대로 수행되지 않음
        printf("%llu\n", ab/findGCD(numArr[i][0], numArr[i][1]));
    }

    for(int i=0; i<n; i++){
        free(*(numArr+i));
    }
    free(numArr);
}

int findGCD(int a, int b){
    if(b==0){
        return a;
    }
    return findGCD(b, a%b);
}