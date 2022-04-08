#include <stdio.h>
#include <string.h>
#include <math.h>

int main(){
    char num[10];
    int sum = 0;
    int B;

    scanf("%s", &num);
    scanf("%d", &B);

    if(B > 36 || B < 2){
        return 0;
    }

    int length = strlen(num)/sizeof(char);

    for(int i = 0; i<length; i++){
        if(48 <= num[i] && num[i] <= 57){   // 1~9일 때 ASCII Code -> Integer
            num[i]-=48;
        }
        if(65 <= num[i] && num[i] <= 90){   // 'A'~'Z'일 때 ASCII Code -> Integer
            num[i]-=55;
        }
        sum = sum + num[i]*pow(B,(length-i-1)); // 정수에 B를 거듭곱해서 B진수로 변환, 합연산
    }
    printf("%d", sum);
}