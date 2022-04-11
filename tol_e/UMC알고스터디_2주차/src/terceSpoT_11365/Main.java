package terceSpoT_11365;

import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String ans = "";
		while(true) {
			String str = sc.nextLine();
			if(str.equals("END")) break;
			for(int i = str.length()-1; i>=0; i--) {
				ans += str.charAt(i);
			}
			ans += "\n";
		}
		System.out.println(ans);
	}
}
