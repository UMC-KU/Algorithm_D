package haveLessFriend_16171;

import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String s = scan.nextLine();
		String k = scan.nextLine();
		int index = 0;
		int start = 0;
		for(int i = 0; i<s.length(); i++) {
			char ch = s.charAt(i);
			if(ch >= '0' && ch <= '9') continue;
			if(ch == k.charAt(index)) {
				//System.out.println("same");
				if(index == 0) {
					//System.out.println("i:"+i);
					start = i;
				}
				index++;
			} else {
				//System.out.println("diff");
				index = 0;
				i = start++;
			}
		}
		if(index == k.length()) {
			System.out.println(1);
		}else {
			System.out.println(0);
		}
	}
}
