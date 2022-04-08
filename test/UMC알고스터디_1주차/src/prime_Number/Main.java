package prime_Number;

import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int m = Integer.parseInt(br.readLine());
		int n = Integer.parseInt(br.readLine());
		
		int[] num = new int[10001];
		num[2] = 1;
		num[3] = 1;
		
		int root = 0;
		for(int i = m; i<=n; i++) {
			root = (int)Math.sqrt(i);
			for(int j = 2; j<=root; j++) {
				if(i%j == 0) break;
				if(j == root) num[i] = 1;
			}
		}
		
		int sum = 0;
		int lowest = 0;
		for(int i = m; i<=n; i++) {
			if(num[i] == 1) {
				if(lowest == 0) lowest = i;
				sum += i;
			}
		}
		if(lowest == 0)	bw.write("-1");
		else bw.write(sum+"\n"+lowest);
		bw.flush();
	}
}
