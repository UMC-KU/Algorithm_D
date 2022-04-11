package decoding_9046;

import java.util.*;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		sc.nextLine();
		String ans = "";
		while((t--)>0) {
			int[] alphabet = new int[26];
			String str = sc.nextLine();
			for(char c:str.toCharArray()) {
				if(c>='a') alphabet[(int)(c-'a')]++;
			}
			
			int max = 0;
			int maxIndex = 0;
			boolean isMultiple = false;
			for(int i = 0; i<alphabet.length; i++) {
				if(max < alphabet[i]) {
					maxIndex = i;
					max = alphabet[i];
					isMultiple = false;
				} else if(max == alphabet[i]) {
					isMultiple = true;
				}
			}
			if(isMultiple) 	ans+="?\n";
			else ans += (char)('a' + maxIndex)+"\n";
		}
		System.out.println(ans);
	}
}
