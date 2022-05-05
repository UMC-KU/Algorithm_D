package prefixNotation_1935;

import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		//BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		String str = br.readLine();
		double[] temp = new double[n];
		Stack<Double> num = new Stack<>();
		Stack<Character> sign = new Stack<>();
		for (int i = 0; i < n; i++) {
			temp[i] = Integer.parseInt(br.readLine());	//각 알파벳에 대응되는 숫자 입력
		}

		double a = 0, b = 0;
		for (int i = 0; i < str.length(); i++) {	//괄호가 없으므로 부호가 나오면 계산 실행
			char ch = str.charAt(i);
			switch (ch) {
			case '+':
				num.push(num.pop() + num.pop());
				break;
			case '-':
				a = num.pop();
				b = num.pop();
				num.push(b - a);
				break;
			case '*':
				num.push(num.pop() * num.pop());
				break;
			case '/':
				a = num.pop();
				b = num.pop();
				num.push(b / a);
				break;
			default:						//알파벳이 나오면 해당 알파벳 순번으로 TEMP를 탐색하여 대응되는 숫자를 가져온다
				num.push(temp[ch - 'A']);
				break;
			}
		}
		System.out.printf("%.2f", num.pop());	//출력타입 -> 소수점 밑 두자리
	}
}
