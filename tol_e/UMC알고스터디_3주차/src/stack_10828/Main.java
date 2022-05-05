package stack_10828;

import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		Stack<Integer> stack = new Stack<Integer>();	// 정수를 쌓아놓는 스택 
		int repeat = Integer.parseInt(br.readLine());	//반복 횟수

		for (int i = 0; i < repeat; i++) {
			String o = br.readLine();	//명령
			String[] p = o.split(" ");	//연산 방법과 숫자를 구분
			if (p[0].equals("push")) {	//push : 추가
				stack.push(Integer.parseInt(p[1]));
			} else if (o.equals("pop")) {	//pop : 제거 (제거되는 값 리턴)
				try {						//try-catch를 통한 빈스택에러 예외처리
					bw.write(stack.pop() + "\n");
				} catch (EmptyStackException e) {
					bw.write("-1\n");
				}
			} else if (o.equals("size")) {	//size : 스택 사이즈 출력
				bw.write(Integer.toString(stack.size()) + "\n");
			} else if (o.equals("empty")) {	//비어있다?1:0
				if (stack.isEmpty()) {
					bw.write("1\n");
				} else {
					bw.write("0\n");
				}
			} else if (o.equals("top")) {	//가장 위에 있는 (마지막으로 추가된 값)
				try {						//try-catch를 통한 빈스택에러 예외처리
					bw.write(Integer.toString(stack.peek()) + "\n");
				} catch (EmptyStackException e) {
					bw.write("-1\n");
				}
			}
		}
		bw.flush();
		bw.close();
		br.close();
	}
}