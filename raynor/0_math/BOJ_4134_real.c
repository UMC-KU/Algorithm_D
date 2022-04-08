#include <stdio.h>
#include <stdlib.h>
#include <math.h>

unsigned int findDicimal(unsigned int);

int main(){
    int n;

    scanf("%d", &n);

    unsigned int* numArr = (unsigned int*)malloc(n*sizeof(unsigned int));
    for(int i=0; i<n; i++){
        scanf("%u", &numArr[i]);
        if(numArr[i]<0 || numArr[i]>4000000000){
            return 0;
        }   
    }

    for(int i=0; i<n; i++){
        printf("%u\n",findDicimal(numArr[i]));
    }
    free(numArr);
}

unsigned int findDicimal(unsigned int num){
    if(num == 0 || num == 1){
        return 2;
    } else if((num & 1 )== 0){
        return findDicimal(num+1);
    }

    for(unsigned int i=2; i*i<num; i++){
        if(num%i==0){
            return (findDicimal(num+2));
        } else {
            continue;
        }
    }
    return num;
}