// Baekjoon No. 21317 ¡�˴ٸ� �ǳʱ� - 220819~ 220820
// Time Complexity O(n)
// ���� 15486, 2156���� ���̵�� ����.
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
        // dp�� dp. memory[]���� larger_jump�� �� �� ���鸸 ����. �� �� ������ ������ memory_jumped[]�� �����ؼ� �ű⼭ small_jump, large_jump�� �����Ŵ.
        // memory[] -> memory[]�� ���� / memory_jumped[] -> memory[], memory_jumped ��� ����.
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
        printf("%d", memory[n-1]);  // point!! memory_jumped [0]~ [2]�� �ʱ�ȭ���� �ʴ´ٴ� ���� ������.
    return 0;
}