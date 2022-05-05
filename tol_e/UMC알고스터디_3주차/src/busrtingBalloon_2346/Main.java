package busrtingBalloon_2346;

import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		String[] str = br.readLine().split(" ");
		int[] arr = new int[n];	
		for(int i = 0; i<n; i++) arr[i] = Integer.parseInt(str[i]);
		
		int count = 0;	//터뜨린 개수
		int index = 0;	//현재 탐색중인 인덱스	(arr[index] == 0 -> 터짐)
		int jump = 0;	//건너뛴 풍선 수
		int num = 0;	//건너뛰어야 할 풍선 수
		while(count != n) { //터뜨린 개수가 풍선 수와 같으면 break
			if(index < 0) index = n-1;
			else if(index > n-1) index = 0;
			if(arr[index] != 0) { //탐색중인 풍선이 안터졌으면
				if(num == jump) {	//터뜨리기
					//System.out.print("HIT--->");
					num = arr[index];
					arr[index] = 0;	//해당 풍선 터뜨리기
					count++;	//터뜨린 풍선 개수 +1
					jump = 0;	//건너뛴 풍선 수 초기화
					bw.write((index+1)+" ");
				}
				if(num > 0) jump++;	//양수일 경우 오른쪽으로 점프
				else if(num < 0)jump--;	//음수는 왼쪽으로 점프
			}
			//System.out.println("loop="+(++loop)+" / arr[index]="+arr[index]+" / num="+num+" / index="+index+" / jump="+jump+" / count="+count);
			if(num > 0) index++;
			else if(num < 0)index--;
		}
		bw.flush();
		bw.close();
		br.close();
	}
}
