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
			temp[i] = Integer.parseInt(br.readLine());	//�� ���ĺ��� �����Ǵ� ���� �Է�
		}

		double a = 0, b = 0;
		for (int i = 0; i < str.length(); i++) {	//��ȣ�� �����Ƿ� ��ȣ�� ������ ��� ����
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
			default:						//���ĺ��� ������ �ش� ���ĺ� �������� TEMP�� Ž���Ͽ� �����Ǵ� ���ڸ� �����´�
				num.push(temp[ch - 'A']);
				break;
			}
		}
		System.out.printf("%.2f", num.pop());	//���Ÿ�� -> �Ҽ��� �� ���ڸ�
	}
}
