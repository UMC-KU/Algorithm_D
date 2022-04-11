package coprime_Num;
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
		String[] num = br.readLine().split(" ");
		double sum = 0;
		double count = 0;
		int x = Integer.parseInt(br.readLine());
		while(n>0) {
			int a = Integer.parseInt(num[num.length - (n--)]);
			if(((a>x)?HCF(a,x):HCF(x,a)) == 1) {
				sum += a;
				count++;
			}
		}
		bw.write(sum/count+"\n");
		bw.flush();
	}
}
