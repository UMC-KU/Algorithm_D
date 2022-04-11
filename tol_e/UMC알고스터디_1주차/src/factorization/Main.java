package factorization;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		if(n == 1)	return;
		
		while(true) {
			int root = (int)Math.sqrt(n);
			int i = 2;
			for(; i<=root; i++) {
				if(n%i == 0) {
					n /= i;
					bw.write((i--)+"\n");
					break;
				}
			}
			if(i == root+1) break;
		}
		bw.write(n+"\n");
		bw.flush();
	}
}
