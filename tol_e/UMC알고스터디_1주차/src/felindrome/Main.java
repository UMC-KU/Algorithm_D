package felindrome;

import java.util.*;
public class Main {
	public static boolean isPrime(int num) {
		if(num == 1) return false;
		for(int i = 2; i<=(int)Math.sqrt(num); i++) {
			if(num%i == 0)
				return false;
		}
		return true;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for(int i = n;; i++) {
			if(isPrime(i)) {
				String str = Integer.toString(i);
				for(int s = 0; s<=str.length()/2; s++) {
					if(str.charAt(s) != str.charAt(str.length()-1-s))
						break;
					if(s == str.length()/2) {
						System.out.println(str);
						return;
					}
				}
			}
		}
	}
}
