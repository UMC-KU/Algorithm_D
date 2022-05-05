package fePipe_10799;

import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		Stack<Character> st = new Stack<>();
		long ans = 0;
		for(int i = 0; i<str.length(); i++) {
			char ch = str.charAt(i);
			if(ch == '(') {
				if(str.charAt(i+1) == ')') {	//���� ���ڰ� ')'�̸� ���������� �Ǻ�
					ans += st.size();			//�������� ��� ��� ���� �� ������ '(' ���� �� ������ �����ش�
					i++;						//���� ���ڸ� �̹� Ž���߱� ������ �ε����� �ϳ� �� �÷��ش�
				} else {						//���� ���ڰ� '('�� ��� �׳� Ǫ��
					st.push(ch);
				}
			}else if(ch == ')') {				//')'������ �׻� '('�� ���� ������ ����Ⱑ �����Ƿ� pop�� �ϰ�
					st.pop();
					ans++;						//������ �������� ���� �������� �����Ƿ� ans+1�� ���ش�.
			}
		}
		System.out.println(ans);
	}
}
