package next_Prime;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int t = Integer.parseInt(br.readLine());
		while((t--)>0) {
			Long n = Long.parseLong(br.readLine());
			while(!checkPrime(n++));
			bw.write((n-1)+"\n");
		}
		bw.flush();
	}
	
	public static boolean checkPrime(long n) {
		if(n<=1) return false;
		for(int i = 2; i<=(int)Math.sqrt(n); i++) {
			if(n%i == 0) return false;
		}
		return true;
	}
}
