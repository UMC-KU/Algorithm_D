#include <stdio.h>

int inputABCM();
int A, M;
int B, C;

int main(){
    int work = 0;
    int fatigue = 0;

    if(inputABCM()){    // inputABCM 함수 내에서 validation check 리턴타입에 따라 전체 실행여부 판단
        for(int time = 1; time <= 24; time++){
            if(fatigue+A <= M){
                work += B;
                fatigue += A;
                } else {
                if(fatigue-C >= 0){
                    fatigue -= C;
                } else {
                    fatigue = 0;
                }
            }
        }
        printf("%d", work);
    }

}

int inputABCM(){
    scanf("%d", &A);
    scanf("%d", &B);
    scanf("%d", &C);
    scanf("%d", &M);

    if(A<1 || A>1000000 || B<1 || B>10000 || M<1 || M>1000000 || C<1 || C>10000){
        return 0;   
    }

    return 1;
}