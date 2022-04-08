#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct sentence{
    char* str;      // 암호 한 줄
    int length;
    char most;     // 가장 많이 나타난 문자
    struct sentence *next, *prev;       // doubly linked list
}STC;

STC *tail, *head;
char password[256];   // 문자열 입력버퍼

// linked list 초기화
void init_STC(){
    head = (STC*)malloc(sizeof(STC));
    tail = (STC*)malloc(sizeof(STC));

    head -> next = tail;
    head -> prev = head;
    tail -> next = tail;
    tail -> prev = head;
}

// 최대 255글자 입력버퍼로 받은 문자열의 실제 길이만큼만 정확하게 동적할당하여 저장
void addSentence(int length){
    STC* newpw = (STC*)malloc(sizeof(STC));
    int* charCnt = (int*)calloc(26,sizeof(int));    // most를 판별하기 위한 배열 (a~z에 해당하는 count를 각각 가지고 있다.)
    int max = 0;        // 최대 카운트(temp)
    int k = 0;
    newpw -> length = length;
    newpw -> str = (char*)malloc(length*sizeof(char));  // 암호 한줄 메모리 동적할당
    for(int i=0; i<length; i++){
        if((password[i] > 122 || password[i] < 97) && password[i] != 32){
            exit(1);
        }
        newpw->str[i] = password[i];        // 입력버퍼에 있는 암호를 실제 데이터에 그대로 옮기기
    }
    for (int i=0; i<length; i++){
        if((newpw->str)[i]<=122 && (newpw->str)[i]>=97){    // 띄어쓰기 제외 알파벳 소문자에 대하여
            if(++charCnt[((newpw->str)[i]-97)] > max){      // (newpw->str)[i]-97 : 알파벳 -> 인덱스 변환 (a:0 ~z:25)
                max = charCnt[((newpw->str)[i]-97)];        // 알파벳을 한번 count 하고 최대 등장수를 초과했으면 most로 갱신
                newpw->most = (newpw->str)[i];
            }
            else if(charCnt[((newpw->str)[i]-97)] == max){  // 최대 등장수가 동일하면 most를 ?로 갱신
                newpw->most = '?';
            }
        }
    }
    if(max == 0){
        exit(1);
    }


    // linked list 끼워넣기
    head->next->prev = newpw;
    newpw->prev = head;
    newpw->next = head->next;
    head->next = newpw;
}

void printMost(){
    STC* current = tail->prev;
    while(current != head){
        printf("%c\n", current->most);
        current = current->prev;
    }
    
}

int main(){
    init_STC();
    int T;

    // T 입력 및 예외처리
    scanf("%d", &T);
    if(T<1 || T>20){
        return 0;
    }
    getchar();
    for(int i=0; i<T; i++){
        gets(password);
        if(strlen(password)<1 || strlen(password)>256){
            return 0;
        }
        addSentence(strlen(password));
    }

    printMost();
}