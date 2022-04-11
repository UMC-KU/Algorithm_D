package warning_3029;

import java.util.*;
public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String t = sc.nextLine();
		String[] curTime = t.split(":");
		t = sc.nextLine();
		String[] naTime = t.split(":");
		int[] max = {24,60,60};
		int[] ans = new int[3];
		int next = 0;
		boolean isSame = true;
		for(int i = 2; i>=0; i--) {
			ans[i] = Integer.parseInt(naTime[i]) - Integer.parseInt(curTime[i])-(next);
			if(ans[i] != 0) isSame = false;
			next = 0;
			if(ans[i] < 0) {
				ans[i] = max[i]+ans[i];
				next++;
			}
		}
		if(isSame) {
			ans[0] = 24;
			ans[1] = 0;
			ans[2] = 0;
		}
		for(int i = 0; i<3; i++) {
			System.out.printf("%02d",ans[i]);
			if(i!=2)System.out.print(":");
		}
	}
}
