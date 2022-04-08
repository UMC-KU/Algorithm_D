#include <stdio.h>
#include <stdlib.h>

int main(){
    int N;
    unsigned int* Narr;
    int count = 0;

    scanf("%d", &N);
    if(N>100 || N<1){
        return 0;
    }

    //  1~1000까지 숫자 중 모든 소수를 찾아놓고 입력받은 숫자가 해당 배열에 존재하는지 확인하는 알고리즘
    
    Narr = (unsigned int*)malloc(N*sizeof(unsigned int));
    int* maxNum = (int*)calloc(1001, sizeof(int));    // 입력받을 수 있는 최대치인 1000에 대한 모든 소수를 찾기위한 동적할당
    maxNum[0] = 1;
    maxNum[1] = 1;      // 0, 1 은 소수가 아니므로 예외 flagging

    for(int i=0; i<N; i++){
        scanf("%d", &Narr[i]);      // 수 입력받기, validation check && return
        if(Narr[i]>1000){
            return 0;
        }
    }

    for(int i=2; i<=1000; i++){
        for(int j=i<<1; j<=1000; j+=i){    // 에라토스테네스의 체
            maxNum[j] = 1;              // -> 큰 숫자에 대하여 2부터 1000까지 에라토스테네스의 체 실행 한 뒤
        }                               //    소수가 아닌 경우에만 해당 배열의 값을 1로 flagging
    }

    for(int i=0; i<N; i++){
        if(maxNum[Narr[i]]==0){         // 입력한 숫자의 값이 maxNum 배열에서 flagging 되었는지 확인 후 count
            count++;
        }
    }

    printf("%d", count);

    free(maxNum);
    free(Narr);
}