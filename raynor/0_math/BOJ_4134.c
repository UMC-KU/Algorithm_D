#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void eratosthenesSieve(int);
int findDicimal(int, int);
int* deviderArr;

int main(){
    int n;

    scanf("%d", &n);
    if(n<0 || n>40*pow(10, 9)){
        return 0;
    }

    int* numArr = (int*)malloc(n*sizeof(int));
    for(int i=0; i<n; i++){
        scanf("%d", &numArr[i]);
    }

    for(int i=0; i<n; i++){
        eratosthenesSieve(numArr[i]);
        printf("%d\n",findDicimal(numArr[i], numArr[i]));
        free(deviderArr);
    }
}

int findDicimal(int num, int trial){
    if(num == 0 || num == 1){
        return 2;
    } else if((num & 1 )== 0){
        return findDicimal(num+1, trial);
    }

    for(int i=0; i<(trial); i++){
        if(deviderArr[i] == 0 && (num%(i+1)) == 0){
            return (findDicimal(num+2, trial));
        } else {
            continue;
        }
    }
    return num;
}

void eratosthenesSieve(int n){
    deviderArr = (int*)calloc(n, sizeof(int));
    deviderArr[0] = 1;
    for(int i=2; i<n; i++){
        for(int j=i<<1; j<n; j+=i){
            deviderArr[j-1] = 1;
        }
    }
}