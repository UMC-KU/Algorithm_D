package eratosthenes_Prime;

import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String[] str = br.readLine().split(" ");
		int n = Integer.parseInt(str[0]);
		int k = Integer.parseInt(str[1]);
		int count = 0;
		int[] num = new int[n + 1];	//탐색된 수 표시
		
		for (int i = 2; i <= n; i++) {	//2~n까지
			if (num[i] == 0) {
				int j = 1;
				while (i * j <= n && count < k) {	//선택된 수의 배수 탐색
					if (num[i * j] == 0) {
						num[i * j] = 1;
						count++;
					}
					j++;
				}
				if (count == k) {
					bw.write((i * (--j)) + "");
					break;
				}
			}
		}
		bw.flush();
	}
}
