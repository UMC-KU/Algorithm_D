// Baekjoon No. 21317 징검다리 건너기 - 220819~ 220820
// Time Complexity O(n)
// 백준 15486, 2156에서 아이디어 얻음.
#include <iostream>
#include <vector>
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    int n, k, jump_using_val = -1;
    int i;
    scanf("%d", &n);
    vector<vector<int>> energy(n, vector<int>(2, 0));
    vector<int> memory(n, 0);
    vector<int> memory_jumped(n, 0);
    for(i = 0; i < n-1; i++)
        scanf(" %d %d", &energy[i][0], &energy[i][1]);
    scanf(" %d", &k);

    // solving
    memory[0] = 0;
    if(n > 1)
        memory[1] = memory[0] + energy[0][0];
    if(n > 2)
        memory[2] = min(memory[1] + energy[1][0], memory[0] + energy[0][1]);
    for(i = 3; i < n; i++){
        memory[i] = min(memory[i-1] + energy[i-1][0], memory[i-2] + energy[i-2][1]);
        // dp의 dp. memory[]에는 larger_jump가 안 된 값들만 저장. 한 번 점프한 값들은 memory_jumped[]에 저장해서 거기서 small_jump, large_jump만 시행시킴.
        // memory[] -> memory[]만 참조 / memory_jumped[] -> memory[], memory_jumped 모두 참조.
        if(i > 4)
            memory_jumped[i] = min(min(memory_jumped[i-1] + energy[i-1][0], memory_jumped[i-2] + energy[i-2][1]), memory[i-3] + k);
        else if(i == 4)
            memory_jumped[i] = min(memory_jumped[i-1] + energy[i-1][0], memory[i-3] + k);
        else if(i == 3)
            memory_jumped[i] = memory[i-3] + k;
    }
    
    if(n > 3)
        printf("%d", min(memory[n-1], memory_jumped[n-1]));
    else
        printf("%d", memory[n-1]);  // point!! memory_jumped [0]~ [2]는 초기화되지 않는다는 것을 간과함.
    return 0;
}