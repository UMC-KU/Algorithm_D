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
			case '+': case '-':	//���� ��ȣ�� ���� ��ȣ�� ������ ���ÿ� ���� ��ȣ�� ��� POP
				while(!sign.isEmpty() && sign.peek() != '(')
					bw.write(sign.pop());
				sign.add(ch);				//���ÿ� ����
				break;
			case '*': case '/':				//���� ��ȣ�� ������ ���ϱⰡ �ƴ� ������ POP  
				while(!sign.isEmpty() && (sign.peek() == '/' || sign.peek() == '*'))
					bw.write(sign.pop());
				sign.add(ch);				//���ÿ� ��ȣ ����
				break;
			case '(':						//�ƹ��͵� ���� �ʰ� �׳� ���ÿ� ����
				sign.add(ch);
				break;
			case ')':						//���� ��ȣ�� ���� ��ȣ�� ������ ���ÿ� ���� ��ȣ�� ��� POP	
				while(!sign.isEmpty() && sign.peek() != '(')
					bw.write(sign.pop());
				sign.pop();					//���� ��ȣ�� ���ÿ��� �Ⱥ����� ������ �ѹ� �� POP
				break;
			default:
				bw.write(ch);				//������ ��� �׳� ���
			}
		}
		while(!sign.isEmpty()) bw.write(sign.pop());	//��ȣ�� ���ÿ� ���������� ��� ���������� POP
		bw.flush();
	}
}
