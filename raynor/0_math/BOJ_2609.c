#include <stdio.h>

int findGCD(int, int);

int main(){

    unsigned int a, b;
    int gcd, lcm;

    scanf("%d", &a);
    scanf("%d", &b);

    if(a>10000 || b>10000){
        return 0;
    }

    gcd = findGCD(a,b);
    printf("%d\n", gcd);
    printf("%d", a*b/gcd);  // 최소공배수는 두수의 곱 나누기 최대공약수
}

int findGCD(int a, int b){
    if(b==0) {
        return a;
    }
    return findGCD(b, a%b);    // recursion (최대공약수 구하기)
}