#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// 입력받은 문자열을 한줄 단위로 저장하는 구조체
typedef struct sentence{
    char* str;      // 암호 한 줄
    int length;     // 한줄 짜리 암호의 길이
    struct sentence *next, *prev;       // doubly linked list
}STC;

STC *tail, *head;
char password[501];   // 문자열 입력버퍼

// linked list 초기화
void init_STC(){
    head = (STC*)malloc(sizeof(STC));
    tail = (STC*)malloc(sizeof(STC));
    tail->str = "END";

    head -> next = tail;
    head -> prev = head;
    tail -> next = tail;
    tail -> prev = head;
}

// 최대 500글자 입력버퍼로 받은 문자열의 실제 길이만큼만 정확하게 동적할당하여 저장
void addSentence(int length){
    STC* newpw = (STC*)malloc(sizeof(STC));
    newpw -> length = length;
    newpw -> str = (char*)malloc(length*sizeof(char));  // 암호 한줄 메모리 동적할당
    for(int i=0; i<length; i++){
        newpw->str[i] = password[i];        // 입력버퍼에 있는 암호를 실제 데이터에 그대로 옮기기
    }

    // linked list 끼워넣기
    head->next->prev = newpw;
    newpw->prev = head;
    newpw->next = head->next;
    head->next = newpw;
}

// 암호 해독
void printSentence(){
    STC* current = tail->prev;

    // queue 형식으로 저장되었기 때문에 가장 뒤쪽(tail)의 암호부터 해독
    while(current != head){
        for(int i=(current->length - 1); i>=0; i--){
            printf("%c", (current->str)[i]);    // 문자열 뒤부터 순서대로 출력
        }
        printf("\n");
        current = current->prev;        // linked list 다음 암호로 이동
    }
}

int main(){
    int count = 0;
    init_STC();

    while(1){
        // 암호 입력(문자열 한줄단위)
        gets(password);

        // END 입력되면 while문 종료
        if(strcmp(password, "END")==0){
            break;
        } else {    // 아니면 구조체에 암호 데이터 저장
            addSentence(strlen(password));
        }
    }
    // 암호해독
    printSentence();
}