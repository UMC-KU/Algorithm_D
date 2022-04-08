package horizontalReading_10798;

import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		String[] str = new String[5];
		int maxIndex = 0;
		for(int i = 0; i<str.length; i++) {
			str[i] = sc.nextLine();
			if(str[i].length() > str[maxIndex].length()) {
				maxIndex = i;
			}
		}
		String ans = "";
		for(int j = 0; j<str[maxIndex].length(); j++) {
			for(int i = 0; i<str.length; i++) {
				try {
					ans += str[i].charAt(j);
				} catch(IndexOutOfBoundsException e) {}
			}
		}
		System.out.println(ans);
	}
}
