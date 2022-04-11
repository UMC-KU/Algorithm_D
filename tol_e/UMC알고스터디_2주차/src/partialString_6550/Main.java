package partialString_6550;

import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String ans = "";
		while(sc.hasNextLine()) {
			String[] str = sc.nextLine().split(" ");
			String s = str[0];
			String t = str[1];
			int len = 0;
			for(int i = 0; i<t.length(); i++) {
				if(t.charAt(i) == s.charAt(len)) {
					len++;
				}
				if(len == s.length()) {
					ans += "Yes\n";
					break;
				}
			}
			if(len != s.length())
				ans+="No\n";
		}
		System.out.println(ans);
	}
}
