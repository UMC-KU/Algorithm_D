package groupWordChecker_1316;

import java.util.*;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.nextLine();
		int count = 0;
		while((n--)>0) {
			String str = sc.nextLine();
			int[] num = new int[26];
			boolean isGroup = true;
			num[str.charAt(0)-'a']++;
			for(int i = 1; i<str.length(); i++) {
				char c = str.charAt(i);
				if(num[c-'a'] > 0) {
					if(str.charAt(i-1) != c) {
						//System.out.println(str.charAt(i-1)+" / "+c);
						isGroup = false;
						break;
					}
				}
				num[c-'a']++;
			}
			if(isGroup) {
				count++;
			}
		}
		System.out.println(count);
	}
}
