package spellingPW_4659;

import java.util.*;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String ans = "";
		while(true) {
			String str = sc.nextLine();
			if(str.equals("end")) break;
			ans+= (goodPW(str))?"<"+str+"> is acceptable.\n":"<"+str+"> is not acceptable.\n";
		}
		System.out.println(ans);
		
	}
	
	public static boolean goodPW(String str) {
		int[] alpha = {1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0};
		boolean isVowel = false;
		boolean isConso = false;
		boolean hasVowel = false;
		int case2 = 0;
		for(int i = 0; i<str.length(); i++) {
			char ch = str.charAt(i);
			try {
				if(str.charAt(i-1) == ch) {
					if(ch-'a' != 4 && ch-'a' != 14) {
						return false;
					}
				}
			} catch(IndexOutOfBoundsException e) {}
			
			if(alpha[ch-'a'] == 1) {
				hasVowel = true;
				if(isVowel) {
					case2++;
				} else{
					isConso = false;
					isVowel = true;
					case2 = 1;
				}
			} else {
				if(isConso) {
					case2++;
				} else  {
					isVowel = false;
					isConso = true;
					case2 = 1;
				}
			}
			System.out.println(case2);
			if(case2 >= 3)	return false;
		}
		if(!hasVowel) return false;
		return true;
	}
}
