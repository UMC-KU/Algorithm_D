package postfixNotation_1918;

import java.io.*;
import java.util.*;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String str = br.readLine();
		Stack<Character> sign = new Stack<>();
		for(int i = 0; i<str.length(); i++) {
			char ch = str.charAt(i);
			switch(ch) {
			case '+': case '-':	//이전 기호가 여는 괄호일 때까지 스택에 쌓인 기호들 모두 POP
				while(!sign.isEmpty() && sign.peek() != '(')
					bw.write(sign.pop());
				sign.add(ch);				//스택에 저장
				break;
			case '*': case '/':				//이전 기호가 나누기 곱하기가 아닐 때까지 POP  
				while(!sign.isEmpty() && (sign.peek() == '/' || sign.peek() == '*'))
					bw.write(sign.pop());
				sign.add(ch);				//스택에 기호 저장
				break;
			case '(':						//아무것도 하지 않고 그냥 스택에 저장
				sign.add(ch);
				break;
			case ')':						//이전 기호가 여는 괄호일 때까지 스택에 쌓인 기호들 모두 POP	
				while(!sign.isEmpty() && sign.peek() != '(')
					bw.write(sign.pop());
				sign.pop();					//여는 괄호가 스택에서 안빠졌기 때문에 한번 더 POP
				break;
			default:
				bw.write(ch);				//숫자일 경우 그냥 출력
			}
		}
		while(!sign.isEmpty()) bw.write(sign.pop());	//기호가 스택에 남아있으면 모두 순차적으로 POP
		bw.flush();
	}
}
