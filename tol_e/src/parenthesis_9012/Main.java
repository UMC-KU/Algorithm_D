package parenthesis_9012;

import java.io.*;
import java.util.*;

public class Main {

	static boolean checkVPS(String s) {
		Stack<Character> a = new Stack<Character>();
		for(char i:s.toCharArray()) {
			if(i =='(') a.add(i);							// '('이 들어오면 push.
			else if(i == ')') {								// ')'이 들어온 경우,
				if(a.empty()||a.peek() == ')') a.add(i);	// 다시 ')'이거나 빈 스택인 경우 추가,
				else a.pop();								// '(' 일 경우 pop으로 '('제거
			}
		}
		if(a.empty()) return true;							// 마지막에 스택이 빈 경우 조건에 부합
		else return false;
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		String str = "";
		for(int i = 0; i<n; i++) {
			str = br.readLine();
			if(checkVPS(str)) bw.write("YES\n");
			else bw.write("NO\n");
		}
		bw.flush();
	}
}
