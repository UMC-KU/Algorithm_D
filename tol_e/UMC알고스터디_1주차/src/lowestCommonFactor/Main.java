package lowestCommonFactor;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		while((n--)>0) {
			String[] str = br.readLine().split(" ");
			int a = Integer.parseInt(str[0]);
			int b = Integer.parseInt(str[1]);
			
			int small = (a<b)?a:b;	//작은 수
			int big = (a>b)?a:b;	//큰 수
			int i = 0;				//큰 수의 배수
			while((big*(++i))%small!=0); //큰 수의 배수에서 작은 수의 배수가 나올때까지 탐색
			bw.write((big*i)+"\n");		
		}
		bw.flush();
	}
}
