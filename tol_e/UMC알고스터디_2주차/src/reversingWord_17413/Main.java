package reversingWord_17413;

import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		Stack<Character> rev = new Stack<>();
		String ans = "";
		boolean isTag = false;
		for (int i = 0; i < str.length(); i++) {
			char ch = str.charAt(i);
			switch (ch) {
			case '<': {
				if(!isTag) {
					while (!rev.isEmpty())
						ans += rev.pop();
				}
				isTag = true;
				break;
			}
			case '>': {
				isTag = false;
				break;
			}
			case ' ': {
				if(!isTag) {
					while (!rev.isEmpty())
						ans += rev.pop();
					break;
				}
			}
			default: {
				if (isTag) {
					break;
				} else {
					rev.add(ch);
					if(i == str.length()-1) {
						while(!rev.isEmpty())
							ans += rev.pop();
					}
					continue;
				}
			}
			}
			ans += ch;
		}
		System.out.println(ans);
	}
}
