#include <stdio.h>
#include <stdlib.h>

int findGCD(int, int);
void printCD(int);

int main(){
    int num;
    int* numArr;
    int gcd;    // 최대공약수

    scanf("%d", &num);  // 입력받을 숫자의 개수 입력 (2 or 3)
    numArr = (int*)malloc(num*sizeof(int)); // 그만큼 입력받을 자연수 배열 동적할당

    for(int i=0; i<num; i++){
        scanf("%d", numArr+i);      // 배열에 차례대로 자연수 입력받기
    }

    gcd = findGCD(numArr[0], numArr[1]);    // 먼저 두 숫자의 최대공약수를 구하고,
    for(int i=2; i<num; i++){               // numArr의 크기가 3 이상일 경우 최대 공약수와 그 다음수의 최대공약수를 구한다.
        gcd = findGCD(gcd, numArr[i]);      // 모든 숫자의 최대공약수를 구하는 효과
    }

    printCD(gcd);   // 최대공약수의 약수 차례대로 출력
    return 0;
}

int findGCD(int a, int b){
    if(b==0) {
        return a;
    }
    findGCD(b, a%b);    // recursion (최대공약수 구하기), 유클리드 호제법
}

void printCD(int gcd){
    for(int i=1; i<=gcd; i++){
        if(gcd%i == 0){
            printf("%d\n", i);  // i로 나누어 떨어질 때, 즉 gcd의 약수를 차례대로 출력
        }
    }
}