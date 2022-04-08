#include <stdio.h>
#include <stdlib.h>

int main(){
    unsigned int N, K;

    scanf("%d", &N);
    scanf("%d", &K);

    if(K>N || N>1000){
        return 0;
    }

    int* Narr = (int*)calloc(N+1,sizeof(int));
    for(int i=2; i<=N; i++){
        for(int j=i; j<=N; j+=i){
            if(Narr[j]==0){         // flagging이 되어 있지 않을 때
                Narr[j] = 1;        // 1로 flagging 하고 카운트 감소
                K--;
            }
            if(K==0){
                printf("%d", j);     // 카운트가 다 닳았을 때 출력하고 return
                return 0;
            }
        }
    }
    free(Narr);
}