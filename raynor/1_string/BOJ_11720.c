#include <stdio.h>
#include <stdlib.h>

int main(){
    int N;
    int sum = 0;
    int* arr;
    char* ch;

    // N입력 및 에러처리
    scanf("%d", &N);
    if(N<1 || N>100){
        return 0;
    }

    arr = (int*)malloc(N*sizeof(int));
    getchar();  // 입력버퍼 초기화 (N을 하나 입력받았기 때문에 그걸 지워줘야 함)

    for(int i=0; i<N; i++){
        ch = getchar();     // 문자 하나씩 입력 받자마자
        arr[i] = ch - '0';  // 아스키코드값사용, 정수로 변환해서 배열에 바로바로 저장
    }

    for (int i=0; i<N; i++){
        sum += arr[i];      // 저장된 배열 가지고 합연산
    }

    printf("%d", sum);      // 출력
}