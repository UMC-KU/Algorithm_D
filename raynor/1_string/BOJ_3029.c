#include <stdio.h>

int timetoSec(char*);

int main(){
    char currentTime[9];
    char throwTime[9];
    char waitTime[9];
    int waitsec;
    int h, m, s;

    // 시간입력 및 예외처리 (이렇게 하는게 맞아...?)
    scanf("%s", currentTime);
    if(atoi(currentTime)>=24 || atoi(currentTime)<0 || atoi(currentTime+3)<0 || atoi(currentTime+3) >= 60
        || atoi(currentTime+6)<0 || atoi(currentTime+6) >= 60){
            return 0;
        }

    scanf("%s", throwTime);
    if(atoi(throwTime)>=24 || atoi(throwTime)<0
        || atoi(throwTime+3)<0 || atoi(throwTime+3) >= 60 || atoi(throwTime+6)<0 || atoi(throwTime+6) >= 60){
            return 0;
        }

    // 기다려야 하는 시간을 초 단위로 환산
    waitsec = timetoSec(throwTime) - timetoSec(currentTime);
    if(waitsec<=0){
        waitsec += 60*60*24;
    }
    // 기다려야 하는 시간(초)을 문자열로 출력하기 위해 시간, 분, 초 단위로 변환
    h = waitsec/3600;
    m = waitsec/60%60;
    s = waitsec-3600*h-60*m;

    sprintf(waitTime, "%02d:%02d:%02d", h,m,s); // 문자열 변환

    printf("%s", waitTime); // 출력
    
}

int timetoSec(char* time){
    int h, m, s;

    h = atoi(time);
    m = atoi(time+3);
    s = atoi(time+6);

    return (h*60*60 + m*60 + s);
}