package whosetheWINNER_20154;

import java.util.*;

public class Main {

	public static void main(String[] args) {
		int[] stroke = { 3, 2, 1, 2, 3, 3, 3, 3, 1, 1, 3, 1, 3, 3, 1, 2, 2, 2, 1, 2, 1, 1, 2, 2, 2, 1 };
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		int[] num = new int[str.length()];
		int index = 0;
		for (char i : str.toCharArray()) {
			num[index++] = stroke[(int) (i - 'A')];
		}
		while (num.length > 1) {
			int[] num2 = new int[(num.length%2 == 0)?num.length/2:num.length/2+1];
			for (int i = 0; i < num.length; i = i + 2) {
				int temp = 0;
				if(i+1 >= num.length) {
					temp = num[i];
				}else {
					temp = (num[i] + num[i + 1]) % 10;
				}
				num2[i/2] = temp;
			}
			num = num2;
		}
		if(num[0]%2 == 1) System.out.println("I'm a winner!");
		else System.out.println("You're the winner?");
	}
}
