#include <stdio.h>
#include <stdlib.h>

int main(){
    unsigned int M, N;
    int sum;
    int min = -1;

    scanf("%d", &M);
    scanf("%d", &N);

    int* maxNum = (int*)calloc(N+1,sizeof(int));    // 입력받은 수 중 큰 숫자만큼의 배열 동적할당
    maxNum[1] = 1;  // 1은 소수가 아니므로 예외 flagging

    if(M>N || M>10000 || N>10000){
        return 0;
    }

    for(int i=2; i<=N; i++){
        for(int j=i<<1; j<=N; j+=i){    // 에라토스테네스의 체
            maxNum[j] = 1;              // -> 큰 숫자에 대하여 2부터 N까지 에라토스테네스의 체 실행 한 뒤
        }                               //    소수가 아닌 경우에만 해당 배열의 값을 1로 flagging
    }

    for(int i=M; i<=N; i++){        // 에라토스테네스의 체로 모든 수를 flagging 한 후 M부터 N까지만 뽑아서 사용
        if(maxNum[i]==0){           // 배열의 값이 0이면 소수라는 뜻
            if(min == -1){          
                min = i;            // 소수가 존재하지 않을 시 -1을 출력하기 위한 초기화 작업
                sum = 0;
            }
            sum = sum + i;          // 소수들만 덧셈
        }
    }

    if(min == -1){
        printf("%d", min);
    } else {
        printf("%d\n", sum);
        printf("%d", min);
    }

    free(maxNum);
}