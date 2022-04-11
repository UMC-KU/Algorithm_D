package lowestCommonFactor_2;
import java.io.*;

public class Main {
	public static int HCF(int n1, int n2) {
		if(n2 == 0) return n1;
		else return HCF(n2, n1%n2);
	}

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		while((n--)>0) {
			String[] str = br.readLine().split(" ");
			int a = Integer.parseInt(str[0]);
			int b = Integer.parseInt(str[1]);
			
			int hcf = (a>b)?HCF(a, b):HCF(b,a);
			int lcm = a*b/hcf;
			bw.write(lcm+"\n");
		}
		bw.flush();
	}
}
