package sum_GCD;
import java.io.*;

public class Main {
	
	public static int HCF(int n1, int n2) {
		if(n2 == 0) return n1;
		else return HCF(n2, n1%n2);
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		while((t--)>0) {
			String[] str = br.readLine().split(" ");
			long sum = 0;
			int n = Integer.parseInt(str[0]);
			for(int i = 1; i<n; i++) {
				int a = Integer.parseInt(str[i]);
				for(int j = i+1; j<=n; j++) {
					int b = Integer.parseInt(str[j]);
					sum+= (a>b)?HCF(a,b):HCF(b,a);
				}
			}
			bw.write(sum+"\n");
		}
		bw.flush();
	}
}
