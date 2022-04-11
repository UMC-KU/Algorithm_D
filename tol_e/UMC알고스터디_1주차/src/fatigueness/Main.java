// -a+c> +b+0 
package fatigueness;

import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		int a = Integer.parseInt(str[0]);
		int b = Integer.parseInt(str[1]);
		int c = Integer.parseInt(str[2]);
		int m = Integer.parseInt(str[3]);
		
		int work = 0;
		int fatigue = 0;
		int time = 0;
		for(; time<24; time++) {
			if(fatigue > m-a) fatigue -= c;
			else if(fatigue > m) fatigue -= c;
			else if(fatigue < m) {
				fatigue += a;
				work += b;
			} 
			if(fatigue < 0) fatigue = 0;
		}
		System.out.println(work);
	}

}
