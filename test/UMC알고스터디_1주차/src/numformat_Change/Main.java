package numformat_Change;
import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException{
		Scanner sc = new Scanner(System.in);
		String n = sc.next();
		int b = sc.nextInt();
		int dec = 0;
		for(int i = n.length()-1; i>=0; i--) {
			char a = n.charAt(i);
			int k = n.length()-1 - i;
			if(a<='9') {
				dec += (a-'0')*Math.pow(b, k);
			} else {
				dec += (a-'A'+10)*Math.pow(b, k);
			}
		}
		System.out.println(dec);
	}
}
