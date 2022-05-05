/* 
 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다
카드 장수 N이 주어졌을 때, 제일 마지막에 남게 되는 카드
 */
package card2_2164;
import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		
		Queue<Integer> q = new LinkedList<Integer>();
		for(int i = 0; i<n; i++) {
			q.add(i+1);		//1~n을 순서대로 큐에 삽입	(시작=1 / 끝=n)
		}
		while(q.size() > 1) {//한 장 남을 때까지 반복
			q.poll();		//첫장 버리기
			q.add(q.poll());//그 다음 첫장 마지막으로 옮기기
		}
		bw.write(q.peek()+"");	//마지막 장 출력
		bw.flush();
		bw.close();
		br.close();
	}
}
