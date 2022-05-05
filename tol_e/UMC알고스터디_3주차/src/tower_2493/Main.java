package tower_2493;

import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		String[] str = br.readLine().split(" ");
		int[] stack = new int[n];	//해당 탑의 신호를 받는 탑의 인덱스
		int[] tower = new int[n];	//해당 탑의 높이 
		int index = -1;				//조회하는 인덱스
		for(int i = 0; i<n; i++) {
			int num = Integer.parseInt(str[i]);	//신호를 보내는 탑의 높이
			while(index >= 0) {		
				if(num > tower[index]) {	//탑의 높이가 조회 중인 탑의 높이보다 크면
					index = stack[index];	//조회한 탑의 신호를 받는 탑을 조회
				} else {					//보다 작거나 같으면 신호를 받는 것이므로
					break;					//인덱스를 저장한 채로 루프문 탈출
				}
			}
			bw.write((index+1)+" ");		//조회한 인덱스에 1을 더한 값을 출력 -> 위치
			stack[i] = index;				//신호를 받는 탑의 인덱스
			tower[i] = num;					//신호를 보내는 탑의 높이 순차적으로 저장
			index = i;						//인덱스 수정
		}
		bw.flush();
		bw.close();
	}
}
